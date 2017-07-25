# -*- coding: utf-8 -*-

from libMe.db.Connector import Connector
from libMe.util import EncryptUtil


class CheckDao(object):
    def __init__(self):
        self.connector = Connector()

    def checkExist(self, title, wx_account, source_id):
        """
        存在逻辑判断
        source_id : 源ID 微信为1
        :return:
        """
        hash_code = self.getHashCode(title, wx_account, source_id)
        cursor = self.connector.cursor()
        if not cursor:
            return True
        sql_query = 'select id from weixin_detail where hash_code=%s'
        cursor.execute(sql_query, (hash_code,))
        results = cursor.fetchall()
        cursor.close()
        if results:
            return True
        else:
            return False

    def getHashCode(self, title, wx_account, source_id):
        # 具体逻辑
        return EncryptUtil.md5(title.encode('utf8')+wx_account.encode('utf8')+str(source_id))