# -*- coding: utf-8 -*-

import logging

import subprocess

import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from libMe.db.DataMonitorDao import DataMonitorDao

# 为了处理：No handlers could be found for logger “apscheduler.scheduler”
logging.basicConfig()


def heartBeat():
    # 心跳
    dataMonitor = DataMonitorDao()
    dataMonitor.heartBeat('weixin_heartbeat')


def start_spider(spider_name):
    command = "scrapy crawl " + spider_name
    out_bytes = subprocess.check_output(command, shell=True)
    print('end')


def start():
    start_spider('wx_detail')


timeSpace = 10 * 60 * 6 * 3
heartTime = 1 * 60  # 心跳跳动时间间隔
scheduler = BlockingScheduler(daemonic=False)
scheduler.add_job(heartBeat, 'interval', seconds=heartTime)
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
