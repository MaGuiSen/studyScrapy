# -*- coding: utf-8 -*-

import scrapy
import thread

import time

from weixin.db.WxSourceDao import WxSourceDao
from weixin.util import NetworkUtil

isEnd = False


class AllSpider(scrapy.Spider):
    name = 'all'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    download_delay = 20

    def __init__(self, name=None, **kwargs):
        super(AllSpider, self).__init__(name=None, **kwargs)
        self.count = 0
        self.wxSourceDao = WxSourceDao()
        self.request_stop = False

    def start_requests(self):
        while True:
            # 检测网络
            if not NetworkUtil.checkNetWork():
                time.sleep(5)
                continue
            # 检测服务器
            if not NetworkUtil.checkService():
                time.sleep(5)
                continue
            # 进行爬虫
            # TODO..清除cookie
            # 获取源
            sources = self.wxSourceDao.queryEnable()
            if not sources:
                time.sleep(5)
                continue
            index = 0
            while index >= len(sources):
                if self.request_stop:
                    # 当网络出现被绊的情况，就需要停止所有的请求等待IP更换
                    continue
                source = sources[index]




