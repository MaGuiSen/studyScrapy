# -*- coding: utf-8 -*-
import time

from libMe.db.Connector import Connector
from libMe.util import EncryptUtil


class CheckDao(object):
    def __init__(self):
        self.connector = Connector(isLocalDB=False)
        self.hashList = []  # 代表此次已经存在的hash,防止同一时间得到相同文章进行抓取

    def resetHashList(self):
        # 每次重新抓取的时候清除
        self.hashList = []
    def checkExist(self, source_url):
        """
        存在逻辑判断
        :return:
        """
        hash_code = self.getHashCode(source_url)
        cursor = self.connector.cursor()
        if not cursor:
            return True
        sql_query = 'select id from jiemian_detail where hash_code=%s'
        cursor.execute(sql_query, (hash_code,))
        results = cursor.fetchall()
        cursor.close()
        if results or self.isInHashList(hash_code):
            return True
        else:
            return False

    def isInHashList(self, hash_code):
        return hash_code in self.hashList

    def getHashCode(self, source_url):
        # 具体逻辑
        return EncryptUtil.md5(source_url)

    def getHtml(self, pageIndex):
        """
        获取所有html逻辑
        :return:
        """
        cursor = self.connector.cursor()
        if not cursor:
            return []
        sql_query = 'select id,content_html from jiemian_detail group by id limit %s, %s'
        cursor.execute(sql_query, ((pageIndex - 1) * 15, 15))
        results = cursor.fetchall()
        cursor.close()
        return results or []

    def getPostTime(self, pageIndex):
        """
        时间逻辑
        :return:
        """
        cursor = self.connector.cursor()
        if not cursor:
            return []
        sql_query = 'select id,post_date from jiemian_detail group by id limit %s, %s'
        cursor.execute(sql_query, ((pageIndex - 1) * 15, 15))
        results = cursor.fetchall()
        cursor.close()
        return results or []

    def updatePostTime(self, id, post_date):
        cursor = self.connector.cursor()
        if not cursor:
            return
        sql_query = "update jiemian_detail set post_date=%s where id=%s"
        cursor.execute(sql_query, (post_date, id))
        cursor.close()
        self.connector.commit()

    def updateStyles(self, id, styles):
        cursor = self.connector.cursor()
        if not cursor:
            return
        sql_query = "update jiemian_detail set styles=%s where id=%s"
        cursor.execute(sql_query, (styles, id))
        cursor.close()
        self.connector.commit()

    def updateHtml(self, id, content_html):
        cursor = self.connector.cursor()
        if not cursor:
            return
        sql_query = "update jiemian_detail set content_html=%s where id=%s"
        cursor.execute(sql_query, (content_html, id))
        cursor.close()
        self.connector.commit()

# checkDao = CheckDao()
# pageIndex = 1
# while True:
#     results = checkDao.getPostTime(pageIndex)
#     if not len(results):
#         print 'end'
#         break
#     print 'pageIndex', pageIndex
#     for result in results:
#         id, post_date = result
#         print 'in: ', id, post_date
#         # post_date = post_date.replace(u'\xa0', u' ')
#         # 处理标签
#         try:
#             # post_date = time.strptime(post_date, "%Y-%m-%d %H:%M:%S")  # time.strftime("%Y-%m-%d %H:%M:%S", )
#             timeArray = time.strptime(str(post_date), "%Y-%m-%d %H:%M:%S")
#             update_time_long = int(time.mktime(timeArray))
#         except Exception as e:
#             print u'出错..........................................................................'
#             pass
#         print 'out: ', id, update_time_long
#         x = time.localtime(update_time_long)
#         print 'out: ', id, time.strftime('%Y-%m-%d %H:%M:%S', x)
#         # checkDao.updatePostTime(id, post_date)
#     pageIndex += 1