# -*- coding: utf-8 -*-

import os

from mysql.connector import MySQLConnection

import config.configutils as cu
from libMe.util import EncryptUtil
from libMe.db.Connector import Connector

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


    def getAllHtml(self):
        """
        存在逻辑判断
        :return:
        """
        cursor = self.connector.cursor()
        if not cursor:
            return []
        sql_query = 'select id,styles,content_html from sina_detail'
        cursor.execute(sql_query)
        results = cursor.fetchall()
        cursor.close()
        return results or []

    def update(self, id, styles, content_html):
        cursor = self.connector.cursor()
        if not cursor:
            return
        sql_query = "update sina_detail set content_html=%s,styles=%s where id=%s"
        cursor.execute(sql_query, (content_html,styles, id))
        cursor.close()
        self.connector.commit()

# checkDao = CheckDao()
# results = checkDao.getAllHtml()
# outHtml = """<div class="content_wrappr_left"><div class="content">${++content++}</div></div>"""
# for result in results:
#     id, styles, content_html = result
#     print id
#     newStyle = styles.replace('overflow-x:hidden', '').replace('overflow:hidden', '')
#     newHtml = content_html
#     if not content_html.startswith('<div class="content_wrappr_left">'):
#         newHtml = outHtml.replace('${++content++}', content_html)
#     checkDao.update(id, newStyle, newHtml)
