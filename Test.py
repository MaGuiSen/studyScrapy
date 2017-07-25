# # -*- coding: utf-8 -*-
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def tt():
    print 1

def tt2():
    print 2

scheduler = BlockingScheduler(daemonic=False)
# 先马上开始执行
scheduler.add_job(tt, 'date')
# 后再抓取之后的某个时间段开始间隔执行
scheduler.add_job(tt2, 'interval', seconds=100,
                  start_date=datetime.datetime.now() + datetime.timedelta(seconds=2))
scheduler.start()