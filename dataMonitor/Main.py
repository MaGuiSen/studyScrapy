# -*- coding: utf-8 -*-


import logging
import time

import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from libMe.db.DataMonitorDao import DataMonitorDao

dataMonitor = DataMonitorDao()

# 参考网站：http://www.cnblogs.com/xcblogs-python/p/5727238.html
import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'maguisen@163.com'  # 发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user = '1059876295@qq.com'  # 收件人邮箱账号，为了后面易于维护，所以写成了变量


def mail(info):
    ret = True
    try:
        msg = MIMEText(info, 'plain', 'utf-8')
        msg['From'] = formataddr(["maguisen", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["我的天", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "心跳出问题"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, "Ma123456")  # 括号中对应的是发件人邮箱账号、邮箱密码（授权码）
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 这句是关闭连接的意思
    except Exception as e:  # 如果try中的语句没有执行，则会执行下面的ret=False
        ret = False
        print e
    return ret
# if ret:
#     print("ok")  # 如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
# else:
#     print("filed")  # 如果发送失败则会返回filed

# 为了处理：No handlers could be found for logger “apscheduler.scheduler”
logger = logging.getLogger('apscheduler.executors.default')
logger.setLevel(logging.INFO)  # DEBUG
fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
logger.addHandler(h)

lastSendTime = int(time.time())


def checkNeedSend():
    currTime = int(time.time())
    global lastSendTime
    if currTime - lastSendTime > 10 * 60:
        return True
    else:
        return False


def outOfData(update_time_long):
    currTime = int(time.time())
    if currTime - update_time_long > 3 * 60:
        return True
    else:
        return False


def heartBeat():
    # 心跳
    results = dataMonitor.getAllHeartBeatTime(cursor_out=None)
    print 'check....'
    needSendTypes = []
    for result in results:
        (type, update_time) = result
        timeArray = time.strptime(str(update_time), "%Y-%m-%d %H:%M:%S")
        update_time_long = int(time.mktime(timeArray))
        print update_time
        if outOfData(update_time_long):
            print 'outOfData'
            print update_time
            needSendTypes.append(type)

    if len(needSendTypes) and checkNeedSend():
        print 'need send email'
        ret = mail(','.join(needSendTypes))
        if ret:
            print 'send_success'
            global lastSendTime
            lastSendTime = int(time.time())


heartTime = 3*60   # 心跳跳动时间间隔 3分钟
scheduler = BlockingScheduler(daemonic=False)
scheduler.add_job(heartBeat, 'interval', seconds=heartTime,
                  start_date=datetime.datetime.now() + datetime.timedelta(seconds=5))
scheduler.start()

