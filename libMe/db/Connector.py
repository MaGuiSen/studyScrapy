# -*- coding: utf-8 -*-
import os

import time
from mysql.connector import MySQLConnection

import config.configutils as cu


class Connector(object):
    def __init__(self):
        self.configPath = os.path.join(os.path.dirname(__file__) + "/config/db_config_inner.ini")
        config = cu.read_db_config(self.configPath)
        self.dbConfig = dict({"connection_timeout": 3600}, **config)
        self.connector = None
        self.getConnector()

    def getConnector(self, attempts=10, delay=4):
        if self.connector:
            return self.connector
        counter = 0
        while counter != attempts:
            counter += 1
            try:
                self.connector = MySQLConnection(charset='utf8mb4', **self.dbConfig)
                break
            except Exception as err:
                if counter == attempts:
                    break
            if delay > 0:
                time.sleep(delay)
        return self.connector

    def cursor(self):
        if not self.getConnector():
            # 如果不存在 则代表没有连接成功（尝试了10次之后还没传成功，就代表此次不进行操作)
            return None
        if self.connector.is_connected():
            return self.connector.cursor()
        else:
            try:
                self.connector.reconnect(attempts=10, delay=1)
                return self.cursor()
            except Exception:
                return None

    def commit(self):
        if self.connector:
            if self.connector.is_connected():
                self.connector.commit()
            else:
                try:
                    self.connector.reconnect(attempts=10, delay=1)
                    self.commit()
                except Exception:
                    pass