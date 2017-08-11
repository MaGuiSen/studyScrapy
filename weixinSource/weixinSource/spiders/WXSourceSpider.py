# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Selector

from ..db.WxSourceDao import WxSourceDao

from libMe.db.LogDao import LogDao
from libMe.util import NetworkUtil
from libMe.util import EncodeUtil
from libMe.util import TimerUtil
from libMe.db.DataMonitorDao import DataMonitorDao


class WXSourceSpider(scrapy.Spider):
    name = 'wx_source'
    download_delay = 20  # 基础间隔 0.5*download_delay --- 1.5*download_delays之间的随机数
    handle_httpstatus_list = [301, 302, 204, 206, 403, 404, 500]  # 可以处理重定向及其他错误码导致的 页面无法获取解析的问题

    def __init__(self, name=None, **kwargs):
        super(WXSourceSpider, self).__init__(name=None, **kwargs)
        self.count = 0
        self.wxSourceDao = WxSourceDao()
        self.currIp = ''
        self.logDao = LogDao(self.logger, 'weixin_source_catch')
        self.dataMonitor = DataMonitorDao()

    def close(spider, reason):
        spider.saveStatus('stop')
        spider.dataMonitor.updateTotal('weixin_source_total')

    def start_requests(self):
        # 如果正在爬，就不请求
        status = self.getStatus()
        if status == 'running':
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

        # 进行爬虫
        # 获取源  可用的，且（是更新失败的，或者最新的同时更新时间跟当前相比大于40分钟）
        sources = self.wxSourceDao.queryEnable(isRandom=True)

        for source in sources:
            # 更新当前条状态为 更新中，如果更新失败或者被绊则更新为更新失败，更新成功之后设置为成功
            (wx_name, wx_account, wx_url, wx_avatar, update_status, is_enable, update_time) = source
            # 更新状态为更新中
            self.wxSourceDao.updateStatus(wx_account, 'updating')
            # 进行页面访问
            url = 'http://weixin.sogou.com/weixin?type=1&s_from=input&ie=utf8&_sug_=n&_sug_type_=&query='
            newUrl = url + wx_account
            self.logDao.warn(u'进行抓取:' + newUrl)
            yield scrapy.Request(url=newUrl,
                                 meta={'request_type': 'weixin_source', 'url': newUrl,
                                       'wx_account': wx_account, 'source': source},
                                 callback=self.parseList, dont_filter=True)

    def parseList(self, response):
        source = response.meta['source']
        wx_account = response.meta['wx_account']
        url = response.meta['url']
        body = EncodeUtil.toUnicode(response.body)
        # 判断被禁止 提示需要重启路由 清理cookie
        if response.status == 302:
            # 更新状态为更新失败
            self.logDao.warn(u'您的访问过于频繁,重新拨号')
            self.wxSourceDao.updateStatus(wx_account, 'updateFail')
            # 获取Ip # 同时空线程30s
            NetworkUtil.getNewIp()
            TimerUtil.sleep(30)
        else:
            self.logDao.info(u'开始解析:' + wx_account)
            # 进行解析
            selector = Selector(text=body)
            results = selector.xpath('//*[@id="main"]/div[4]/ul/li')
            self.logDao.info(u'列表长度:' + str(len(results)))
            hasCatch = False
            for result in results:
                wx_name = result.xpath('//*[@id="sogou_vr_11002301_box_0"]/div/div[2]/p[1]/a/text()').extract_first()
                wx_account_ = result.xpath('//p[@class="info"]/label/text()').extract_first()
                wx_url = result.xpath('//p[@class="tit"]/a/@href').extract_first()
                if wx_account_ == wx_account:
                    self.logDao.info(u'成功抓取:' + wx_account_)
                    self.wxSourceDao.updateSource(wx_account, wx_name, wx_url, 'last')
                    hasCatch = True
                    break
            if not hasCatch:
                self.logDao.info(u'没有抓到:' + wx_account_)
                self.wxSourceDao.updateStatus(wx_account, 'none')
            pass

    def getStatus(self):
        try:
            with open("catchStatus.json", 'r') as load_f:
                aa = json.load(load_f)
                return aa.get('status')
        finally:
            if load_f:
                load_f.close()

    def saveStatus(self, status):
        try:
            with open("catchStatus.json", "w") as f:
                json.dump({'status': status}, f)
        finally:
            if f:
                f.close()
