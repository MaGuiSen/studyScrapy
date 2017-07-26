# -*- coding: utf-8 -*-
import os

from mysql.connector import MySQLConnection

import config.configutils as cu


class Connector(object):
    def __init__(self):
        self.configPath = os.path.join(os.path.dirname(__file__) + "/config/db_config_inner.ini")
        config = cu.read_db_config(self.configPath)
        dbConfig = dict({"connection_timeout": 3600}, **config)
        self.connector = MySQLConnection(charset='utf8', **dbConfig)

    def cursor(self):
        if self.connector.is_connected():
            return self.connector.cursor()
        else:
            try:
                self.connector.reconnect(attempts=10, delay=1)
                return self.cursor()
            except Exception:
                return None
        pass

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