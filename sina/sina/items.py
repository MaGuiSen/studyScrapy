# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ContentItem(scrapy.Item):
    content_txt = scrapy.Field()
    image_urls = scrapy.Field()
    title = scrapy.Field()
    source_url = scrapy.Field()
    post_date = scrapy.Field()
    sub_channel = scrapy.Field()
    post_user = scrapy.Field()
    tags = scrapy.Field()
    styles = scrapy.Field()
    content_html = scrapy.Field()  # 带标签的内容
    hash_code = scrapy.Field()
    info_type = scrapy.Field()
    src_source_id = scrapy.Field()
    src_account_id = scrapy.Field()
    src_channel = scrapy.Field()
    src_ref = scrapy.Field()
