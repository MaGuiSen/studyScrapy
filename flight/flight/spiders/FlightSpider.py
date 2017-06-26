# -*- coding: utf-8 -*-
import json
import hashlib
import os

import scrapy
import time
from scrapy import Selector
import datetime
# from flight.flight.Log import Log

# Landed  ： Delayed / On-time / 空
# Scheduled ： Delayed / 空
# Unknown：  空
# Cancelled： 空
# En Route: 在航行中
# ArrivalGate
Landed = {
    'total': 0,
    'ScheduledDeparture': 0,
    'ScheduledArrival': 0,
    'ActualDeparture': 0,
    'ActualArrival': 0,
    'ArrivalTerminal': 0,
    'BaggageClaim': 0,
    'DepartureTerminal': 0,
    'DepartureGate': 0,
    'EstimatedGateArrival': 0,
    'EstimatedGateDeparture': 0,
    'ArrivalGate':0,
    'EstimatedArrival':0,
    'EstimatedDeparture': 0,
}
Scheduled = {
    'total': 0,
    'ScheduledDeparture': 0,
    'ScheduledArrival': 0,
    'ActualDeparture': 0,
    'ActualArrival': 0,
    'ArrivalTerminal': 0,
    'BaggageClaim': 0,
    'DepartureTerminal': 0,
    'DepartureGate': 0,
    'EstimatedGateArrival': 0,
    'EstimatedGateDeparture': 0,
    'ArrivalGate': 0,
    'EstimatedArrival': 0,
    'EstimatedDeparture': 0,
}
Unknown = {
    'total': 0,
    'ScheduledDeparture': 0,
    'ScheduledArrival': 0,
    'ActualDeparture': 0,
    'ActualArrival': 0,
    'ArrivalTerminal': 0,
    'BaggageClaim': 0,
    'DepartureTerminal': 0,
    'DepartureGate': 0,
    'EstimatedGateArrival': 0,
    'EstimatedGateDeparture': 0,
    'ArrivalGate': 0,
    'EstimatedArrival': 0,
    'EstimatedDeparture': 0,
}
EnRoute = {
    'total': 0,
    'ScheduledDeparture': 0,
    'ScheduledArrival': 0,
    'ActualDeparture': 0,
    'ActualArrival': 0,
    'ArrivalTerminal': 0,
    'BaggageClaim': 0,
    'DepartureTerminal': 0,
    'DepartureGate': 0,
    'EstimatedGateArrival': 0,
    'EstimatedGateDeparture': 0,
    'ArrivalGate': 0,
    'EstimatedArrival': 0,
    'EstimatedDeparture': 0,
}
Cancelled = {
    'total': 0,
    'ScheduledDeparture': 0,
    'ScheduledArrival': 0,
    'ActualDeparture': 0,
    'ActualArrival': 0,
    'ArrivalTerminal': 0,
    'BaggageClaim': 0,
    'DepartureTerminal': 0,
    'DepartureGate': 0,
    'EstimatedGateArrival': 0,
    'EstimatedGateDeparture': 0,
    'ArrivalGate': 0,
    'EstimatedArrival': 0,
    'EstimatedDeparture': 0,
}


class FlightSpider(scrapy.Spider):
    name = 'flight'
    download_delay = 2
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    headers = {'User-Agent': user_agent}

    def start_requests(self):
        # 还差到达和出发的区分airportQueryType ： 0  出发   1 到达
        url = 'http://www.flightstats.com/go/FlightStatus/flightStatusByAirport.do'
        currDate = datetime.datetime.now()
        while True:
            currTime = 0
            while True:
                formDate = {
                    'airportQueryTime': str(currTime),
                    'airportQueryType': '0',
                    'queryNext': 'false',
                    'queryPrevious': 'false',
                    'sortField': '3',
                    'airport': '(HKG) Hong Kong International Airport',
                    'airportQueryDate': currDate.strftime('%Y-%m-%d'),
                    'codeshareDisplay': '1',
                    'airportToFilter': '',
                    'airlineToFilter': ''
                }
                yield scrapy.FormRequest(url=url, formdata=formDate, meta={'currDate': currDate, 'currTime': currTime},
                                         callback=self.parse)
                currTime += 1
                print '循环当前时间', currTime
                if currTime > 23:
                    break
                time.sleep(1)
            currDate = currDate - datetime.timedelta(days=1)
            print '循环当前日期', currDate.strftime('%Y-%m-%d')

    # def start_requests(self):
    #     # 还差到达和出发的区分airportQueryType ： 0  出发   1 到达
    #         url = 'http://www.flightstats.com/go/FlightStatus/flightStatusByAirport.do'
    #         currDate = datetime.datetime.now()
    #         currTime = 0  # 0 -- 23
    #     #     # while True:
    #     #     nextDate = currDate - datetime.timedelta(days=1)
    #     #     formDate = {
    #     #         'airportQueryTime': '19',
    #     #         'airportQueryType': '0',
    #     #         'queryNext': 'false',
    #     #         'queryPrevious': 'false',
    #     #         'sortField': '3',
    #     #         'airport': '(HKG) Hong Kong International Airport',
    #     #         'airportQueryDate': nextDate.strftime('%Y-%m-%d'),
    #     #         'codeshareDisplay': '1',
    #     #         'airportToFilter': '',
    #     #         'airlineToFilter': ''
    #     #     }
    #     #     yield scrapy.FormRequest(url=url, meta={'currDate': currDate, 'currTime': currTime}, formdata=formDate, callback=self.parse)
    #     #     time.sleep(1)
    #     #     currDate = nextDate
    #         # 0 -- 23
    #         while True:
    #             currTime = 0
    #             while True:
    #                 formDate = {
    #                     'airportQueryTime': str(currTime),
    #                     'airportQueryType': '0',
    #                     'queryNext': 'false',
    #                     'queryPrevious': 'false',
    #                     'sortField': '3',
    #                     'airport': '(HKG) Hong Kong International Airport',
    #                     'airportQueryDate': currDate.strftime('%Y-%m-%d'),
    #                     'codeshareDisplay': '1',
    #                     'airportToFilter': '',
    #                     'airlineToFilter': ''
    #                 }
    #                 yield scrapy.FormRequest(url=url, formdata=formDate,meta={'currDate': currDate, 'currTime': currTime},  callback=self.parse)
    #                 currTime += 1
    #                 if currTime > 23:
    #                     break
    #                 time.sleep(1)
    #         currDate = currDate - datetime.timedelta(days=1)

    def parse(self, response):
        currDate = response.meta['currDate']
        currTime = response.meta['currTime']
        selector = Selector(text=response.body)
        trs = selector.xpath('//table[@class="flightStatusByAirportListingTable"]/tr')

        if len(trs) > 1:
            print currDate.strftime('%Y-%m-%d'), currTime, '有值列表长度为：', len(trs) - 1
        else:
            print currDate.strftime('%Y-%m-%d'), currTime, '无值'

        if len(trs) > 1:
            index = -1
            for tr in trs:
                index += 1
                if index == 0:
                    continue
                detailPageUrl = tr.xpath('td/a/@href').extract_first()
                detailPageUrl = 'http://www.flightstats.com' + detailPageUrl
                status = tr.xpath('td[5]/a/div/text()').extract_first()
                print '当前飞机状态:', status
                yield scrapy.Request(url=detailPageUrl, meta={'detailPageUrl': detailPageUrl, 'currDate': currDate, 'currTime': currTime, 'status': status},
                                     callback=self.parseDetail)
                # url = 'http://www.flightstats.com/go/FlightStatus/flightStatusByFlight.do?id=912158714&airline=AF&flightNumber=185&departureDate=2017-06-23'
                # yield scrapy.Request(url=url, callback=self.parseDetail)

    def parseDetail(self, response):
        detailPageUrl = response.meta['detailPageUrl']
        currDate = response.meta['currDate']
        currTime = response.meta['currTime']
        flightStatus = response.meta['status']
        print '当前状态：', flightStatus
        print '当前url:',detailPageUrl
        print '当前时间日期：', currDate.strftime('%Y-%m-%d'), currTime
        selector = Selector(text=response.body)
        flightName = selector.xpath('//*[@id="mainAreaLeftColumn"]/div[1]/h2/text()').extract()
        status = selector.xpath('//*[@id="mainAreaLeftColumn"]/div[1]/div/div[3]/div[2]/text()').extract()
        updateTime = selector.xpath('//*[@id="mainAreaLeftColumn"]/div[1]/div/div[3]/div[3]/text()').extract()
        motes = selector.xpath('//*[@id="mainAreaLeftColumn"]/div[1]/div/div[4]').extract()
        statusTable = selector.xpath('//table[@class="statusDetailsTable"]/tbody/tr').extract()
        statusTrs = selector.xpath('//table[@class="statusDetailsTable"]/tr').extract()
        index = -1
        hasKeyTr = False  # 表示已经有行经过了
        keyLeft = ''
        keyRight = ''
        valueLeft = ''
        valueRight = ''
        # 计算个数
        global Landed, Scheduled, Unknown, Cancelled, EnRoute
        if 'Landed' in flightStatus:
            Landed['total'] += 1
        elif 'Scheduled' in flightStatus:
            Scheduled['total'] += 1
        elif 'Unknown' in flightStatus:
            Unknown['total'] += 1
        elif 'Cancelled' in flightStatus:
            Cancelled['total'] += 1
        elif 'En Route' in flightStatus:
            EnRoute['total'] += 1

        for tr in statusTrs:
            index += 1
            if index == 0:
                continue
            selector = Selector(text=tr)
            tds = selector.xpath('//td/text()').extract() or []
            length = len(tds)
            if index % 2:
                # 奇数行 代表标题
                hasKeyTr = True
                if length == 1:
                    keyLeft = tds[0]
                    keyRight = ''
                elif length == 2:
                    keyLeft = tds[0]
                    keyRight = tds[1]
                else:
                    keyLeft = ''
                    keyRight = ''
                # 重置value
                valueLeft = ''
                valueRight = ''
            else:
                # 偶数行 代表值
                hasKeyTr = False
                if length == 1:
                    valueLeft = tds[0]
                    valueRight = ''
                elif length == 2:
                    valueLeft = tds[0]
                    valueRight = tds[1]
                else:
                    valueLeft = ''
                    valueRight = ''
                # 此处说明已经取到key 和 Value
                keyLeft = keyLeft.strip().replace('\n', u' ').replace(' ', '').strip(':')
                keyRight = keyRight.strip().replace('\n', u' ').replace(' ', '').strip(':')
                valueLeft = valueLeft.strip().replace('\n', u' ').replace(' ', '')
                valueRight = valueRight.strip().replace('\n', u' ').replace(' ', '')
                print keyLeft, valueLeft, keyRight, valueRight
                # 计算个数
                if 'Landed' in flightStatus:
                    self.addKeyValueNum(Landed, keyLeft, valueLeft)
                    self.addKeyValueNum(Landed, keyRight, valueLeft)
                elif 'Scheduled' in flightStatus:
                    self.addKeyValueNum(Scheduled, keyLeft, valueLeft)
                    self.addKeyValueNum(Scheduled, keyRight, valueLeft)
                elif 'Unknown' in flightStatus:
                    self.addKeyValueNum(Unknown, keyLeft, valueLeft)
                    self.addKeyValueNum(Unknown, keyRight, valueLeft)
                elif 'Cancelled' in flightStatus:
                    self.addKeyValueNum(Cancelled, keyLeft, valueLeft)
                    self.addKeyValueNum(Cancelled, keyRight, valueLeft)
                elif 'En Route' in flightStatus:
                    self.addKeyValueNum(EnRoute, keyLeft, valueLeft)
                    self.addKeyValueNum(EnRoute, keyRight, valueLeft)
                keyLeft = ''
                keyRight = ''
        print 'Landed:', Landed
        print 'Scheduled:', Scheduled
        print 'Unknown:', Unknown
        print 'Cancelled:', Cancelled
        print 'EnRoute:', EnRoute
        all = {
            'Landed': Landed,
            'Scheduled': Scheduled,
            'Unknown': Unknown,
            'Cancelled': Cancelled,
            'EnRoute': EnRoute,
        }
        try:
            with open("total.json", 'wb') as f:
                timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                f.write(json.dumps(dict({'time': timeStr}, **all)))
        except Exception,e:
            print e.message

    def addKeyValueNum(self, currObj, key, value):
        if key and value and value != 'N/A':
            currObj[key] += 1



