# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

class MysqlPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        print 'heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
        pass

class MyImagesPipeline(ImagesPipeline):
    def __init__(self, store_uri, download_func=None, settings=None):
        super(MyImagesPipeline, self).__init__(store_uri, download_func=None, settings=None)
        botName = 'weixin'  # 注意需要更改。。。

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
        return item

class MyImageDownLoad(ImagesPipeline):
    def __init__(self, store_uri, download_func=None, settings=None):
        super(MyImagesPipeline, self).__init__(store_uri, download_func=None, settings=None)
        botName = 'weixin'  # 注意需要更改。。。

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
        return item
