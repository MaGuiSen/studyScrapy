# -*- coding: utf-8 -*-
from scrapy import cmdline
# cmdline.execute("scrapy crawl sina2  -s HTTPCACHE_ENABLED=0  ".split())
cmdline.execute("scrapy crawl sina_history  -s HTTPCACHE_ENABLED=0  ".split())
