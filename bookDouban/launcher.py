# -*- coding: utf-8 -*-
from scrapy import cmdline

cmdline.execute("scrapy crawl crawl_ip  -s HTTPCACHE_ENABLED=0  ".split())