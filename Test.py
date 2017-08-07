# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# import logging
# import time
# import datetime
# from apscheduler.schedulers.blocking import BlockingScheduler
# import subprocess
#
# # 为了处理：No handlers could be found for logger “apscheduler.scheduler”
# logger = logging.getLogger('apscheduler.executors.default')
# logger.setLevel(logging.INFO)  # DEBUG
# fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
# h = logging.StreamHandler()
# h.setFormatter(fmt)
# logger.addHandler(h)
#
#
# def heartBeat():
#     # 心跳
#     update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     print 'heatBeat:', update_time
#
#
# def start():
#     update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     print 'start:', update_time
#     currTime = int(time.time())
#     timeArray = time.strptime(str('2017-7-31 12:46:00'), "%Y-%m-%d %H:%M:%S")
#     update_time_long = int(time.mktime(timeArray))
#     if 10 < currTime - update_time_long < 40:
#         raise Exception()
#
# timeSpace = 15
# heartTime = 10  # 心跳跳动时间间隔
# scheduler = BlockingScheduler(daemonic=False)
#
# scheduler.add_job(heartBeat, 'interval', seconds=heartTime)
# # 先马上开始执行
# scheduler.add_job(start, 'date')
# # 后再抓取之后的某个时间段开始间隔执行
# scheduler.add_job(start, 'interval', seconds=timeSpace,
#                   start_date=datetime.datetime.now() + datetime.timedelta(seconds=timeSpace))
# scheduler.start()



# demo
# def timerr():
#     print 1111
# scheduler = BlockingScheduler(daemonic=False)
# # scheduler.add_job(timerr, 'cron', args=[], hour="20", minute="5", timezone='Asia/Shanghai')
# # scheduler.add_job(timerr, 'cron', args=[], hour="22", minute="0", timezone='Asia/Shanghai')
# # 参考 http://blog.csdn.net/mx472756841/article/details/51751616
# scheduler.add_job(timerr, 'interval', seconds=3)
# scheduler.start()
# import datetime
#
# print datetime.datetime.now().hour
# import datetime
#
#
# def checkNeedSend():
#     # 如果在晚上12点到早上6点不爬
#     hour = datetime.datetime.now().hour
#     if 0 <= hour <= 6:
#         return False
# print checkNeedSend()

for index in range(1,30):
    print index