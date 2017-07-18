# -*- coding: utf-8 -*-
import hashlib
import json
import time

import scrapy
from scrapy import Selector

from libMe.db.LogDao import LogDao
from libMe.util import NetworkUtil
from libMe.util import TimerUtil
from ..items import TXContentItem

isEnd = False


# 60s/120s/300s 刷新一次
class TXDetailSpider(scrapy.Spider):
    name = 'tx_detail'
    download_delay = 5  # 基础间隔 0.5*download_delay --- 1.5*download_delays之间的随机数
    handle_httpstatus_list = [301, 302, 204, 206, 403, 404, 500]  # 可以处理重定向及其他错误码导致的 页面无法获取解析的问题

    def __init__(self, name=None, **kwargs):
        super(TXDetailSpider, self).__init__(name=None, **kwargs)
        self.count = 0
        self.request_stop = False
        self.request_stop_time = 0
        self.logDao = LogDao('tx_list_detail')

    def start_requests(self):
        # while True:
            # 检测网络
            if not NetworkUtil.checkNetWork():
                # 20s检测一次
                TimerUtil.sleep(20)
                self.logDao.warn(u'检测网络不可行')
                # continue

            # 检测服务器
            if not NetworkUtil.checkService():
                # 20s检测一次
                TimerUtil.sleep(20)
                self.logDao.warn(u'检测服务器不可行')
                # continue

            # 进行页面访问
            newUrl = 'http://tech.qq.com/l/scroll.htm'
            self.logDao.warn(u'进行抓取列表:' + newUrl)
            yield scrapy.Request(url=newUrl,
                                 meta={'request_type': 'tx_page_list', 'url': newUrl},
                                 callback=self.parseArticleList, dont_filter=True)

    # TODO...还没有遇到被禁止的情况
    def parseArticleList(self, response):
        url = response.meta['url']
        body = response.body.decode('gbk')
        self.logDao.info(u'开始解析列表')
        selector = Selector(text=body)

        articles = selector.xpath('//div[@class="mod newslist"]//li')
        for article in articles:
            source_url = article.xpath('a/@href').extract_first('')
            title = article.xpath('a/text()').extract_first('')
            post_date = article.xpath('span/text()').extract_first('')
            post_date = time.strftime('%Y', time.localtime(time.time())) + u'年' + post_date
            self.logDao.info(u'抓取文章' + title + ':' + post_date + ':' + source_url)
            yield scrapy.Request(url=source_url,
                                 meta={'request_type': 'tx_detail', "title": title, 'post_date': post_date,
                                       "source_url": source_url},
                                 callback=self.parseArticle)

    def parseArticle(self, response):
        title = response.meta['title']
        post_date = response.meta['post_date']
        source_url = response.meta['source_url']
        body = response.body.decode('gbk')
        self.logDao.info(u'开始解析文章:' + title + ':' + post_date + ':' + source_url)

        selector = Selector(text=body)
        post_user = selector.xpath('//*[@bosszone="jgname"]/text() | //*[@bosszone="jgname"]/a/text()').extract()
        if post_user:
            post_user = ''.join(post_user)
        else:
            post_user = ''

        page_content = selector.xpath('//div[@id="Cnt-Main-Article-QQ"]')

        # 解析文档中的所有图片url，然后替换成标识
        image_urls = []
        imgs = page_content.xpath('descendant::img')
        page_content = page_content.extract_first(default='').replace('\t', '').replace('\n', '')
        for img in imgs:
            # 图片可能放在src
            image_url = img.xpath('@src').extract_first()
            if image_url and image_url.startswith('http'):
                self.logDao.info(u'得到图片：' + image_url)
                m2 = hashlib.md5()
                m2.update(image_url)
                image_hash = m2.hexdigest()
                image_urls.append({
                    'url': image_url,
                    'hash': image_hash
                })
                # 替换url为hash
                page_content = page_content.replace(image_url, image_hash)

        m2 = hashlib.md5()
        m2.update(source_url.encode('utf8'))
        urlHash = m2.hexdigest()

        main = {
            'title': title,
            'post_date': post_date,
            'post_user': post_user,
            'page_content': page_content,
            'tags': '',
            'channel_name': ''
        }
        self.saveFile(urlHash, json.dumps(main, encoding="utf8", ensure_ascii=False))

        contentItem = TXContentItem()
        contentItem['channel_name'] = ''
        contentItem['source_url'] = source_url
        contentItem['title'] = title
        contentItem['post_date'] = post_date
        contentItem['post_user'] = post_user
        contentItem['image_urls'] = image_urls
        contentItem['page_content'] = page_content
        contentItem['tags'] = ''
        return contentItem

    def saveFile(self, title, content):
        filename = 'html/%s.json' % title
        with open(filename, 'wb') as f:
            f.write(content.encode("utf8"))
        self.log('Saved file %s' % filename)
