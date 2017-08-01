# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random


class RandomUserAgent(object):
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class ExceptionMiddleware(object):
    def process_request(self, request, spider):
        print 'process_request', request.url

    def process_response(self, request, response, spider):
        print 'process_response', request.url, response.status
        return response
        # 这边根据response的status判断是正常的还是ip被禁止了，然后根据类型返回response或者是再次执行request

    def process_exception(self, request, exception, spider):
        print 'process_exception', exception
        spider.logDao.info(u'抓取异常：' + exception.message)