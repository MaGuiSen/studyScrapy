# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time

import requests
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from libMe.db.Connector import Connector
from libMe.util.FileUtil import UploadUtil
from util import EncryptUtil
from util import FileUtil
from util import TimerUtil
from .items import ContentItem


class MysqlPipeline(object):
    def __init__(self):
        self.connector = Connector()

    def process_item(self, item, spider):
        cursor = self.connector.cursor()
        if not cursor:
            return item
        if isinstance(item, ContentItem):
            # 如果存在，则不做处理
            spider.logDao.info(u'存新浪详情：' + item['title'])
            sql = "insert into sina_detail (" \
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
                spider.logDao.info(u'存新浪详情：' + item['title'] + u'  成功'+ u' ' + item['post_date'])
            except Exception, e:
                spider.logDao.warn(u'存新浪详情：' + item['title'] + u'  失败')
                spider.logDao.warn(u'存新浪详情错误信息：' + e.message)
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
        botName = 'sina'  # 注意需要更改。。。
        self.fileUtil = UploadUtil(u'/news/' + botName + u'/image/',
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


class MyImageDownLoad(object):
    @classmethod
    def from_settings(cls, settings):
        savePath = settings['IMAGES_STORE']
        botName = settings['BOT_NAME']
        return cls(botName, savePath)  # 相当于dbpool付给了这个类，self中可以得到

    def __init__(self, botName, savePath):
        self.botName = botName
        self.savePath = savePath
        self.fileUtil = UploadUtil(u'/news/' + botName + u'/image/',
                                   u'img/')

    def process_item(self, item, spider):
        image_urls = []
        for image_url in item['image_urls']:
            url = image_url.get('url')
            urlHash = EncryptUtil.md5(url)
            path = 'full/' + str(urlHash) + '.jpg'
            detailPath = self.savePath + '/' + path
            # 创建目录
            saveDir = self.savePath + '/full'
            if not FileUtil.dirIsExist(saveDir):
                FileUtil.createDir(saveDir)

            if FileUtil.fileIsExist(detailPath):
                spider.logDao.info(u'图片已经存在本地:' + url)
                image_url_new = {
                    'ok': True,
                    'x': {
                        'url': url,
                        'path': path
                    }
                }
            else:
                try:
                    fileResponse = requests.get(url, timeout=10)
                    req_code = fileResponse.status_code
                    req_msg = fileResponse.reason
                    if req_code == 200:
                        open(detailPath, 'wb').write(fileResponse.content)
                        image_url_new = {
                            'ok': True,
                            'x': {
                                'url': url,
                                'path': path
                            }
                        }
                        spider.logDao.info(u'图片成功下载:' + url)
                    else:
                        spider.logDao.info(u'下载图片失败:' + url)
                        image_url_new = {
                            'ok': False,
                            'x': {
                                'url': url,
                            }
                        }
                except Exception, e:
                    print e
                    spider.logDao.warn(u'下载图片失败:' + url)
                    image_url_new = {
                        'ok': False,
                        'x': {
                            'url': url,
                        }
                    }
            image_urls.append(image_url_new)
            # 空转2s
            TimerUtil.sleep(2)

        for image_url in image_urls:
            ok = image_url.get('ok', False)
            if ok:
                x = image_url.get('x', {})
                url = x['url']
                path = x['path']
                # 上传照片
                imgUrl = self.fileUtil.upload(path)
                if imgUrl:
                    # 拿出内容，然后替换路径为url
                    item['content_html'] = item['content_html'].replace('&amp;', '&').replace(url, imgUrl)
                    spider.logDao.warn(u'上传图片成功:' + imgUrl)
        item['image_urls'] = image_urls
        return item
