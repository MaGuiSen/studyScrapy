# -*- coding: utf-8 -*-
import random
import time

from libMe.db.Connector import Connector


class WxSourceDao(object):
    def __init__(self):
        self.connector = Connector()
        self.orderType = 'desc'  # 用于判断是升序还是降序

    def queryEnable(self, isRandom=False):
        cursor = self.connector.cursor()
        if not cursor:
            return []
        if self.orderType == "desc":
            self.orderType = "asc"
        else:
            self.orderType = "desc"
        # """
        #     select wx_name,wx_account,wx_url,wx_avatar,update_status,is_enable,update_time from weixin_source
        #     where is_enable='1'
        #     and
        #     (
        #         (update_status='last' and round((UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(update_time))/60)>20)
        #         or
        #         (update_status='updating' and round((UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(update_time))/60)>20)
        #         or update_status='updateFail'
        #         or update_status='none'
        #     )
        #     order by id
        # """
        # 可用的 且（ 更新状态为last且时间大于20分钟/ 更新状态为updating且时间大于20分钟/更新状态为updating/更新状态为none）
        sql_query = "select id,wx_name,wx_account,wx_url,wx_avatar,update_status,is_enable,update_time from weixin_source " \
                    "where is_enable='1' and ((update_status='last' and round((UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(" \
                    "update_time))/60)>40) or (update_status='updating' and round((UNIX_TIMESTAMP(NOW())-UNIX_TIMESTAMP(" \
                    "update_time))/60)>40) or update_status='updateFail' or update_status='none') order by id "+self.orderType
        cursor.execute(sql_query)
        results = cursor.fetchall()
        cursor.close()
        results = results or []
        # print "sources长度", len(results)
        if isRandom and results:
            # 随机排序 防止出现都是请求同一个
            random.shuffle(results)
        return results

    def queryWxUrl(self, isRandom=False):
        """
        获取wxUrl有值，且是有效的
        :return:
        """
        cursor = self.connector.cursor()
        if not cursor:
            return []

        if self.orderType == "desc":
            self.orderType = "asc"
        else:
            self.orderType = "desc"
        sql_query = "select id,wx_name,wx_account,wx_url,wx_avatar,update_status,is_enable,update_time from weixin_source " \
                    "where is_enable='1' and wx_url !='' order by id " + self.orderType
        cursor.execute(sql_query)
        results = cursor.fetchall()
        cursor.close()
        results = results or []
        if isRandom and results:
            # 随机排序 防止出现都是请求同一个
            random.shuffle(results)
        return results

    def updateStatus(self, wx_account, update_status):
        cursor = self.connector.cursor()
        if not cursor:
            return
        sql_query = "update weixin_source set update_status=%s,update_time=%s where wx_account=%s"
        update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        cursor.execute(sql_query, (update_status, update_time, wx_account))
        cursor.close()
        self.connector.commit()

    def resetUpdating(self):
        """
        重置更新中的的为updateFail，如果出现网络问题，似乎无法回调到而是会一直retry，所以先尝试手动在外部重置
        """
        cursor = self.connector.cursor()
        if not cursor:
            return
        sql_query = "update weixin_source set update_status='updateFail',update_time=%s where update_status='updating'"
        update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        cursor.execute(sql_query, (update_time,))
        cursor.close()
        self.connector.commit()

    def updateSource(self, wx_account, wx_name, wx_url, update_status):
        cursor = self.connector.cursor()
        if not cursor:
            return
        sql_query = "update weixin_source set wx_name=%s,wx_url=%s,update_status=%s,update_time=%s where " \
                    "wx_account=%s "
        update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        cursor.execute(sql_query, (wx_name, wx_url, update_status, update_time, wx_account))
        cursor.close()
        self.connector.commit()


