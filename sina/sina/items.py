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
    page_content = scrapy.Field()  # 一个数组
    image_urls = scrapy.Field()  # [{'url':'', 'hash':''}]
    title = scrapy.Field()
    source_url = scrapy.Field()
    post_date = scrapy.Field()
    channel_name = scrapy.Field()
    post_user = scrapy.Field()
    tags = scrapy.Field()
