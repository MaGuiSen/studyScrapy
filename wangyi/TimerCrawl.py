# -*- coding: utf-8 -*-

import logging

import subprocess

import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def start_spider(spider_name):
    command = "scrapy crawl " + spider_name
    out_bytes = subprocess.check_output(command, shell=True)
    print('end')


def start():
    start_spider('wangyi_detail')


timeSpace = 10*60
scheduler = BlockingScheduler(daemonic=False)
# 先马上开始执行
scheduler.add_job(start, 'date')
# 后再抓取之后的某个时间段开始间隔执行
scheduler.add_job(start, 'interval', seconds=timeSpace,
                  start_date=datetime.datetime.now() + datetime.timedelta(seconds=timeSpace))
scheduler.start()



# demo
# def timerr():
#     print 1111
# scheduler = BlockingScheduler(daemonic=False)
# # scheduler.add_job(timerr, 'cron', args=[], hour="20", minute="5", timezone='Asia/Shanghai')
# # scheduler.add_job(timerr, 'cron', args=[], hour="22", minute="0", timezone='Asia/Shanghai')
# # 参考 http://blog.csdn.net/mx472756841/article/details/51751616
# scheduler.add_job(timerr, 'interval', seconds=3)
# scheduler.start()
