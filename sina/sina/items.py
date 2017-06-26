# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SinaContentItem(scrapy.Item):
    title = scrapy.Field()
    publishTime = scrapy.Field()
    fromSource = scrapy.Field()
    contents = scrapy.Field()  # 一个数组
    image_urls = scrapy.Field()  # [{'url':'', 'hash':''}]
    # image_urls和images是固定的
