# -*- coding: utf-8 -*-

from libMe.db.Connector import Connector
from libMe.util import EncryptUtil


class CheckDao(object):
    def __init__(self):
        self.connector = Connector()

    def checkExist(self, source_url):
        """
        存在逻辑判断
        :return:
        """
        hash_code = self.getHashCode(source_url)
        cursor = self.connector.cursor()
        if not cursor:
            return True
        sql_query = 'select id from wangyi_detail where hash_code=%s'
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