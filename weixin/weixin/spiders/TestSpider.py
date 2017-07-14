# -*- coding: utf-8 -*-
import hashlib
import re

import demjson
import scrapy
from scrapy import Selector

isEnd = False


class WXSpider(scrapy.Spider):
    name = 'test'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    download_delay = 20

    def __init__(self, name=None, **kwargs):
        super(WXSpider, self).__init__(name=None, **kwargs)
        self.count = 0;

    def start_requests(self):
        newUrl = 'http://weixin.sogou.com/antispider/?from=%2fweixin%3Ftype%3d1%26s_from%3dinput%26ie%3dutf8%26_sug_%3dn%26_sug_type_%3d%26query%3dDataBureau'
        yield scrapy.Request(url=newUrl, callback=self.parse)

    def parse(self, response):
        print '您的访问过于频繁' in response.body
