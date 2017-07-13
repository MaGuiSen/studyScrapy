# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy import cmdline


class IPSpider(scrapy.Spider):
    name = 'crawl_ip'
    # Ignoring response <503 http://www.xicidaili.com/>: HTTP status code is not handled or not allowed   503 Service Unavailable
    def start_requests(self):
        urls = [
            'http://blog.csdn.net/wangzhaotongalex/article/details/49157043',
        ]
        for url in urls:
            print u'请求url：' + url
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print u'开始解析。。。'
