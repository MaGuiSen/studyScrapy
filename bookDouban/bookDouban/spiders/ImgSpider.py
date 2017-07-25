# -*- coding: utf-8 -*-

import scrapy

from items import ContentItem


class ImgSpider(scrapy.Spider):
    name = 'img_crawl'
    def start_requests(self):
        urls = [
            'https://segmentfault.com/a/1190000003112597',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def close(spider, reason):
        print 'close'

    def parse(self, response):
        print u'开始解析。。。'
        image_urls = []
        image_urls.append({
            'url': 'http://n.sinaimg.cn/tech/crawl/20170725/nFQc-fyiiahz0277318.jpg',
        })
        item = ContentItem()
        item['image_urls'] = image_urls
        return item
