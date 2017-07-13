# -*- coding: utf-8 -*-
import socket
import time

import requests
from mysql.connector import MySQLConnection
import os
import config.configutils as cu


class WxSourceDao(object):
    def __init__(self):
        self.configPath = os.path.join(os.path.dirname(__file__) + "/config/db_config_inner.ini")
        self.dbConfig = cu.read_db_config(self.configPath)
        self.connector = MySQLConnection(charset='utf8', **self.dbConfig)

    '''
        wx_source
        wx源：
            wx_name  名称
            wx_account  账号：唯一标识
            wx_url 对应列表
            wx_avatar 头像
            update_status   状态：last updating updateFail none
            is_enable  是否使能
            update_time 更新时间
    '''
    def queryEnable(self):
        cursor = self.connector.cursor()
        # 可用的 且（ 更新状态为last且时间大于20分钟/ 更新状态为updating且时间大于20分钟/更新状态为updating/更新状态为none）
        sql_query = "select wx_name,wx_account,wx_url,wx_avatar,update_status,is_enable,update_time from wx_source " \
                    "where is_enable='1' and ((update_status='last' and round((UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(" \
                    "update_time))/60)>20) or (update_status='updating' and round((UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(" \
                    "update_time))/60)>20) or update_status='updateFail' or update_status='none') "
        cursor.execute(sql_query)
        results = cursor.fetchall()
        cursor.close()
        return results or []

    def updateStatus(self, wx_account, update_status):
        cursor = self.connector.cursor()
        sql_query = "update wx_source set update_status=%s,update_time=%s where wx_account=%s"
        update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        cursor.execute(sql_query, (update_status, update_time, wx_account))
        cursor.close()
        self.connector.commit()

    def resetUpdating(self):
        """
        重置更新中的的为updateFail，如果出现网络问题，似乎无法回调到而是会一直retry，所以先尝试手动在外部重置
        """
        cursor = self.connector.cursor()
        sql_query = "update wx_source set update_status='updateFail',update_time=%s where update_status='updating'"
        update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        cursor.execute(sql_query, (update_time, ))
        cursor.close()
        self.connector.commit()

    def updateSource(self, wx_account, wx_name, wx_url, update_status):
        cursor = self.connector.cursor()
        sql_query = "update wx_source set wx_name=%s,wx_url=%s,update_status=%s,update_time=%s where " \
                    "wx_account=%s "
        update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        cursor.execute(sql_query, (wx_name, wx_url, update_status, update_time, wx_account))
        cursor.close()
        self.connector.commit()

# import socket
# localIP = socket.gethostbyname(socket.gethostname())#得到本地ip
# print "local ip:%s "%localIP
#
# ipList = socket.gethostbyname_ex(socket.gethostname())
# for i in ipList:
#     if i != localIP:
#        print "external IP:%s"%i
