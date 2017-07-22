# -*- coding: utf-8 -*-
import re

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


def clearUrl(value):
    # 替换样式里面的链接
    # url\(\s *\"?http.*?\"?\s*\)
    # url(http://storage.fedev.sina.com.cn/components/floatBarRight/40b6e9494c042dc1cb8682aac0e174d0.png)
    # url( "http://mat1.gtimg.com/www/images/channel_logo/tech_logo.png "  )
    # url(data:image/png;base64,iVBORw0KGgo)
    pAll = re.compile('url\(.*?\)')
    matchUrls = pAll.findall(value)
    if len(matchUrls):
        for matchUrl in matchUrls:
            value = value.replace(matchUrl, 'url("")')

    # ngMethod=scale,src=http://www.sinaimg.cn/IT/deco/2014/0619/index/playIconH.png)}
    pAll = re.compile('src=.*?\)')
    matchUrls = pAll.findall(value)
    if len(matchUrls):
        for matchUrl in matchUrls:
            value = value.replace(matchUrl, 'src="")')

    # (src="https://mat1.gtimg.com/news/base2011/img/trs.png",s
    pAll = re.compile('src=\".*\"')
    matchUrls = pAll.findall(value)
    if len(matchUrls):
        for matchUrl in matchUrls:
            value = value.replace(matchUrl, 'src="")')
    return value

# cc = CssUtil()
# css = cc.downLoad('http://img1.cache.netease.com/cnews/css07/style.css').decode('gbk')
# css2 = cc.downLoad('http://img1.cache.netease.com/cnews/css13/endpage1301_v1.7.9.css').decode('gbk')
# print cc.compressCss([css, css2])
