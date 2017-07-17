# -*- coding: utf-8 -*-
from scrapy import cmdline

cmdline.execute("scrapy crawl sina  -s HTTPCACHE_ENABLED=0  ".split())