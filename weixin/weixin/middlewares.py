# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals


class RandomUserAgent(object):
    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class WeixinSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ExceptionMiddleware(object):
    def process_request(self, request, spider):
        print 'process_request', request.url

    def process_response(self, request, response, spider):
        print 'process_response', request.url, response.status
        return response
        # 这边根据response的status判断是正常的还是ip被禁止了，然后根据类型返回response或者是再次执行request

    def process_exception(self, request, exception, spider):
        print '#### ExceptionMiddleware process_exception ####', exception
        # {'request_type': 'wx_source', 'url': newUrl,
        #  'wx_account': wx_account, 'source': source}
        request_type = request.meta['request_type']
        if request_type == 'wx_source':
            # 只有在数据源请求发生错误才将当前数据源状态更新为失败
            wx_account = request.meta['wx_account']
            spider.wxSourceDao.updateStatus(wx_account, 'updateFail')
            spider.logDao.info(u'数据源抓取异常：' + wx_account + ':' + exception.message)
        if request_type == 'wx_page_list':
            # 不做处理，让其自动结束
            url = request.meta['url']
            spider.logDao.info(u'列表抓取异常：' + url + ':' + exception.message)
        if request_type == 'wx_detail':
            # 不做处理，让其自动结束
            detailUrl = request.meta['detailUrl']
            spider.logDao.info(u'详情抓取异常：' + detailUrl + ':' + exception.message)
