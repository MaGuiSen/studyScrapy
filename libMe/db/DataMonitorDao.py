# -*- coding: utf-8 -*-
import time

from libMe.db.Connector import Connector


class DataMonitorDao(object):
    def __init__(self):
        self.connector = Connector()

    def getAllHeartBeatTime(self,cursor_out=None):
        """
                :param cursor_out:
                :param types:
                    sina_heartbeat
                    tengxun_heartbeat
                    wangyi_heartbeat
                    weixin_heartbeat
                    weixin_source_heartbeat
                :return:
                得到心跳更新时间
                """
        if not cursor_out:
            cursor = self.connector.cursor()
            if not cursor:
                return
        else:
            cursor = cursor_out

        typeStr = " where type in ('sina_heartbeat','tengxun_heartbeat','wangyi_heartbeat','weixin_heartbeat','weixin_source_heartbeat')"

        sql_query = "select type, update_time from data_monitor " + typeStr
        try:
            cursor.execute(sql_query)
        except Exception as e:
            print e.msg
        results = cursor.fetchall()
        if not cursor_out:
            cursor.close()
            self.connector.close()
        return results or []

    def heartBeat(self, type=''):
        """
        :param type:
            sina_heartbeat
            tengxun_heartbeat
            wangyi_heartbeat
            weixin_heartbeat
            weixin_source_heartbeat
        :return:
        更新跳动时间
        """
        if not type:
            return
        cursor = self.connector.cursor()
        if not cursor:
            return
        info = u'跳动中'
        remark = ''
        if type == 'sina_heartbeat':
            remark = u'新浪_心跳1分钟更新一次'
        elif type == 'tengxun_heartbeat':
            remark = u'腾讯_心跳1分钟更新一次'
        elif type == 'wangyi_heartbeat':
            remark = u'网易_心跳1分钟更新一次'
        elif type == 'weixin_heartbeat':
            remark = u'微信_心跳1分钟更新一次'
        elif type == 'weixin_source_heartbeat':
            remark = u'微信源_心跳1分钟更新一次'
        # 检测是否存在type ,  update_time ,  info , remark, account
        if self.checkExist(cursor_out=cursor, type=type):
            update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            sql_query = "update data_monitor set update_time=%s,info=%s,remark=%s  where type=%s"
            values = (update_time, info, remark, type)
        else:
            sql_query = "INSERT INTO data_monitor ( type, update_time, info, remark) VALUES (" \
                        "%s, %s, %s, %s); "
            update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            values = (type, update_time, info, remark)
        print u'跳一下', update_time
        try:
            cursor.execute(sql_query, values)
        except Exception as e:
            print e.msg
        cursor.close()
        self.connector.commit()
        self.connector.close()

    def updateTotal(self, type, account=''):
        """
        :param account:
        :param type:
            sina_total
            tengxun_total
            wangyi_total
            weixin_total
            weixin_source_total
            weixin_account_total
        :return:
        更新总数
        """
        if not type:
            return

        cursor = self.connector.cursor()
        if not cursor:
            return

        count = self.getTotal(cursor_out=cursor, type=type, account=account)

        info = u'总数：' + str(count)
        remark = ''
        if type == 'sina_total':
            remark = u'新浪条数'
        elif type == 'tengxun_total':
            remark = u'腾讯条数'
        elif type == 'wangyi_total':
            remark = u'网易条数'
        elif type == 'weixin_total':
            remark = u'微信条数'
        elif type == 'weixin_source_total':
            remark = u'微信源条数'
        elif type == 'weixin_account_total':
            remark = u'微信源_对应账号条数'
        # 检测是否存在type ,  update_time ,  info , remark, account
        if self.checkExist(cursor_out=cursor, type=type, account=account):
            update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            sql_query = "update data_monitor set update_time=%s,info=%s,remark=%s  where type=%s and account=%s"
            values = (update_time, info, remark, type, account)
        else:
            sql_query = "INSERT INTO data_monitor ( type, update_time, info, remark, account) VALUES (" \
                        "%s, %s, %s, %s, %s); "
            update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            values = (type, update_time, info, remark, account)
        try:
            cursor.execute(sql_query, values)
        except Exception as e:
            print e.msg
        cursor.close()
        self.connector.commit()

    def checkExist(self, cursor_out=None, type='', account=''):
        """
        :param cursor_out:
        :param account:
        :param type:
            sina_total
            tengxun_total
            wangyi_total
            weixin_total
            weixin_source_total
            weixin_account_total
        :return:
        得到总数
        """
        if not cursor_out:
            cursor = self.connector.cursor()
            if not cursor:
                return
        else:
            cursor = cursor_out

        accountWhere = ''
        if account:
            accountWhere = " and account='%s'" % account

        sql_query = "select * from data_monitor where type=%s" + accountWhere
        try:
            cursor.execute(sql_query, (type,))
        except Exception as e:
            print e.msg
        results = cursor.fetchall()
        if not cursor_out:
            cursor.close()
        if results:
            return True
        else:
            return False

    def getTotal(self, cursor_out=None, type='', account=''):
        """
        :param cursor_out:
        :param account:
        :param type:
            sina_total
            tengxun_total
            wangyi_total
            weixin_total
            weixin_source_total
            weixin_account_total
        :return:
        得到总数
        """
        if not cursor_out:
            cursor = self.connector.cursor()
            if not cursor:
                return
        else:
            cursor = cursor_out

        table = ''
        accountWhere = ''

        if type == 'sina_total':
            table = 'sina_detail'
        elif type == 'tengxun_total':
            table = 'tengxun_detail'
        elif type == 'wangyi_total':
            table = 'wangyi_detail'
        elif type == 'weixin_total':
            table = 'weixin_detail'
        elif type == 'weixin_source_total':
            table = 'weixin_source'
        elif type == 'weixin_account_total':
            table = 'weixin_detail'
            if not account:
                return 0
            accountWhere = " where wx_account='%s'" % account

        if not table:
            return 0
        sql_query = "select count(*) from " + table + accountWhere
        try:
            cursor.execute(sql_query)
        except Exception as e:
            print e.msg
        results = cursor.fetchone()
        if not cursor_out:
            cursor.close()
        if results:
            (count,) = results
            return count
        else:
            return 0

# print DataMonitorDao().getTotal(cursor_out=None, type='weixin_account_total', account='qqtech')
# print DataMonitorDao().getAllHeartBeatTime(cursor_out=None)


