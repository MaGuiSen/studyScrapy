# -*- coding: utf-8 -*-

import os

from mysql.connector import MySQLConnection

import config.configutils as cu
from libMe.util import EncryptUtil


class CheckDao(object):
    def __init__(self):
        self.configPath = os.path.join(os.path.dirname(__file__) + "/config/db_config_inner.ini")
        self.dbConfig = cu.read_db_config(self.configPath)
        self.connector = MySQLConnection(charset='utf8', **self.dbConfig)

    def checkExist(self, source_url):
        """
        存在逻辑判断
        :return:
        """
        hash_code = self.getHashCode(source_url)
        cursor = self.connector.cursor()
        sql_query = 'select id from sina_detail where hash_code=%s'
        cursor.execute(sql_query, (hash_code,))
        results = cursor.fetchall()
        cursor.close()
        if results:
            return True
        else:
            return False

    def getHashCode(self, source_url):
        # 具体逻辑
        return EncryptUtil.md5(source_url)