# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class WYContentItem(scrapy.Item):
    content_txt = scrapy.Field()
    image_urls = scrapy.Field()
    title = scrapy.Field()
    source_url = scrapy.Field()
    post_date = scrapy.Field()
    channel_name = scrapy.Field()
    post_user = scrapy.Field()
    tags = scrapy.Field()
    styles = scrapy.Field()
    content_html = scrapy.Field()  # 带标签的内容
    hash_code = scrapy.Field()
    info_type = scrapy.Field()
    src_source_id = scrapy.Field()
    src_account_id = scrapy.Field()
    src_channel = scrapy.Field()
