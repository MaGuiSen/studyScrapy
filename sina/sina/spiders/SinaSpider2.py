# -*- coding: utf-8 -*-
import random
import time

import demjson
import scrapy
from scrapy import Selector

from libMe.db.DataMonitorDao import DataMonitorDao
from libMe.db.LogDao import LogDao
from libMe.util import CssUtil
from libMe.util import EncodeUtil
from libMe.util import EncryptUtil
from libMe.util import NetworkUtil
from libMe.util import TimerUtil
from ..db.CheckDao import CheckDao
from ..items import ContentItem


# 60s整体刷新一次
class SinaSpider(scrapy.Spider):
    name = 'sina2'
    download_delay = 2.5  # 基础间隔 0.5*download_delay --- 1.5*download_delays之间的随机数
    handle_httpstatus_list = [301, 302, 204, 206, 403, 404, 500]  # 可以处理重定向及其他错误码导致的 页面无法获取解析的问题

    # 错误码 [scrapy.downloadermiddlewares.retry] DEBUG: Retrying <GET http://tech.sina.com.cn/i/2017-07-18/doc-ifyiakur9086112.shtml> (failed 1 times): TCP connection timed out: 10060: �������ӷ���һ��ʱ���û����ȷ�𸴻����ӵ�����û�з�Ӧ�����ӳ���ʧ�ܡ�.
    # [scrapy.downloadermiddlewares.retry] DEBUG: Retrying <GET http://tech.sina.com.cn/i/2017-07-17/doc-ifyiakwa4300270.shtml> (failed 1 times): User timeout caused connection failure: Getting http://tech.sina.com.cn/i/2017-07-17/doc-ifyiakwa4300270.shtml took longer than 180.0 seconds..
    def __init__(self, name=None, **kwargs):
        super(SinaSpider, self).__init__(name=None, **kwargs)
        self.count = 0
        self.logDao = LogDao(self.logger, 'sina_detail')
        self.checkDao = CheckDao()
        # 用于缓存css
        self.css = {
            'hash': 'style'
        }
        self.dataMonitor = DataMonitorDao()
        self.logger.info(u'重走init')

    def close(spider, reason):
        spider.dataMonitor.updateTotal('sina_total')

    def start_requests(self):
        # while True:
        # 检测网络
        while not NetworkUtil.checkNetWork():
            # 20s检测一次
            TimerUtil.sleep(20)
            self.logDao.warn(u'检测网络不可行')
            # continue

        # 检测服务器
        while not NetworkUtil.checkService():
            # 20s检测一次
            TimerUtil.sleep(20)
            self.logDao.warn(u'检测服务器不可行')
            # continue

        src_channel = '新浪科技'

        # 进行爬虫
        url = 'http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=96&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=220&asc=&page=1'
        # url = 'http://tech.sina.com.cn/t/2017-07-24/doc-ifyihrit1274195.shtml'

        r = random.uniform(0, 1)
        newUrl = url + ('&r=' + str(r))
        self.logDao.info(u"开始抓取列表：" + newUrl)
        yield scrapy.Request(url=newUrl, meta={'request_type': 'sina_list', 'url': newUrl, 'src_channel': src_channel},
                             callback=self.parseList)

        # 补缺补漏
        url = 'http://feed.mix.sina.com.cn/api/roll/get?pageid=372&lid=2431&k=&num=50&page=1&callback=&_=1501148356254'
        r = random.uniform(0, 1)
        newUrl = url + ('&r=' + str(r))
        self.logDao.info(u"开始抓取列表：" + newUrl)
        yield scrapy.Request(url=newUrl, meta={'request_type': 'sina_list', 'url': newUrl, 'src_channel': src_channel},
                             callback=self.parseList2)

        # 新浪财经 要闻
        src_channel = '新浪财经'
        # 补缺补漏
        url = 'http://finance.sina.com.cn/'
        newUrl = url
        self.logDao.info(u"开始抓取列表：" + newUrl)
        yield scrapy.Request(url=newUrl, meta={'request_type': 'sina_list', 'url': newUrl, 'src_channel': src_channel},
                             callback=self.parseList3)

    # TODO。。还没有找到被禁止的情况
    def parseList3(self, response):
        body = EncodeUtil.toUnicode(response.body)
        if False:
            self.logDao.info(u'访问过多被禁止')
        else:
            src_channel = response.meta['src_channel']
            url = response.meta['url']
            self.logDao.info(u'开始解析列表' + url)

            selector = Selector(text=body)
            articles = selector.xpath('//*[@id="fin_tabs0_c0"]//a')
            # 格式化
            for article in articles:
                channel_name = u'财经'
                title = article.xpath('./text()').extract_first('')
                source_url = article.xpath('./@href').extract_first('')
                if not source_url:
                    continue

                callback = self.parseDetail2
                if self.checkDao.checkExist(source_url):
                    self.logDao.info(u'文章已经存在：' + title + source_url)
                    continue
                self.logDao.info(u"开始抓取文章：" + source_url)

                yield scrapy.Request(url=source_url,
                                     meta={'request_type': 'sina_detail', 'category': channel_name,
                                           'src_channel': src_channel,
                                           'title': title, 'source_url': source_url},
                                     callback=callback)

    # TODO。。还没有找到被禁止的情况
    def parseList2(self, response):
        data = EncodeUtil.toUnicode(response.body)
        if False:
            self.logDao.info(u'访问过多被禁止')
        else:
            src_channel = response.meta['src_channel']
            url = response.meta['url']
            self.logDao.info(u'开始解析列表' + url)

            # 格式化
            data = demjson.decode(data) or {}

            result = data.get('result', {})
            list = result.get('data', [])

            for item in list:
                channel_name = u'科技'
                title = item.get('title', '')
                source_url = item.get('url', '')
                callback = self.parseDetail2
                if self.checkDao.checkExist(source_url):
                    self.logDao.info(u'文章已经存在：' + title + source_url)
                    continue
                self.logDao.info(u"开始抓取文章：" + source_url)
                # item['url'] = "http://tech.sina.com.cn/d/f/2017-07-31/doc-ifyinvwu3872514.shtml"
                yield scrapy.Request(url=item['url'],
                                     meta={'request_type': 'sina_detail', 'category': channel_name,
                                           'src_channel': src_channel,
                                           'title': title, 'source_url': source_url},
                                     callback=callback)

    # TODO。。还没有找到被禁止的情况
    def parseList(self, response):
        data = EncodeUtil.toUnicode(response.body)
        if False:
            self.logDao.info(u'访问过多被禁止')
        else:
            src_channel = response.meta['src_channel']
            url = response.meta['url']
            self.logDao.info(u'开始解析列表' + url)

            data = data.lstrip('var jsonData = ').rstrip(';')
            # 格式化
            data = demjson.decode(data) or {}

            list = data.get('list', [])

            for item in list:
                channel = item.get('channel', {})
                channel_name = channel.get('title', '')
                title = item.get('title', '')
                source_url = item.get('url', '')
                callback = self.parseDetail2
                if self.checkDao.checkExist(source_url):
                    self.logDao.info(u'文章已经存在：' + title + source_url)
                    continue
                self.logDao.info(u"开始抓取文章：" + item['url'])
                # item['url'] = "http://tech.sina.com.cn/d/f/2017-07-31/doc-ifyinvwu3872514.shtml"
                yield scrapy.Request(url=item['url'],
                                     meta={'request_type': 'sina_detail', 'category': channel_name,
                                           'src_channel': src_channel,
                                           'title': title, 'source_url': source_url},
                                     callback=callback)

    def parseDetail2(self, response):
        body = EncodeUtil.toUnicode(response.body)
        if False:
            self.logDao.info(u'访问过多被禁止')
        else:
            src_channel = response.meta['src_channel']
            category = response.meta['category']
            title = response.meta['title']
            source_url = response.meta['source_url']
            self.logDao.info(u'开始解析文章:' + title + ':' + category + ':' + source_url)

            selector = Selector(text=body)

            # 得到样式
            styleUrls = selector.xpath('//link[@rel="stylesheet"]/@href').extract()
            styleList = []
            for styleUrl in styleUrls:
                # 得到hash作为key
                styleUrlHash = EncryptUtil.md5(styleUrl)
                if not self.css.get(styleUrlHash):
                    # 不存在则去下载 并保存
                    self.css[styleUrlHash] = CssUtil.downLoad(styleUrl)
                styleList.append(self.css[styleUrlHash])
            styles = CssUtil.compressCss(styleList).replace('\'', '"').replace('\\', '\\\\')
            styles = CssUtil.clearUrl(styles)
            styles = styles.replace('overflow-x:hidden', '').replace('overflow:hidden', '')

            title_ = selector.xpath('//*[@id="artibodyTitle"]/text()').extract_first('')
            if title_:
                title = title_

            post_date = selector.xpath('//*[@id="pub_date"]/text() | //*[@class="titer"]/text() | //meta[@name="weibo: article:create_at"]/@content').extract_first('')
            post_date = post_date.replace('\r\n', '').strip(' ').replace(u'年', '-').replace(u'月', '-').replace(u'日', ' ')

            try:
                post_date = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(post_date, "%Y-%m-%d %H:%M"))
            except Exception:
                try:
                    post_date = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(post_date, "%Y-%m-%d %H:%M:%S"))
                except Exception:
                    pass

            src_ref = selector.xpath(
                '//*[@id="media_name"]/a[1]/text() | //*[@class="source"]/a/text() | //*[@class="source"]/text() | //meta[@name="mediaid"]/@content').extract_first(
                '')

            post_user = selector.xpath('//*[@id="author_ename"]/a/text()').extract_first('')

            tags = selector.xpath('//p[@class="art_keywords"]/a/text() | //div[@class="article-keywords"]/a/text()').extract() or []
            tags = ','.join(tags)

            content_html = selector.xpath('//*[@id="artibody"][1]')
            if not len(content_html):
                self.logDao.info(u'不存在内容：' + source_url)
                return
            # 去除内部不需要的标签  2017-07-24 19:23
            # 完整案例：content_html.xpath('*[not(boolean(@class="entHdPic" or @class="ep-source cDGray")) and not(name(.)="script")]').extract()
            content_items = content_html.xpath('*[not(boolean(@class="entHdPic")) and not(name(.)="script")]')

            if not len(content_items):
                self.logDao.info(u'不存在内容：' + source_url)
                return
            # 得到纯文本
            content_txt = []
            for item in content_items:
                # 文本
                # TODO...之后处理 取出标题类型
                allTxt = item.xpath('.//text()').extract()
                allTxt = ''.join(allTxt).replace('\t', '')
                if u'来源：' in allTxt and len(allTxt) < 25:
                    # 说明这是真正的来源
                    if not post_user:
                        # 先替换作者 ，如果不存在的话
                        post_user = src_ref
                    src_ref = allTxt.replace(u'来源：', '').strip(u' ')
                # 加入
                content_txt.append(allTxt)
            content_txt = '\n'.join(content_txt)
            # 组装新的内容标签
            outHtml = """<div class="content_wrappr_left article article_16"><div class="content"><div class="BSHARE_POP blkContainerSblkCon clearfix blkContainerSblkCon_16" id="artibody">${++content++}</div></div></div>"""
            content_items = content_items.extract()
            content_items = ''.join(content_items)

            content_html = outHtml.replace('${++content++}', content_items)

            selector = Selector(text=content_html)
            # 解析文档中的所有图片url，然后替换成标识
            image_urls = []
            imgs = selector.xpath('descendant::img')

            for img in imgs:
                # 图片可能放在src
                image_url = img.xpath('@src').extract_first()
                if image_url and image_url.startswith('http'):
                    self.logDao.info(u'得到图片：' + image_url)
                    image_urls.append({
                        'url': image_url,
                    })

            urlHash = EncryptUtil.md5(source_url.encode('utf8'))
            self.saveFile(urlHash, body)

            # 得到hashCode
            hash_code = self.checkDao.getHashCode(source_url)

            # 去除 image 的 alt title
            selector = Selector(text=content_html)
            imgAltTitles = selector.xpath('//img/@alt|//img/@title').extract()
            # 处理提示块img的 alt title, 关注//img/@alt|//img/@title
            for imgAltTitle in imgAltTitles:
                if imgAltTitle.strip(' '):
                    content_html = content_html.replace(imgAltTitle, '')

            contentItem = ContentItem()
            contentItem['content_txt'] = content_txt
            contentItem['image_urls'] = image_urls
            contentItem['title'] = title
            contentItem['source_url'] = source_url
            contentItem['post_date'] = post_date
            contentItem['sub_channel'] = category
            contentItem['post_user'] = post_user
            contentItem['tags'] = tags
            contentItem['styles'] = styles
            contentItem['content_html'] = content_html
            contentItem['hash_code'] = hash_code
            contentItem['info_type'] = 1
            contentItem['src_source_id'] = 2
            # contentItem['src_account_id'] = 0
            contentItem['src_channel'] = src_channel
            contentItem['src_ref'] = src_ref
            return contentItem

    def saveFile(self, title, content):
        filename = 'html/%s.html' % title
        with open(filename, 'wb') as f:
            f.write(content.encode("utf8"))
        self.log('Saved file %s' % filename)
