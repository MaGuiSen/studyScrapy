# -*- coding: utf-8 -*-
import os
import time

from mysql.connector import MySQLConnection

import config.configutils as cu


class LogDao(object):
    def __init__(self, logger, belongTo=''):
        self.configPath = os.path.join(os.path.dirname(__file__) + "/config/db_config_inner.ini")
        self.dbConfig = cu.read_db_config(self.configPath)
        self.connector = MySQLConnection(charset='utf8', **self.dbConfig)
        self.belongTo = belongTo
        self.logger = logger

    '''
    scrapy_log
        id
        info 具体内容
        level 级别：info warn
        save_time 时间
        belong_to 所属模块
        attach 附加信息
    '''
    def queryAll(self):
        cursor = self.connector.cursor()
        sql_query = "select id,info,level,save_time,belong_to,attach from scrapy_log "
        cursor.execute(sql_query)
        results = cursor.fetchall()
        cursor.close()
        return results or []

    def queryPart(self, belong_to):
        cursor = self.connector.cursor()
        sql_query = "select id,info,level,save_time,belong_to,attach from scrapy_log where belong_to=%s"
        cursor.execute(sql_query, (belong_to, ))
        results = cursor.fetchall()
        cursor.close()
        return results or []

    def save(self, info, level, belong_to='', attach=''):
        self.logger.info(belong_to+info)
        cursor = self.connector.cursor()
        sql_query = 'insert into scrapy_log (info,level,save_time,belong_to,attach) values (%s,%s,%s,%s,%s)'
        save_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        cursor.execute(sql_query, (info, level, save_time, belong_to, attach))
        cursor.close()
        self.connector.commit()

    def info(self, info, belong_to='', attach=''):
        belong_to = belong_to if belong_to else self.belongTo
        self.save(info, 'info', belong_to, attach)

    def warn(self, info, belong_to='', attach=''):
        belong_to = belong_to if belong_to else self.belongTo
        self.save(info, 'warn', belong_to, attach)