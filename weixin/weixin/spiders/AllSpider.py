# -*- coding: utf-8 -*-
import time

import scrapy
from scrapy import Selector

from weixin.db.LogDao import LogDao
from weixin.db.WxSourceDao import WxSourceDao
from weixin.util import NetworkUtil

isEnd = False


class AllSpider(scrapy.Spider):
    name = 'all'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    download_delay = 20  # 基础间隔 0.5*download_delay --- 1.5*download_delays之间的随机数

    def __init__(self, name=None, **kwargs):
        super(AllSpider, self).__init__(name=None, **kwargs)
        self.count = 0
        self.wxSourceDao = WxSourceDao()
        self.request_stop = False
        self.currIp = ''
        self.request_stop_time = 0
        self.logDao = LogDao('wx_source_catch')

    def start_requests(self):
        while True:
            # 检测网络
            if not NetworkUtil.checkNetWork():
                # 20s检测一次
                time.sleep(20)
                self.logDao.warn(u'检测网络不可行')
                continue
            # 检测服务器
            if not NetworkUtil.checkService():
                # 20s检测一次
                time.sleep(20)
                self.logDao.warn(u'检测服务器不可行')
                continue

            if self.request_stop:
                # 拨号生效时间不定，所以需要间隔一段时间再重试
                timeSpace = time.time() - self.request_stop_time
                if timeSpace / 60 <= 2:
                    # 当时间间隔小于 2分钟 就不请求
                    continue
                else:
                    self.request_stop = False

            # 进行爬虫
            # TODO..清除cookie
            # 获取源  可用的，且（是更新失败的，或者最新的同时更新时间跟当前相比大于20分钟）
            sources = self.wxSourceDao.queryEnable()
            for source in sources:
                if self.request_stop:
                    self.logDao.warn(u'出现被绊或者出现网络异常，退出循环')
                    # 当网络出现被绊的情况，就需要停止所有的请求等待IP更换
                    break
                # 更新当前条状态为 更新中，如果更新失败或者被绊则更新为更新失败，更新成功之后设置为成功
                (wx_name, wx_account, wx_url, wx_avatar, update_status, is_enable, update_time) = source
                # print wx_name, wx_account, wx_url, wx_avatar, update_status, is_enable, update_time
                # 更新状态为更新中
                self.wxSourceDao.updateStatus(wx_account, 'updating')
                # 进行页面访问
                url = 'http://weixin.sogou.com/weixin?type=1&s_from=input&ie=utf8&_sug_=n&_sug_type_=&query='
                newUrl = url + wx_account
                self.logDao.warn(u'进行抓取:'+newUrl)
                yield scrapy.Request(url=newUrl,
                                     meta={'url': newUrl, 'wx_account': wx_account, 'source': source},
                                     callback=self.parseList)
            if self.request_stop:
                # 则需要发起通知 进行重新拨号
                # 但是并不知道什么时候网络重新拨号成功呢
                # 记录当前时间
                # 充值updating的状态为updateFail
                self.wxSourceDao.resetUpdating()
                self.logDao.warn(u'更改更新中状态为updateFail,防止下次取不到')
                self.logDao.warn(u'发送重新拨号信号，请等待2分钟会尝试重新抓取')
                self.request_stop_time = time.time()
                pass

    def parseList(self, response):
        source = response.meta['source']
        wx_account = response.meta['wx_account']
        url = response.meta['url']
        body = response.body
        # 判断被禁止 提示需要重启路由 清理cookie
        if '您的访问过于频繁' in body:
            self.request_stop = True
            # 更新状态为更新失败
            self.logDao.warn(u'您的访问过于频繁')
            self.wxSourceDao.updateStatus(wx_account, 'updateFail')
        else:
            # 进行解析，如果解析失败
            selector = Selector(text=response.body)
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
                self.wxSourceDao.updateStatus(wx_account, 'none')
            pass


AllSpider().start_requests()
