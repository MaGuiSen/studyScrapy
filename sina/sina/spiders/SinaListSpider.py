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

    def start_requests(self):
        # params = '''
        #         callback=jQuery111202870494215627517_1498024592835&
        #         cateid=1z&
        #         cre=tianyi&
        #         mod=pctech&
        #         merge=3&
        #         statics=1&
        #         length=15&
        #         up=1&
        #         down=0&
        #         fields=media, author, labels_show, commentid, comment_count, title, url, info, thumbs, thumb, ctime, reason, vid, img_count,
        #         tm=int(time.time())&
        #         action=1&
        #         top_id=1Tbiz, 1Te8L, 1Tdwo, 1Teft, 1TeGe, 1TYCd, 1TXKW, 1Tbpa,
        #         offset=0&
        #         ad=json.dumps({"rotate_count": 100, "platform": "pc", "channel": "tianyi_pctech", "page_url": "http://tech.sina.com.cn/",
        #                "timestamp": 1498024592929})&
        #         ctime=int(time.time())&
        #         _'=1498024592845&
        #     '''
        # # params = params.replace('int(time.time())', str(int(time.time()))).replace('1498024592929', str(1498024592929)).replace('time.time()', str(time.time()))
        # # params.replace('')
        urls = [
            'http://tech.sina.com.cn/t/2017-06-19/doc-ifyhfnqa4438329.shtml?cre=tianyi&mod=pctech&loc=7&r=0&doct=0&rfunc=13&tj=none&s=0&tr=1',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies={'SUB': '_2AkMuFoMaf8NxqwJRmP0RyWrhaoh1yw7EieKYSnLBJRMyHRl-yD83qnUntRCe5Jvl9dNMpdUed35Y7eiXZcRQZA..',
                                                                       'SUBP': '0033WrSXqPxfM72-Ws9jqgMF55529P9D9Wh5_ALReIU66h.RlIImdams'})

    def parse(self, response):
        a = 1
        print '...............................................'
        print response
        return