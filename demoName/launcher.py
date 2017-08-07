# -*- coding: utf-8 -*-
from scrapy import cmdline
cmdline.execute("scrapy crawl demoName_detail  -s HTTPCACHE_ENABLED=0  ".split())


