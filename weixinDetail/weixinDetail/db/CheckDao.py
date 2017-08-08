# -*- coding: utf-8 -*-

from libMe.db.Connector import Connector
from libMe.util import EncryptUtil


class CheckDao(object):
    def __init__(self):
        self.connector = Connector()
        self.hashList = []  # 代表此次已经存在的hash,防止同一时间得到相同文章进行抓取

    def resetHashList(self):
        # 每次重新抓取的时候清除
        self.hashList = []

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
        if results or self.isInHashList(hash_code):
            return True
        else:
            self.hashList.append(hash_code)
            return False

    def isInHashList(self, hash_code):
        return hash_code in self.hashList

    def getHashCode(self, title, wx_account, source_id):
        # 具体逻辑
        return EncryptUtil.md5(title.encode('utf8')+wx_account.encode('utf8')+str(source_id))

    def getAllStyle(self):
        """
        存在逻辑判断
        :return:
        """
        cursor = self.connector.cursor()
        if not cursor:
            return []
        sql_query = 'select id,styles from weixin_detail'
        cursor.execute(sql_query)
        results = cursor.fetchall()
        cursor.close()
        return results or []

    def getHtml(self, pageIndex):
        """
        存在逻辑判断
        :return:
        """
        cursor = self.connector.cursor()
        if not cursor:
            return []
        sql_query = 'select id,content_html from weixin_detail group by id limit %s, %s'
        cursor.execute(sql_query, ((pageIndex-1)*15, 15))
        results = cursor.fetchall()
        cursor.close()
        return results or []

    def updateStyles(self, id, styles):
        cursor = self.connector.cursor()
        if not cursor:
            return
        sql_query = "update weixin_detail set styles=%s where id=%s"
        cursor.execute(sql_query, (styles, id))
        cursor.close()
        self.connector.commit()

    def updateHtml(self, id, content_html):
        cursor = self.connector.cursor()
        if not cursor:
            return
        sql_query = "update weixin_detail set content_html=%s where id=%s"
        cursor.execute(sql_query, (content_html, id))
        cursor.close()
        self.connector.commit()

# checkDao = CheckDao()
# results = checkDao.getAllStyle()
# for result in results:
#     id, styles = result
#     styles = CssUtil.clearBackgroundColor(styles, ['#f3f3f3'])
#     checkDao.updateStyles(id, styles)

# pageIndex = 1
# while True:
#     results = checkDao.getHtml(pageIndex)
#     if not len(results):
#         print 'end'
#         break
#     print 'pageIndex', pageIndex
#     for result in results:
#         id, content_html = result
#         # 处理标签
#         print id
#         selector = Selector(text=content_html)
#         imgAltTitles = selector.xpath('//img/@alt|//img/@title').extract()
#         # 处理提示块img的 alt title, 关注//img/@alt|//img/@title
#         print len(imgAltTitles)
#         for imgAltTitle in imgAltTitles:
#             if imgAltTitle.strip(' '):
#                 print 'here', imgAltTitle
#                 content_html = content_html.replace(imgAltTitle, '')
#         # 更新
#         checkDao.updateHtml(id, content_html)
#     pageIndex += 1



