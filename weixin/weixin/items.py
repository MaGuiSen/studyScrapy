# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WXDetailItem(scrapy.Item):
    post_date = scrapy.Field()  # 发表时间
    post_user = scrapy.Field()  # 发表的人
    page_content = scrapy.Field()  # 文章内容
    title = scrapy.Field()  # 标题
    wx_account = scrapy.Field()  # 微信账户
    source_url = scrapy.Field()  # 来源url
    image_urls = scrapy.Field()  # 图片替换
    update_time = scrapy.Field()  # 数据库更新时间
