# -*- coding: utf-8 -*-
import json
import hashlib
import scrapy
import time
from scrapy import Selector
from ..items import SinaContentItem


class SinaSpider(scrapy.Spider):
    name = 'list'
    download_delay = 2
    '''cateid:
        热点：1z
        产业：1z_22
        创事记：1z_vAZ
        手机：1z_28
        数码：1z_26
        探索：1z_23
        苹果汇：1z_7Wr3
        创业：1z_20

        action:
            1:上滑
            0:第一页
        ctime:上次请求的最后一条
    '''
    def start_requests(self):
        params = {
            'callback': '',
            'cateid': '1z',
            'cre': 'tianyi',
            'mod': 'pctech',
            'merge': '3',
            'statics': '1',
            'length': '15',
            'up': '0',
            'down': '0',
            'fields': 'media%2Cauthor%2Clabels_show%2Ccommentid%2Ccomment_count%2Ctitle%2Curl%2Cinfo%2Cthumbs%2Cthumb%2Cctime%2Creason%2Cvid%2Cimg_count',
            'tm': '1498465995',
            'action': '0',
            'top_id': '1W2E8%2C1W1o4%2C1W0G3%2C1W5cq%2C1W0jK%2C1W2RD%2C1W2FW%2C1W55s%2C1W3VG',
            'offset': '0',
            'ad': '%7B%22rotate_count%22%3A100%2C%22platform%22%3A%22pc%22%2C%22channel%22%3A%22tianyi_pctech%22%2C%22page_url%22%3A%22http%3A%2F%2Ftech.sina.com.cn%2F%22%2C%22timestamp%22%3A1498462406453%7D',
            'ctime': '',
            '_': '1498462406769',
        }
        urls = [
            'http://cre.mix.sina.com.cn/api/v3/get?'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,)

    def parse(self, response):
        a = 1
        print '...............................................'
        print response
        return
