# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time

from mysql.connector import MySQLConnection
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from libMe.util.FileUtil import FileUtil
from .items import ContentItem


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
            port=settings['MYSQL_PORT'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            use_unicode=False,
        )
        connector = MySQLConnection(**dbParams)
        return cls(connector)  # 相当于dbpool付给了这个类，self中可以得到

    def __init__(self, connector):
        self.connector = connector

    def process_item(self, item, spider):
        cursor = self.connector.cursor()
        if isinstance(item, ContentItem):
            # 如果存在，则不做处理
            spider.logDao.info(u'存网易详情：' + item['title'])
            sql = "insert into wangyi_detail (" \
                  "content_txt,title,source_url,post_date,sub_channel,post_user,tags,styles," \
                  "content_html,hash_code,info_type,src_source_id,src_channel,src_ref,update_time) " \
                  "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

            update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            try:
                cursor.execute(sql, (
                    item['content_txt'],
                    item['title'],
                    item['source_url'],
                    item['post_date'],
                    item['sub_channel'],
                    item['post_user'],
                    item['tags'],
                    item['styles'],
                    item['content_html'],
                    item['hash_code'],
                    item['info_type'],
                    item['src_source_id'],
                    item['src_channel'],
                    item['src_ref'],
                    update_time))
                spider.logDao.info(u'存网易详情：' + item['title'] + u'  成功')
            except Exception, e:
                print e
        else:
            pass
        cursor.close()
        self.connector.commit()
        return item

    def close_spider(self, spider):
        self.connector.commit()


class MyImagesPipeline(ImagesPipeline):
    def __init__(self, store_uri, download_func=None, settings=None):
        super(MyImagesPipeline, self).__init__(store_uri, download_func=None, settings=None)
        botName = 'wangyi'  # 注意需要更改。。。
        self.fileUtil = FileUtil(u'/news/' + botName + u'/image/',
                                 u'img/')

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url['url'])

    def item_completed(self, results, item, info):
        # [{path:'', url:''}]
        image_urls = []
        for ok, x in results:
            if ok:
                url = x['url']
                path = x['path']
                # # TODO...
                # break
                imgUrl = self.fileUtil.upload(path)
                if imgUrl:
                    # 拿出内容，然后替换路径为url
                    item['content_html'] = item['content_html'].replace('&amp;', '&').replace(url, imgUrl)
        return item
