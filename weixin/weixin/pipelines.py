# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import json

import time
from mysql.connector import MySQLConnection
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from weixin.items import WXDetailItem


class WeixinPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    @classmethod
    def from_settings(cls, settings):
        """1、@classmethod声明一个类方法，而对于平常我们见到的则叫做实例方法。
           2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
           3、可以通过类来调用，就像C.f()，相当于java中的静态方法"""
        dbParams = dict(
            host=settings['MYSQL_HOST'],  # 读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            use_unicode=False,
        )
        connector = MySQLConnection(**dbParams)
        return cls(connector)  # 相当于dbpool付给了这个类，self中可以得到

    def __init__(self, connector):
        self.connector = connector

    def process_item(self, item, spider):
        cursor = self.connector.cursor()
        if isinstance(item, WXDetailItem):
            # 如果存在，则不做处理
            if not self.checkDetailExist(cursor, item['title']):
                spider.logDao.info(u'存微信详情：' + item['title'])
                sql = "insert into wx_detail (post_date,post_user,page_content,title,wx_account,source_url,image_urls,"\
                      "update_time) values(%s,%s,%s,%s,%s,%s,%s,%s) "
                update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                cursor.execute(sql, (item['post_date'],
                                     item['post_user'],
                                     item['page_content'],
                                     item['title'],
                                     item['wx_account'],
                                     item['source_url'],
                                     json.dumps(item['image_urls'], encoding="utf8", ensure_ascii=False),
                                     update_time))
        else:
            pass
        cursor.close()
        spider.logDao.info(u'存微信详情：' + item['title']+ '成功')
        self.connector.commit()
        return item

    def checkDetailExist(self, cursor,  title):
        sql_query = 'select title from wx_detail where title=%s'
        cursor.execute(sql_query, (title, ))
        results = cursor.fetchall()
        if results:
            return True
        else:
            return False

    def close_spider(self, spider):
        self.connector.commit()


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url['url'])

    def item_completed(self, results, item, info):
        # [{path:'', url:''}]
        image_urls = []
        for ok, x in results:
            if ok:
                print(x)
                url = x['url']
                path = x['path']
                m2 = hashlib.md5()
                m2.update(url)
                image_hash = m2.hexdigest()
                image_urls.append({
                    'path': path,
                    'hash': image_hash,
                    'url': url
                })
        item['image_urls'] = image_urls
        return item