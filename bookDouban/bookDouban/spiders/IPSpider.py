# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy import cmdline


class IPSpider(scrapy.Spider):
    name = 'crawl_ip'

    def start_requests(self):
        urls = [
            'http://www.xicidaili.com/',
        ]
        for url in urls:
            print u'请求url：' + url
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print u'开始解析。。。'
