# -*- coding: utf-8 -*-
import json
import time

import demjson
import scrapy
from scrapy import Selector

from libMe.db.LogDao import LogDao
from libMe.util import CssUtil
from libMe.util import EncryptUtil
from libMe.util import NetworkUtil
from libMe.util import EncodeUtil
from libMe.util import TimerUtil
from ..db.CheckDao import CheckDao
from ..items import ContentItem
from libMe.db.DataMonitorDao import DataMonitorDao


# 60s/120s/300s 刷新一次
class TXDetailSpider(scrapy.Spider):
    name = 'jiemian_detail'
    download_delay = 2.5  # 基础间隔 0.5*download_delay --- 1.5*download_delays之间的随机数
    handle_httpstatus_list = [301, 302, 204, 206, 403, 404, 500]  # 可以处理重定向及其他错误码导致的 页面无法获取解析的问题

    def __init__(self, name=None, **kwargs):
        super(TXDetailSpider, self).__init__(name=None, **kwargs)
        self.count = 0
        self.request_stop = False
        self.request_stop_time = 0
        self.logDao = LogDao(self.logger, 'jiemian_list_detail')
        self.checkDao = CheckDao()
        # 用于缓存css
        self.css = {
            'hash': 'style'
        }
        self.dataMonitor = DataMonitorDao()
        self.isRunningStop = False

    def close(spider, reason):
        if not spider.isRunningStop:
            # 如果启动爬虫时候，还有未完成的抓取，此时不应该设置状态为停止，反之
            spider.saveStatus('stop')
        # spider.dataMonitor.updateTotal('jiemian_total')
        pass

    def start_requests(self):
        # 如果正在爬，就不请求
        status = self.getStatus()
        if status == 'running':
            self.isRunningStop = True
            return
        self.saveStatus('running')

        # 检测网络
        while not NetworkUtil.checkNetWork():
            # 20s检测一次
            TimerUtil.sleep(20)
            self.logDao.warn(u'检测网络不可行')

        # 检测服务器
        while not NetworkUtil.checkService():
            # 20s检测一次
            TimerUtil.sleep(20)
            self.logDao.warn(u'检测服务器不可行')
        # 必读 玩物 产品榜 快报 游戏要闻 单品 盘点 花边要闻 游戏快报
        cids = [
            {'src_channel': '界面新闻', 'sub_channel': '界面科技-必读', 'num': '6'},
            {'src_channel': '界面新闻', 'sub_channel': '界面科技-玩物', 'num': '66'},
            {'src_channel': '界面新闻', 'sub_channel': '界面科技-产品榜', 'num': '73'},
            {'src_channel': '界面新闻', 'sub_channel': '界面科技-快报', 'num': '84'},
            {'src_channel': '界面新闻', 'sub_channel': '界面游戏-游戏要闻', 'num': '100'},
            {'src_channel': '界面新闻', 'sub_channel': '界面游戏-单品', 'num': '119'},
            {'src_channel': '界面新闻', 'sub_channel': '界面游戏-盘点', 'num': '120'},
            {'src_channel': '界面新闻', 'sub_channel': '界面游戏-花边要闻', 'num': '121'},
            {'src_channel': '界面新闻', 'sub_channel': '界面游戏-游戏快报', 'num': '122'}
        ]
        # 必读
        url = 'https://a.jiemian.com/index.php?m=lists&a=ajaxlist&callback=&_=1502103362598&page='
        for cid in cids:
            for page in range(1, 2):
                cidNum = cid.get('num')
                src_channel = cid.get('src_channel')
                sub_channel = cid.get('sub_channel')
                newUrl = url + str(page) + ('&cid=' + cidNum)
                self.logDao.warn(u'进行抓取列表:' + newUrl)
                yield scrapy.Request(url=newUrl,
                                     meta={'request_type': 'jiemian_page_list', 'url': newUrl,
                                           'src_channel': src_channel,
                                           'sub_channel': sub_channel
                                           },
                                     callback=self.parseArticleList, dont_filter=True)

    # TODO...还没有遇到被禁止的情况
    def parseArticleList(self, response):
        body = EncodeUtil.toUnicode(response.body)
        if False:
            self.logDao.info(u'访问过多被禁止')
        else:
            # 格式化
            jsonStr = demjson.decode(body.lstrip('(').rstrip(')')) or {}
            rst = jsonStr.get('rst', '')
            if not rst:
                self.logDao.info(u'不存在内容')
                return
            self.logDao.info(u'开始解析列表')
            src_channel = response.meta['src_channel']
            sub_channel = response.meta['sub_channel']
            selector = Selector(text=rst)
            articles = selector.xpath('//div[boolean(contains(@class,"news-view"))]')
            for article in articles:
                source_url = article.xpath('.//div[@class="news-header"]//a/@href').extract_first('')
                title = article.xpath(
                    './/div[@class="news-header"]//a/@title | .//div[@class="news-header"]//a/text()').extract_first('')
                post_date = article.xpath('.//div[@class="news-footer"]//span[@class="date"]/text()').extract_first('')
                tags = article.xpath('.//div[@class="news-tag"]/a/text()').extract()

                if not source_url:
                    self.logDao.info(u'文章不存在' + title + ':' + source_url + ':' + post_date)
                    continue

                # 如果存在则不抓取
                if self.checkDao.checkExist(source_url):
                    self.logDao.info(u'文章已经存在' + title + ':' + source_url + ':' + post_date)
                    continue

                self.logDao.info(u'抓取文章' + title + ':' + source_url + ':' + post_date)

                yield scrapy.Request(url=source_url,
                                     meta={'request_type': 'jiemian_detail', "title": title, 'post_date': post_date,
                                           'sub_channel': sub_channel,
                                           'src_channel': src_channel,
                                           'tags': tags,
                                           'source_url': source_url},
                                     callback=self.parseArticle)

    def parseArticle(self, response):
        body = EncodeUtil.toUnicode(response.body)
        if False:
            self.logDao.info(u'访问过多被禁止')
        else:
            title = response.meta['title']
            post_date = response.meta['post_date']
            source_url = response.meta['source_url']
            sub_channel = response.meta['sub_channel']
            src_channel = response.meta['src_channel']
            tags = response.meta['tags']
            self.logDao.info(u'开始解析文章:' + title + ':' + post_date + ':' + source_url)

            selector = Selector(text=body)

            # 得到样式
            styleUrls = selector.xpath('//link[@rel="stylesheet"]/@href').extract()
            styleList = []
            for styleUrl in styleUrls:
                if styleUrl.startswith('//'):
                    styleUrl = 'http:' + styleUrl
                # 得到hash作为key
                styleUrlHash = EncryptUtil.md5(styleUrl)
                if not self.css.get(styleUrlHash):
                    # 不存在则去下载 并保存
                    self.css[styleUrlHash] = CssUtil.downLoad(styleUrl)
                styleList.append(self.css[styleUrlHash])
            styles = CssUtil.compressCss(styleList).replace('\'', '"').replace('\\', '\\\\')

            # 替换样式里面的链接
            styles = CssUtil.clearUrl(styles)
            styles = CssUtil.clearBackgroundColor(styles, ['#f5f5f5'])

            post_user = selector.xpath('//div[@class="article-info"]//span[@class="author"]//text()').extract_first('')

            src_ref = src_channel

            post_date = selector.xpath('//div[@class="article-info"]//span[@class="date"]//text()').extract_first('')

            try:
                post_date = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(post_date, "%Y/%m/%d %H:%M"))
            except Exception:
                pass

            tags_ = selector.xpath('//div[@class="article-info"]//*[@class="tags"]//text()').extract()
            tags = tags + tags_
            tags = ','.join(tags)

            """
                article-main
                    article-img
                    article-content
                        p
                        article-source
                            p:来源
                            p:点击下载“界面新闻”APP 不抓
            """

            # 得到article-img
            article_img = selector.xpath('//div[@class="article-main"]/div[@class="article-img"]').extract_first('')

            # 得到article-content
            article_content = selector.xpath('//div[@class="article-main"]/div[@class="article-content"]').extract_first('')

            if not article_content:
                self.logDao.info(u'文章不存在' + title + ':' + source_url + ':' + post_date)
                return

            contentSelector = Selector(text=article_content)
            content_items = contentSelector.xpath('//div[@class="article-content"]/*[not(name(.)="script") and not('
                                                  'name(.)="iframe") and not(name(.)="style") and not(boolean( '
                                                  'contains(a//@href,"?m=app"))) and not(boolean(@class="share-view" '
                                                  'or @class="article-source"))]')

            # 得到来源 做替换
            contentSource = contentSelector.xpath('//div[@class="article-content"]/div[@class="article-source"]/p/text()').extract_first('')
            if contentSource:
                contentSource = contentSource.replace(u'来源：', u'')
                src_ref = contentSource

            # 得到纯文本
            content_txt = []
            for item in content_items:
                # 文本
                allTxt = item.xpath('.//text()').extract()
                allTxt = ''.join(allTxt).replace('\t', '')
                # 加入
                content_txt.append(allTxt)
            content_txt = '\n'.join(content_txt)

            # 组装新的内容标签
            outHtml = u"""<div class="article-main">${++articleImg++}<div class="article-content" style="font-family:
            'Microsoft YaHei', 黑体;">${++content++}</div></div> """

            content_items = content_items.extract()
            content_items = ''.join(content_items)

            content_html = outHtml.replace('${++articleImg++}', article_img).replace('${++content++}', content_items)

            selector = Selector(text=content_html)
            # 解析文档中的所有图片url，然后替换成标识
            image_urls = []
            imgs = selector.xpath('descendant::img')

            for img in imgs:
                # 图片可能放在src 或者data-src
                image_url_base = img.xpath('@src').extract_first('')
                if image_url_base.startswith('//'):
                    image_url = 'http:' + image_url_base
                else:
                    image_url = image_url_base
                if image_url and image_url.startswith('http'):
                    self.logDao.info(u'得到图片：' + image_url)
                    image_urls.append({
                        'url': image_url,
                    })
                    content_html = content_html.replace(image_url_base, image_url)

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
            contentItem['sub_channel'] = sub_channel
            contentItem['post_user'] = post_user
            contentItem['tags'] = tags
            contentItem['styles'] = styles
            contentItem['content_html'] = content_html
            contentItem['hash_code'] = hash_code
            contentItem['info_type'] = 1
            contentItem['src_source_id'] = 5
            # contentItem['src_account_id'] = 0
            contentItem['src_channel'] = src_channel
            contentItem['src_ref'] = src_ref
            return contentItem

    def saveFile(self, title, content):
        filename = 'html/%s.html' % title
        with open(filename, 'wb') as f:
            f.write(content.encode("utf8"))
        self.log('Saved file %s' % filename)

    def getStatus(self):
        loadF = None
        try:
            with open("catchStatus.json", 'r') as loadF:
                aa = json.load(loadF)
                return aa.get('status')
        finally:
            if loadF:
                loadF.close()

    def saveStatus(self, status):
        loadF = None
        try:
            with open("catchStatus.json", "w") as loadF:
                json.dump({'status': status}, loadF)
        finally:
            if loadF:
                loadF.close()
