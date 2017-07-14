# -*- coding: utf-8 -*-
from scrapy import cmdline

# cmdline.execute("scrapy crawl all  -s HTTPCACHE_ENABLED=0  ".split())


cmdline.execute("scrapy crawl wechat  -s HTTPCACHE_ENABLED=0  ".split())
