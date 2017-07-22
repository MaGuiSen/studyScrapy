# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ContentItem(scrapy.Item):
    wx_name = scrapy.Field()
    wx_account = scrapy.Field()
    wx_url = scrapy.Field()
    wx_avatar = scrapy.Field()
    update_status = scrapy.Field()
    source_id = scrapy.Field()  # 1

