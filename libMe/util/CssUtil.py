# -*- coding: utf-8 -*-
import requests
from csscompressor import compress

def downLoad(url):
    result = requests.get(url, timeout=5)
    if result.status_code == 200:
        return result.content
    else:
        return ''


def compressCss(listCss):
    listCss = ''.join(listCss)
    return compress(listCss)

# cc = CssUtil()
# css = cc.downLoad('http://img1.cache.netease.com/cnews/css07/style.css').decode('gbk')
# css2 = cc.downLoad('http://img1.cache.netease.com/cnews/css13/endpage1301_v1.7.9.css').decode('gbk')
# print cc.compressCss([css, css2])