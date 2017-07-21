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
from scrapy import Selector

value = """
ckground-image:url(http://i.sso.sina.com.cn/images/login/top_account_icon_v2.png);_background-image:url(http://i.sso.sina.com.cn/images/login/top_account_icon_ie6_v2.png)}.T
"""

selector = Selector(text=value)
print 1
