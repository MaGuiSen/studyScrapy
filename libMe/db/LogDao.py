# -*- coding: utf-8 -*-
import time

from libMe.db.Connector import Connector


class LogDao(object):
    def __init__(self, logger, belongTo=''):
        self.connector = Connector()
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
        if not cursor:
            return []
        sql_query = "select id,info,level,save_time,belong_to,attach from scrapy_log "
        cursor.execute(sql_query)
        results = cursor.fetchall()
        cursor.close()
        return results or []

    def queryPart(self, belong_to):
        cursor = self.connector.cursor()
        if not cursor:
            return []
        sql_query = "select id,info,level,save_time,belong_to,attach from scrapy_log where belong_to=%s"
        cursor.execute(sql_query, (belong_to, ))
        results = cursor.fetchall()
        cursor.close()
        return results or []

    def save(self, info, level, belong_to='', attach=''):
        self.logger.info(belong_to + info)
        if True:
            return
        cursor = self.connector.cursor()
        if not cursor:
            return
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