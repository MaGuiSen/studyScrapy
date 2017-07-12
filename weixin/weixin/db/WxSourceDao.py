# -*- coding: utf-8 -*-
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
            status   状态：last updating updateFail
            is_enable  是否使能
            update_time 更新时间
    '''
    def queryEnable(self):
        cursor = self.connector.cursor()
        sql_query = 'select wx_name,wx_account,wx_url, wx_avatar, status, is_enable, update_time from wx_source'
        cursor.execute(sql_query)
        results = cursor.fetchall()
        cursor.close()
        return results or []