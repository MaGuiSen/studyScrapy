# -*- coding: utf-8 -*-
from scrapy import cmdline

cmdline.execute("scrapy crawl wx_source  -s HTTPCACHE_ENABLED=0  ".split())