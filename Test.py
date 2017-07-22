# # -*- coding: utf-8 -*-
#
# import sys, re, os
# from collections import deque
# from bs4 import BeautifulSoup, Tag
# from csscompressor import compress
#
# # html param
# html = sys.argv[1]
# # target param
# target = sys.argv[2]
# # path from html param
# path = re.sub(r"[^\/]*$", "", html)
# # open html file
# soup = BeautifulSoup(open(html))
# # find last script as anchorpoint
# lastScript = soup.findAll("script", attrs = {"src" : True})[-1]
# # get all scripts containing src attribute (= external scripts)
# scripts = soup.findAll("script", attrs = {"src" : True})
# # find last style link as anchorpoint
# lastStylesheet = soup.findAll("link", attrs = {"rel" : "stylesheet"})[-1]
# # get all links to css stylesheets
# stylesheets = soup.findAll("link", attrs = {"rel" : "stylesheet"})
#
# # create list of script srcs
# print("\nRead Scripts:")
# scriptsSrc = deque()
# for script in scripts:
#     scriptsSrc.append(path + script.attrs["src"])
#     print("\t" + path + script.attrs["src"])
#
# # create list of stylesheets srcs
# print("\nRead Stylesheets:")
# stylesheetsSrc = deque()
# for stylesheet in stylesheets:
#     stylesheetsSrc.append(path + stylesheet.attrs["href"])
#     print("\t" + path + stylesheet.attrs["href"])
#
# # merge stylsheets to temp.css
# print("Merge Stylesheets:")
# with open("temp.css", "w") as outfileCSS:
#     for fname in stylesheetsSrc:
#         # add space every script
#         outfileCSS.write("\n")
#         with open(fname) as infile:
#             for line in infile:
#                 outfileCSS.write(line)
# print("\n");
#
# # minify javascript
# print("Minify temp.js\n\t~")
# with open("temp.js") as js:
#     minified_js = jsmin(js.read())
#
# # minify css
# print("\nMinify temp.css\n\t~")
# with open("temp.css") as css:
#     minified_css = compress(css.read())
#
# # replace scripts with merged and min embed script / css
# print("\nReplacing and deleting\n\t~")
# tag = soup.new_tag("script")
# tag["type"] = "text/javascript"
# tag.append(minified_js)
# lastScript.replace_with(tag)
#
# tag = soup.new_tag("style")
# tag["type"] = "text/css"
# tag.append(minified_css)
# lastStylesheet.replace_with(tag)
#
# #remove script and style tags
# for script in scripts:
#     script.decompose()
# for stylesheet in stylesheets:
#     stylesheet.decompose()
#
# #remove temp
# os.remove("temp.js")
# os.remove("temp.css")
#
# #save html as target
# file = open(target,"w")
# file.write(soup.prettify())
# file.close()
#
# print("\nFIN\n")
#
#
#
# for fname in stylesheetsSrc:
# import urllib
#
# connect_url = 'http://s1.hao123img.com/resource/fe/pkg/aio-eef856ab5.1fd5261cd.css'
# # # add space every script
# # with open(fname, 'wb') as infile:
# #     for line in infile:
# #         print line
#
# import requests
# ress = requests.get(connect_url, timeout=5)
# print ress.status_code
# import os
#
# # from qcloud_cos import CosClient
# # from qcloud_cos import UploadFileRequest
# #
# #
# #
# # def get_cos_client():
# #     # -1251316472.cossh.myqcloud.com
# #     appid = 1251316472  # 替换为用户的appid
# #     secret_id = u'AKID3atJdSnNR1Bwf1l4HnnYaSMzpBArC4A5'  # 替换为用户的secret_id
# #     secret_key = u'I2J7ho6wpQRRUpdX8K6KISBJCYSlm1hq'  # 替换为用户的secret_key
# #     region_info = "sh"  # 替换为用户的region，例如 sh 表示华东园区, gz 表示华南园区, tj 表示华北园区
# #     cos_client = CosClient(appid, secret_id, secret_key, region=region_info)
# #     return cos_client
# #
# #
# # client = get_cos_client()
# # request = UploadFileRequest(u"crawler", u'/news/wangyi/image/9fd29328f26019137720286869de5ee28922c1e0.jpg', u'./res/img/wangyi/full/9fd29328f26019137720286869de5ee28922c1e0.jpg', insert_only=0)
# # upload_file_ret = client.upload_file(request)
# # if upload_file_ret['code'] == 0:
# #     print u'upload successfully',upload_file_ret
# #     # print upload_file_ret
# # else:
# #     print u'fail to uplaod ',upload_file_ret


# # print """
# #     \\aaaa,'''''
# # """.replace('\'', '"').replace('\\', '\\\\')
# import time
#
# print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1500608959))
import re

from scrapy import Selector

value = """
ntComment:hover{background-color:#d9d9d9;background-position:0 0;cursor:default}.CCC-floa
t-bar-right .CCC-fbr-share{background:url(http://storage.fedev.sina.com.cn/components/floatBarRight/40b6e9494c042dc1cb8682aac0e174d0.png) no-repeat 0 0}.CCC-float-bar-right
.CCC-fbr-share:hover{background-image:url(http://storage.fedev.sina.com.cn/components/floatBarRight/40b6e9494c042dc1cb8682aac0e174d0.png)}.CCC-float-bar-right .CCC-fbr-rel-read{bac
kground:url(http://storage.fedev.sina.com.cn/components/floatBarRight/9bda1595692833a35266d0166794579a.png) no-repeat 0 0}.CCC-float-bar-right .CCC-fbr-rel-read:hover{background-i
mage:url(http://storage.fedev.sina.com.cn/components/floatBarRight/9bda1595692833a35266d0166794579a.png)}.CCC-float-bar-right .CCC-fbr-rec-read{bac
kground:url(http://storage.fedev.sina.com.cn/components/floatBarRight/9bda1595692833a35266d0166794579a.png) no-repeat 0 0}.CCC-float-bar-right .CCC-fbr-rec-read:hover{back
ground-image:url(http://storage.fedev.sina.com.cn/components/floatBarRight/9bda1595692833a35266d0166794579a.png)}.CCC-float-bar-right .CCC-fbr-share-weibo{backgro
und:url(http://storage.fedev.sina.com.cn/components/floatBarRight/b2dc9d062dfa9b83e7d014f78058f61c.png) no-repeat 0 0}.CCC-float-bar-right .CCC-fbr-share-weibo:h
over{background-image:url(http://storage.fedev.sina.com.cn/components/floatBarRight/b2dc9d062dfa9b83e7d014f78058f61c.png)}.CCC-float-bar-right .CCC-fbr-share
-weixin{background:url(http://storage.fedev.sina.com.cn/components/floatBarRight/76eca8efdc993ebd26e02a8f03c27baf.png) no-repeat 0 0}.CCC-float-bar-right .
CCC-fbr-share-weixin:hover{background-image:url(http://storage.fedev.sina.com.cn/components/floatBarRight/76eca8efdc993ebd26e02a8f03c27baf.png)}.CCC-float-
bar-right .CCC-fbr-to-top{background:url(http://storage.fedev.sina.com.cn/components/floatBarRight/41b1c76ccf09dc08379eb9dbaa818d5f.png) no-repeat 0 0}.CC
C-float-bar-right .CCC-fbr-to-top:hover{background-image:url(http://storage.fedev.sina.com.cn/components/floatBarRight/41b1c76ccf09dc08379eb9dbaa818d5f.png)}.
CCC-float-bar-right .CCC-fbr-title{position:absolute;bottom:7px;display:inline-block;width:62px;text-align:center;font-size:12px;color:#7b7b7b}.CCC-float-bar-right
.CCC-fbr-box:hover .CCC-fbr-title{color:#fff}.CCC-float-bar-right .CCC-fbf-preventComment:hover .CCC-fbr-title{color:#7b
ckground-image:url( "http://mat1.gtimg.com/www/images/channel_logo/tech_logo.png "  );_background-image:url("http://mat1.gtimg.com/www/dddddaaa/channel_logo/tech_logo.png")}.T

dth:62px;text-align:center;font-size:12px;color:#7b7b7b}.CCC-
float-bar-right .CCC-fbr-box:hover .CCC-fbr-titl
e{color:#fff}.CCC-float-bar-right .CCC-fbf-prev
entComment:hover .CCC-fbr-title{color:#7b7b7b}
.CCC-float-bar-right .CCC-fbr-box .CCC-fbr-di
an{position:absolute;width:14px;height:14px;b
ackgrou
nd:url(data:image/gif;base64,R0lGODlhDAAMAJEDAP/U1f/Fx+k0O////yH/C05FVFNDQVBFMi4wAwEAAAAh/wtYTVAgRGF0YVhNUDw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDE0IDc5LjE1MTQ4MSwgMjAxMy8wMy8xMy0xMjowOToxNSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDoxOTVERTM2QzBBQTQxMUU2ODk4NUMwM0U4NUMyNEY2NSIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDoxOTVERTM2RDBBQTQxMUU2ODk4NUMwM0U4NUMyNEY2NSI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjE5NURFMzZBMEFBNDExRTY4OTg1QzAzRTg1QzI0RjY1IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjE5NURFMzZCMEFBNDExRTY4OTg1QzAzRTg1QzI0RjY1Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEgHx4dHBsaGRgXFhUUExIREA8ODQwLCgkIBwYFBAMCAQAAIfkEBQ8AAwAsAAAAAAwADAAAAhGcj6nLKC8WhGq+avGUtPnfFAAh+QQJDwADACwCAAIACAAIAAACD9yAYLesfV5DMFYlmUmvAAAh+QQJDwADACwAAAAADAAMAAACJZyPGcsaYMA6U1gxZgb3ShMMnZWB4lhuo/BlYedST6TJTJjkRwEAIfkECQ8AAwAsAAAAAAwADAAAAiCcg2mnk8HWQg4OgQWjOVfbYdEVbmT3gV7FSu2zWTFlFAAh+QQJCAADACwAAAAADAAMAAACIJyDaavTHhaLyIgrjsIYxsFdmhVqUZglHzdWEjR9j/kUACH5BAUIAAMALAAAAAAMAAwAAAIgnINpizt9gotPDoFFtDnT22mVEYpQuZHeCDltO7pJWwAAOw==) no-repeat 0 0;right:8px;top:5px}.CCC
-float-bar-right .CCC-fbr-box:hove
r .CCC-fbr
-di
an{backg
round:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMCAYAAABWdVznAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDE0IDc5LjE1MTQ4MSwgMjAxMy8wMy8xMy0xMjowOToxNSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo0Q0U2NTJBNDE3NTMxMUU2OURBMkU4OERCRDczNjRCMCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo0Q0U2NTJBNTE3NTMxMUU2OURBMkU4OERCRDczNjRCMCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjRDRTY1MkEyMTc1MzExRTY5REEyRTg4REJENzM2NEIwIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjRDRTY1MkEzMTc1MzExRTY5REEyRTg4REJENzM2NEIwIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+ECszHgAAAFpJREFUeNpi/P//PwMpgImBRICuYRoQ/0fD05AVsKApznxlaoNigtjpI5lQZhaIYETyw390xUiawGqp4gfaapgOdSs290+HC4A8jYSn/ccE05DVMNI8pgECDAA2XkSDwAbgdAAAAABJRU5ErkJggg==) no-repeat 0 0}.CCC-weixin-box{left:50%;top:50%;margin-left:-110px;margin-top:-123px;position:fixed;height:246px;width:220px;z-index:100000001;font-size:12px;border:6px solid #7f7f7f;border-radius:5px;display:none}.CCC-weixin-box .CCC-wxb-top{width:100%;color:#666;background:#f2f2f2;height:24px;line-height:24px;border-bottom:1px solid #e8e8e8}.CCC-weixin-box .CCC-wxb-close{top:0;right:15px;cursor:pointer;position:absolute;z-index:10000000;color:#666;font-weight:bold;font-family:Helvetica,Arial;font-size:14px;line-height:24px}.CCC-weixin-box .CCC-wxb-top span{margin-left:15px}.CCC-weixin-box .CCC-wxb-qrcode-box{background-color:#fff;height:220px;width:220px}.CCC-weixin-box .CCC-wxb-qrcode-box img{width:178px;height:178px;margin:21px}.CCC-comment-box{width:937px;position:fixed;display:none;top:0;right:-937px;z-index:90001}.CCC-comment-mode .CCC-comment-box{right:0;-webkit-animation:showComment .5s forwards;animation:showComment .5s forwards;display:block}.CCC-comment-box .CCC-comment-close{position:absolute;left:0;top:0;width:22px;height:37px;overflow:hidden;background:url("") no-repeat 6px center #fff;border:1px solid #d8d8d8;border-right:0;text-indent:-999



hot{padding-left:30px;background-position:-17px -665px}.feed-card-icon-qaq{padding-left:31px;background-position:-16px -428px}.feed-card-ico
n-qaa{width:30px;height:23px;background-position:-16px -486px;float:left}.feed-card-ic
on-vote{padding-left:50px;background-position:0 -576px}.feed-card-icon-score{paddi
ng-left:50px;background-position:0 -620px}.feed-card-icon-video{padding-left:30px
;background-position:-17px -24px}.feed-card-icon-svideo{background:url("") no-repeat;_
background-image:none;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(ena
bled=true,sizingMethod=scale,src=http://www.sinaimg.cn/IT/deco/2014/0619/index/playIcon.png);cursor
:pointer;height:22px;width:22px;display:block}.feed-card-icon-svideo:hover{background:url("") no-re
peat;_background-image:none;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=tru
e,sizingMethod=scale,src=http://www.sinaimg.cn/IT/deco/2014/0619/index/playIconH.png)}.feed-card-icon-img{padding-left:30px;background-position:-17px -55px}.feed-card-icon-picAlbum{font-size:13px;color:#666;height:23px;line-height:23px;font-style:normal;padding-left:24px;background-position:-24px -85px;font-weight:normal}.feed-card-icon-topic{padding-left:50px;background-position:0 -116px}.feed-card-icon-bbs{padding-left:26px;background-position:-23px -536px}.feed-card-icon-wb{padding-left:30px;background-position:-17px -147px}.feed-card-picAlbum-i{float:left;margin-right:5px
er(src="https://mat1.gtimg.com/news/base2011/img/trs.png",s
"""

def clearUrl(value):
    # 替换样式里面的链接
    pAll = re.compile('url\(\s*\"?http.*?\"?\s*\)')
    matchUrls = pAll.findall(value)
    if len(matchUrls):
        for matchUrl in matchUrls:
            value = value.replace(matchUrl, 'url("")')
    return value

print clearUrl(value)

print aaaa

