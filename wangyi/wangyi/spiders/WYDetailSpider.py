# -*- coding: utf-8 -*-
import random

import demjson
import scrapy
from scrapy import Selector

from libMe.db.LogDao import LogDao
from libMe.util import CssUtil
from libMe.util import EncryptUtil
from libMe.util import NetworkUtil
from libMe.util import TimerUtil
from libMe.util import EncodeUtil
from ..db.CheckDao import CheckDao
from ..items import ContentItem
from libMe.db.DataMonitorDao import DataMonitorDao


# 60s/120s/300s 刷新一次
class WYDetailSpider(scrapy.Spider):
    name = 'wangyi_detail'
    download_delay = 2.5  # 基础间隔 0.5*download_delay --- 1.5*download_delays之间的随机数
    handle_httpstatus_list = [301, 302, 204, 206, 403, 404, 500]  # 可以处理重定向及其他错误码导致的 页面无法获取解析的问题

    def __init__(self, name=None, **kwargs):
        super(WYDetailSpider, self).__init__(name=None, **kwargs)
        self.count = 0
        self.request_stop = False
        self.request_stop_time = 0
        self.logDao = LogDao(self.logger,'wangyi_list_detail')
        self.checkDao = CheckDao()
        # 用于缓存css
        self.css = {
            'hash': 'style'
        }
        self.dataMonitor = DataMonitorDao()

    def close(spider, reason):
        spider.dataMonitor.updateTotal('wangyi_total')

    def start_requests(self):
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

            src_channel = '网易科技'
            # 进行页面访问
            newUrl = 'http://tech.163.com/special/00094IHV/news_json.js?' + str(random.uniform(0, 1))
            self.logDao.warn(u'进行抓取列表:' + newUrl)
            yield scrapy.Request(url=newUrl,
                                 meta={'request_type': 'wangyi_page_list', 'url': newUrl,
                                       'src_channel': src_channel},
                                 callback=self.parseArticleList, dont_filter=True)

            src_channel = '网易财经'
            # 进行页面访问
            newUrl = 'http://money.163.com/special/00251G8F/news_json.js?' + str(random.uniform(0, 1))
            self.logDao.warn(u'进行抓取列表:' + newUrl)
            yield scrapy.Request(url=newUrl,
                                 meta={'request_type': 'wangyi_page_list', 'url': newUrl,
                                       'src_channel': src_channel},
                                 callback=self.parseArticleList, dont_filter=True)

    # TODO...还没有遇到被禁止的情况
    def parseArticleList(self, response):
        url = response.meta['url']
        body = EncodeUtil.toUnicode(response.body)
        if False:
            self.logDao.info(u'访问过多被禁止')
        else:
            src_channel = response.meta['src_channel']
            self.logDao.info(u'开始解析列表')
            body = body.lstrip('var data=').rstrip(';')
            # 格式化
            jsonStr = demjson.decode(body) or {}
            articles = jsonStr.get('news') or []
            categoryList = jsonStr.get('category') or []
            for article_ins in articles:
                for article in article_ins:
                    source_url = article.get('l', '')
                    title = article.get('t', '')
                    timeStr = article.get('p', '')
                    # 如果存在则不抓取
                    if self.checkDao.checkExist(source_url):
                        self.logDao.info(u'文章已经存在' + title + timeStr + source_url)
                        continue
                    categoryIndex = article.get('c')
                    category = ''
                    if 0 <= categoryIndex < len(categoryList):
                        category = categoryList[categoryIndex].get('n')
                    post_date = article.get('p')
                    self.logDao.info(u'抓取文章' + title + ':' + post_date + ':' + source_url)
                    yield scrapy.Request(url=source_url,
                                         meta={'request_type': 'wangyi_detail', "title": title, 'category':category,'post_date': post_date,
                                               "source_url": source_url,
                                               'src_channel': src_channel},
                                         callback=self.parseArticle)

    def parseArticle(self, response):
        body = EncodeUtil.toUnicode(response.body)
        if False:
            self.logDao.info(u'访问过多被禁止')
        else:
            category = response.meta['category']
            src_channel = response.meta['src_channel']
            title = response.meta['title']
            post_date = response.meta['post_date']
            source_url = response.meta['source_url']
            self.logDao.info(u'开始解析文章:' + title + ':' + post_date + ':' + source_url)
            if not body:
                return
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

            src_ref = selector.xpath('//*[@id="ne_article_source"]/text()').extract_first()
            content_html = selector.xpath('//*[@id="endText"]')
            if not len(content_html):
                self.logDao.info(u'不存在内容：' + source_url)
                return
            # 去除内部不需要的标签
            # 完整案例：content_html.xpath('*[not(boolean(@class="entHdPic" or @class="ep-source cDGray")) and not(name(.)="script")]').extract()
            content_items = content_html.xpath('*[not(boolean(@class="gg200x300" or @class="ep-source cDGray")) and not(name(.)="script")]')
            if not len(content_items):
                self.logDao.info(u'不存在内容：' + source_url)
                return
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
            outHtml = """<div class="post_text" id="endText" style="border-top:1px solid #ddd;" jcid="5611">${++content++}</div>"""
            content_items = content_items.extract()
            content_items = ''.join(content_items)

            content_html = outHtml.replace('${++content++}', content_items)

            selector = Selector(text=content_html)
            # 解析文档中的所有图片url，然后替换成标识
            image_urls = []
            imgs = selector.xpath('descendant::img')

            for img in imgs:
                # 图片可能放在src 或者data-src
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
            contentItem['post_user'] = ''
            contentItem['tags'] = ''
            contentItem['styles'] = styles
            contentItem['content_html'] = content_html
            contentItem['hash_code'] = hash_code
            contentItem['info_type'] = 1
            contentItem['src_source_id'] = 4
            # contentItem['src_account_id'] = 0
            contentItem['src_channel'] = src_channel
            contentItem['src_ref'] = src_ref
            return contentItem

    def saveFile(self, title, content):
        filename = 'html/%s.html' % title
        with open(filename, 'wb') as f:
            f.write(content.encode("utf8"))
        self.log('Saved file %s' % filename)
