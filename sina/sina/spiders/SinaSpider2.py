# -*- coding: utf-8 -*-
import hashlib
import random
import json
import re

import scrapy
import time
from scrapy import Selector

from libMe.db.LogDao import LogDao
from libMe.util import CssUtil
from libMe.util import EncryptUtil
from libMe.util import NetworkUtil
from libMe.util import EncodeUtil
from libMe.util import TimerUtil
from ..db.CheckDao import CheckDao
from ..items import ContentItem

import demjson


# 60s整体刷新一次
class SinaSpider(scrapy.Spider):
    name = 'sina2'
    download_delay = 2.5  # 基础间隔 0.5*download_delay --- 1.5*download_delays之间的随机数
    handle_httpstatus_list = [301, 302, 204, 206, 403, 404, 500]  # 可以处理重定向及其他错误码导致的 页面无法获取解析的问题

    # 错误码 [scrapy.downloadermiddlewares.retry] DEBUG: Retrying <GET http://tech.sina.com.cn/i/2017-07-18/doc-ifyiakur9086112.shtml> (failed 1 times): TCP connection timed out: 10060: �������ӷ���һ��ʱ���û����ȷ�𸴻����ӵ�����û�з�Ӧ�����ӳ���ʧ�ܡ�.
    # [scrapy.downloadermiddlewares.retry] DEBUG: Retrying <GET http://tech.sina.com.cn/i/2017-07-17/doc-ifyiakwa4300270.shtml> (failed 1 times): User timeout caused connection failure: Getting http://tech.sina.com.cn/i/2017-07-17/doc-ifyiakwa4300270.shtml took longer than 180.0 seconds..
    def __init__(self, name=None, **kwargs):
        super(SinaSpider, self).__init__(name=None, **kwargs)
        self.count = 0
        self.request_stop = False
        self.request_stop_time = 0
        self.logDao = LogDao(self.logger, 'sina_detail')
        self.checkDao = CheckDao()
        # 用于缓存css
        self.css = {
            'hash': 'style'
        }

    def start_requests(self):
        # while True:
        # 检测网络
        if not NetworkUtil.checkNetWork():
            # 20s检测一次
            TimerUtil.sleep(20)
            self.logDao.warn(u'检测网络不可行')
            # continue

        # 检测服务器
        if not NetworkUtil.checkService():
            # 20s检测一次
            TimerUtil.sleep(20)
            self.logDao.warn(u'检测服务器不可行')
            # continue

        if self.request_stop:
            # 拨号生效时间不定，所以需要间隔一段时间再重试
            timeSpace = time.time() - self.request_stop_time
            if timeSpace / 60 <= 2:
                # 当时间间隔小于 2分钟 就不请求
                # continue
                pass
            else:
                self.request_stop = False

        # 进行爬虫

        url = 'http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=96&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page=1'
        # url = 'http://tech.sina.com.cn/t/2017-07-24/doc-ifyihrit1274195.shtml'

        if self.request_stop:
            self.logDao.warn(u'出现被绊或者出现网络异常，退出循环')
            # 当网络出现被绊的情况，就需要停止所有的请求等待IP更换
            # break
        r = random.uniform(0, 1)
        newUrl = url + ('&r=' + str(r))
        self.logDao.info(u"开始抓取列表：" + newUrl)
        yield scrapy.Request(url=newUrl, meta={'request_type': 'sina_list', 'url': newUrl}, callback=self.parseList)

        # if self.request_stop:
        #     # 需要发起通知 进行重新拨号
        #     self.logDao.warn(u'发送重新拨号信号，请等待2分钟会尝试重新抓取')
        #     self.request_stop_time = time.time()
        #     pass
        # else:
        #     # 正常抓好之后，当前跑空线程10分钟，不影响一些还没请求完成的request
        #     self.logDao.info(u'请求了一轮了，但是可能还有没有请求完成，睡一会10分钟')
        #     TimerUtil.sleep(10 * 60)
        #     pass

    # TODO。。还没有找到被禁止的情况
    def parseList(self, response):
        data = EncodeUtil.toUnicode(response.body)
        if False:
            self.logDao.info(u'访问过多被禁止')
        else:
            url = response.meta['url']
            self.logDao.info(u'开始解析列表' + url)

            data = data.lstrip('var jsonData = ').rstrip(';')
            # 格式化
            data = demjson.decode(data) or {}

            list = data.get('list') or []

            for item in list:
                itemTime = item.get('time') or 0
                channel = item.get('channel') or {}
                channel_name = channel.get('title')
                source_url = item['url']
                callback = self.parseDetail2
                if self.checkDao.checkExist(source_url):
                    self.logDao.info(u'文章已经存在：' + source_url)
                    continue
                self.logDao.info(u"开始抓取文章：" + item['url'])
                # item['url'] = "http://tech.sina.com.cn/i/2017-07-21/doc-ifyihrmf3085159.shtml"
                yield scrapy.Request(url=item['url'],
                                     meta={'request_type': 'sina_detail', 'category': channel_name,
                                           'title': item['title'], 'source_url': item['url']},
                                     callback=callback)

    def parseDetail2(self, response):
        body = EncodeUtil.toUnicode(response.body)
        if False:
            self.logDao.info(u'访问过多被禁止')
        else:
            category = response.meta['category']
            title = response.meta['title']
            source_url = response.meta['source_url']
            self.logDao.info(u'开始解析文章:' + title + ':' + category + ':' + source_url)

            selector = Selector(text=body)

            # 得到样式
            styleUrls = selector.xpath('//link[@rel="stylesheet"]/@href').extract()
            styleList = []
            for styleUrl in styleUrls:
                # 得到hash作为key
                styleUrlHash = EncryptUtil.md5(styleUrl)
                if not self.css.get(styleUrlHash):
                    # 不存在则去下载 并保存
                    self.css[styleUrlHash] = CssUtil.downLoad(styleUrl)
                styleList.append(self.css[styleUrlHash])
            styles = CssUtil.compressCss(styleList).replace('\'', '"').replace('\\', '\\\\')
            styles = CssUtil.clearUrl(styles)

            post_date = selector.xpath('//*[@id="pub_date"]/text() | //*[@class="titer"]/text()').extract_first('')
            post_date = post_date.replace('\r\n', '').strip(' ').replace(u'年', '-').replace(u'月', '-').replace(u'日', '')
            src_ref = selector.xpath(
                '//*[@id="media_name"]/a[1]/text() | //*[@class="source"]/a/text() | //*[@class="source"]/text()').extract_first(
                '')

            post_user = selector.xpath('//*[@id="author_ename"]/a/text()').extract_first('')

            tags = selector.xpath('//p[@class="art_keywords"]/a/text()').extract() or []
            tags = ','.join(tags)

            content_html = selector.xpath('//*[@id="artibody"][1]')
            if len(content_html):
                # 去除内部不需要的标签
                # 完整案例：content_html.xpath('*[not(boolean(@class="entHdPic" or @class="ep-source cDGray")) and not(name(.)="script")]').extract()
                content_items = content_html.xpath('*[not(boolean(@class="entHdPic")) and not(name(.)="script")]')

                # 得到纯文本
                content_txt = []
                for item in content_items:
                    # 文本
                    # TODO...之后处理 取出标题类型
                    allTxt = item.xpath('.//text()').extract()
                    allTxt = ''.join(allTxt).replace('\t', '')
                    if u'来源：' in allTxt:
                        # 说明这是真正的来源
                        if not post_user:
                            # 先替换作者 ，如果不存在的话
                            post_user = src_ref
                        src_ref = allTxt.replace(u'来源：', '').strip(u' ')
                    # 加入
                    content_txt.append(allTxt)
                content_txt = '\n'.join(content_txt)
                # 组装新的内容标签
                outHtml = """<div class="BSHARE_POP blkContainerSblkCon clearfix blkContainerSblkCon_16" id="artibody">${++content++}</div>"""
                content_items = content_items.extract()
                content_items = ''.join(content_items)

                content_html = outHtml.replace('${++content++}', content_items)

                selector = Selector(text=content_html)
                # 解析文档中的所有图片url，然后替换成标识
                image_urls = []
                imgs = selector.xpath('descendant::img')

                for img in imgs:
                    # 图片可能放在src
                    image_url = img.xpath('@src').extract_first()
                    if image_url and image_url.startswith('http'):
                        self.logDao.info(u'得到图片：' + image_url)
                        image_urls.append({
                            'url': image_url,
                        })

                urlHash = EncryptUtil.md5(source_url.encode('utf8'))
                self.saveFile(urlHash, body)

                # 得到hashCode
                hash_code = self.checkDao.getHashCode(source_url)

                contentItem = ContentItem()
                contentItem['content_txt'] = content_txt
                contentItem['image_urls'] = image_urls
                contentItem['title'] = title
                contentItem['source_url'] = source_url
                contentItem['post_date'] = post_date
                contentItem['sub_channel'] = category
                contentItem['post_user'] = post_user
                contentItem['tags'] = tags
                contentItem['styles'] = styles
                contentItem['content_html'] = content_html
                contentItem['hash_code'] = hash_code
                contentItem['info_type'] = 1
                contentItem['src_source_id'] = 2
                # contentItem['src_account_id'] = 0
                contentItem['src_channel'] = '新浪科技'
                contentItem['src_ref'] = src_ref
                return contentItem

    def saveFile(self, title, content):
        filename = 'html/%s.html' % title
        with open(filename, 'wb') as f:
            f.write(content.encode("utf8"))
        self.log('Saved file %s' % filename)
