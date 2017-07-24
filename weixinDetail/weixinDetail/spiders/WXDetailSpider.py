# -*- coding: utf-8 -*-
import hashlib
import re

import demjson
import scrapy
import time
from scrapy import Selector

from ..db.WxSourceDao import WxSourceDao
from ..items import ContentItem

from libMe.db.LogDao import LogDao
from libMe.util import NetworkUtil
from libMe.util import EncodeUtil
from libMe.util import TimerUtil
from ..db.CheckDao import CheckDao


class WXDetailSpider(scrapy.Spider):
    name = 'wx_detail'
    download_delay = 20  # 基础间隔 0.5*download_delay --- 1.5*download_delays之间的随机数
    handle_httpstatus_list = [301, 302, 204, 206, 403, 404, 500]  # 可以处理重定向及其他错误码导致的 页面无法获取解析的问题

    def __init__(self, name=None, **kwargs):
        super(WXDetailSpider, self).__init__(name=None, **kwargs)
        self.count = 0
        self.wxSourceDao = WxSourceDao()
        self.request_stop = False
        self.request_stop_time = 0
        self.logDao = LogDao(self.logger,'weixin_list_detail')
        self.checkDao = CheckDao()

    def start_requests(self):
        # unKnow = ["didalive", "HIS_Technology", "CINNO_CreateMore", "ad_helper", "zhongduchongdu"]; 是搜索不到的
        # TODO..加上while可能有问题，有些可能抓不到
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
            # TODO..清除cookie
            # 获取源  可用有值
            sources = self.wxSourceDao.queryWxUrl(isRandom=True)

            for source in sources:
                if self.request_stop:
                    self.logDao.warn(u'出现被绊或者出现网络异常，退出循环')
                    # 当网络出现被绊的情况，就需要停止所有的请求等待IP更换
                    break
                (id, wx_name, wx_account, wx_url, wx_avatar, update_status, is_enable, update_time) = source
                # 进行页面访问
                newUrl = wx_url
                self.logDao.warn(u'进行抓取:' + newUrl)
                # TODO..no more duplicates will be shown (see DUPEFILTER_DEBUG to show all duplicates)
                yield scrapy.Request(url=newUrl,
                                     meta={'request_type': 'weixin_page_list',
                                           'wx_account': wx_account, 'source': source, 'wx_account_id':id},
                                     callback=self.parseArticleList, dont_filter=True)
                # 跑空线程2秒
                TimerUtil.sleep(2)

            # if self.request_stop:
            #     # 需要发起通知 进行重新拨号
            #     self.logDao.warn(u'发送重新拨号信号，请等待2分钟会尝试重新抓取')
            #     self.request_stop_time = time.time()
            #     pass
            # else:
            #     # 正常抓好之后，当前跑空线程40分钟，不影响一些还没请求完成的request
            #     if sources:
            #         self.logDao.info(u'请求了一轮了，但是可能还有没有请求完成，睡一会')
            #         self.logDao.info(u'')
            #         # TimerUtil.sleep(40 * 60)
            #         pass

    def parseArticleList(self, response):
        body = EncodeUtil.toUnicode(response.body)
        selector = Selector(text=body)
        title = selector.xpath('//title/text()').extract_first('').strip(u' ')
        isN = u"请输入验证码" == title
        if isN or response.status == 302:
            self.logDao.info(u'访问过多被禁止')
            # 更新状态为更新失败
            self.request_stop = True
        else:
            source = response.meta['source']
            wx_account = response.meta['wx_account']
            wx_account_id = response.meta['wx_account_id']
            self.logDao.info(u'开始解析列表:' + wx_account)
            # 进行解析
            articleJS = selector.xpath('//script/text()').extract()
            for js in articleJS:
                if 'var msgList = ' in js:
                    p8 = re.compile('var\s*msgList\s*=.*;')
                    matchList = p8.findall(js)
                    for match in matchList:
                        match = match.lstrip('var msgList = ').rstrip(';')
                        # 格式化
                        articles = demjson.decode(match) or {}
                        articles = articles['list'] or []
                        self.logDao.info(u'匹配到文章列表' + wx_account)
                        for article in articles:
                            app_msg_ext_info = article.get('app_msg_ext_info') or {}
                            desc = app_msg_ext_info.get('digest') or ''
                            title = app_msg_ext_info.get('title') or ''
                            # 如果存在则不抓取
                            if self.checkDao.checkExist(title, wx_account, 1):
                                self.logDao.info(u'已经存在' + wx_account + ':' + title + ':' + detailUrl)
                                continue
                            detailUrl = app_msg_ext_info['content_url'] or ''
                            detailUrl = "http://mp.weixin.qq.com" + detailUrl
                            detailUrl = detailUrl.replace("amp;", "")
                            self.logDao.info(u'抓取' + wx_account + ':' + title + ':' + detailUrl)
                            yield scrapy.Request(url=detailUrl,
                                                 meta={'request_type': 'weixin_detail', 'wx_account': wx_account,
                                                       "source": source, "title": title, 'wx_account_id':wx_account_id,
                                                       "source_url": detailUrl},
                                                 callback=self.parseArticle)

    def parseArticle(self, response):
        body = EncodeUtil.toUnicode(response.body)
        selector = Selector(text=body)
        title = selector.xpath('//title/text()').extract_first('').strip(u' ')
        isN = u"请输入验证码" == title
        if isN or response.status == 302:
            self.logDao.info(u'访问过多被禁止')
            # 更新状态为更新失败
            self.request_stop = True
        else:
            wx_account = response.meta['wx_account']
            title = response.meta['title']
            source_url = response.meta['source_url']
            wx_account_id = response.meta['wx_account_id']
            self.logDao.info(u'开始解析文章' + wx_account + ':' + title + ':' + source_url)
            self.logDao.info(u'开始解析文章：' + source_url)
            # 进行解析
            post_date = selector.xpath('//*[@id="post-date"]/text()').extract_first('')
            post_user = selector.xpath('//*[@id="post-user"]/text()').extract_first('')
            content_html = selector.xpath('//*[@id="js_content"]')
            if len(content_html):
                styles = ''  # 微信不需要样式
                # 去除内部不需要的标签
                content_items = content_html.xpath('*')

                # 得到纯文本
                content_txt = []
                for item in content_items:
                    # 文本
                    allTxt = item.xpath('.//text()').extract()
                    allTxt = ''.join(allTxt).replace('\t', '')
                    # 加入
                    content_txt.append(allTxt)
                content_txt = '\n'.join(content_txt)

                # 组装新的内容标签
                outHtml = """<div class="rich_media_content " id="js_content">${++content++}</div>"""
                content_items = content_items.extract()
                content_items = ''.join(content_items)

                content_html = outHtml.replace('${++content++}', content_items)

                selector = Selector(text=content_html)

                # 解析文档中的所有图片url，然后替换成标识
                image_urls = []
                imgs = selector.xpath('descendant::img')

                for img in imgs:
                    # 图片可能放在src 或者data-src
                    image_url = img.xpath('@src | @data-src').extract_first('')
                    if image_url and image_url.startswith('http'):
                        self.logDao.info(u'得到图片：' + image_url)
                        image_urls.append({
                            'url': image_url,
                        })
                self.logDao.info(wx_account + u'得到文章：' + title + ":" + post_date + ':' + post_user)
                self.logDao.info(u'得到文章：' + source_url)

                # 得到hashCode
                hash_code = self.checkDao.getHashCode(title, wx_account, 1)

                self.saveFile(hash_code, body)

                contentItem = ContentItem()
                contentItem['content_txt'] = content_txt
                contentItem['image_urls'] = image_urls
                contentItem['title'] = title
                contentItem['source_url'] = source_url
                contentItem['post_date'] = post_date
                contentItem['sub_channel'] = ''
                contentItem['post_user'] = post_user
                contentItem['tags'] = ''
                contentItem['styles'] = styles
                contentItem['content_html'] = content_html
                contentItem['hash_code'] = hash_code
                contentItem['info_type'] = 1
                contentItem['src_source_id'] = 1
                contentItem['src_account_id'] = wx_account_id
                contentItem['src_channel'] = '微信公众号'
                contentItem['src_ref'] = ''
                contentItem['wx_account'] = wx_account

                return contentItem

    def saveFile(self, title, content):
        filename = 'html/%s.html' % title
        with open(filename, 'wb') as f:
            f.write(content.encode("utf8"))
        self.log('Saved file %s' % filename)



"""
2017-07-21 17:47:12 [scrapy.pipelines.files] ERROR: File (unknown-error): Error processing file from <GET http://mmbiz.qpic.cn/mmbiz_png/fdj3u9OyUyE4JWLkEdTzCDY7vbzWcsNZDgcAia0rYhJZkbOIBW1rjZHb8icUut2w6Pb9CBotp5ic9wibMkKjWxM1ZA/0?wx_fmt=png> referred in <None>
Traceback (most recent call last):
  File "C:\Python27\lib\site-packages\scrapy\pipelines\files.py", line 356, in media_downloaded
    checksum = self.file_downloaded(response, request, info)
  File "C:\Python27\lib\site-packages\scrapy\pipelines\images.py", line 98, in file_downloaded
    return self.image_downloaded(response, request, info)
  File "C:\Python27\lib\site-packages\scrapy\pipelines\images.py", line 102, in image_downloaded
    for path, image, buf in self.get_images(response, request, info):
  File "C:\Python27\lib\site-packages\scrapy\pipelines\images.py", line 115, in get_images
    orig_image = Image.open(BytesIO(response.body))
  File "C:\Python27\lib\site-packages\PIL\Image.py", line 2452, in open
    % (filename if filename else fp))
IOError: cannot identify image file <cStringIO.StringI object at 0x00000000083D3360>

"""
