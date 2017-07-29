# -*- coding: utf-8 -*-
import json
import re

import demjson
import scrapy
import time
from scrapy import Selector

from libMe.db.LogDao import LogDao
from libMe.util import EncodeUtil
from libMe.util import NetworkUtil
from libMe.util import TimerUtil
from libMe.util import CssUtil
from ..db.CheckDao import CheckDao
from ..db.WxSourceDao import WxSourceDao
from ..items import ContentItem
from libMe.db.DataMonitorDao import DataMonitorDao


class WXDetailSpider(scrapy.Spider):
    name = 'wx_detail'
    download_delay = 15  # 基础间隔 0.5*download_delay --- 1.5*download_delays之间的随机数
    handle_httpstatus_list = [301, 302, 204, 206, 403, 404, 500]  # 可以处理重定向及其他错误码导致的 页面无法获取解析的问题

    def __init__(self, name=None, **kwargs):
        super(WXDetailSpider, self).__init__(name=None, **kwargs)
        self.count = 0
        self.wxSourceDao = WxSourceDao()
        self.logDao = LogDao(self.logger, 'weixin_list_detail')
        self.checkDao = CheckDao()
        self.dataMonitor = DataMonitorDao()
        self.wxSources = []

    def close(spider, reason):
        spider.saveStatus('stop')
        spider.dataMonitor.updateTotal('weixin_total')
        for source in spider.wxSources:
            (id, wx_name, wx_account, wx_url, wx_avatar, update_status, is_enable, update_time) = source
            spider.dataMonitor.updateTotal('weixin_account_total', account=wx_account)


    def start_requests(self):
        # unKnow = ["didalive", "HIS_Technology", "ad_helper", "zhongduchongdu"]; 是搜索不到的
        # TODO..加上while可能有问题，有些可能抓不到
        # while True:
        # 如果正在爬，就不请求
        status = self.getStatus()
        if status == 'running':
            return
        self.saveStatus('running')
        # 检测网络
        while not NetworkUtil.checkNetWork():
            # 20s检测一次
            TimerUtil.sleep(20)
            self.logDao.warn(u'检测网络不可行')
            # continue

        # 检测服务器
        while not NetworkUtil.checkService():
            # 20s检测一次
            TimerUtil.sleep(20)
            self.logDao.warn(u'检测服务器不可行')
            # continue

        # 获取源  可用有值
        sources = self.wxSourceDao.queryWxUrl(isRandom=True)
        self.wxSources = sources
        for source in sources:
            (id, wx_name, wx_account, wx_url, wx_avatar, update_status, is_enable, update_time) = source
            # 进行页面访问
            newUrl = wx_url
            self.logDao.warn(u'进行抓取:' + newUrl)
            yield scrapy.Request(url=newUrl,
                                 meta={'request_type': 'weixin_page_list',
                                       'source_url': newUrl,
                                       'wx_account': wx_account, 'source': source, 'wx_account_id': id},
                                 callback=self.parseArticleList, dont_filter=True)

    def parseArticleList(self, response):
        body = EncodeUtil.toUnicode(response.body)
        selector = Selector(text=body)
        source_url = response.meta['source_url']
        title = selector.xpath('//title/text()').extract_first('').strip(u' ')
        isN = u"请输入验证码" == title
        if isN or response.status == 302:
            self.logDao.info(u'访问过多被禁止,重新拨号')
            # 获取Ip # 同时空线程30s
            NetworkUtil.getNewIp()
            TimerUtil.sleep(50)
            NetworkUtil.openWebbrowser(source_url)
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
                                self.logDao.info(u'已经存在' + wx_account + ':' + title)
                                continue
                            detailUrl = app_msg_ext_info['content_url'] or ''
                            detailUrl = "http://mp.weixin.qq.com" + detailUrl
                            detailUrl = detailUrl.replace("amp;", "")
                            self.logDao.info(u'抓取' + wx_account + ':' + title + ':' + detailUrl)
                            if not detailUrl:
                                continue
                            yield scrapy.Request(url=detailUrl,
                                                 meta={'request_type': 'weixin_detail', 'wx_account': wx_account,
                                                       "source": source, "title": title, 'wx_account_id': wx_account_id,
                                                       "source_url": detailUrl},
                                                 callback=self.parseArticle)

    def parseArticle(self, response):
        body = EncodeUtil.toUnicode(response.body)
        selector = Selector(text=body)
        title = selector.xpath('//title/text()').extract_first('').strip(u' ')
        source_url = response.meta['source_url']
        isN = u"请输入验证码" == title
        if isN or response.status == 302:
            self.logDao.info(u'访问过多被禁止,重新拨号')
            # 获取Ip # 同时空线程30s
            NetworkUtil.getNewIp()
            TimerUtil.sleep(50)
            NetworkUtil.openWebbrowser(source_url)
        else:
            wx_account = response.meta['wx_account']
            title = response.meta['title']
            source_url = response.meta['source_url']
            wx_account_id = response.meta['wx_account_id']
            self.logDao.info(u'开始解析文章' + wx_account + ':' + title + ':' + source_url)
            self.logDao.info(u'开始解析文章：' + source_url)
            # 进行解析
            post_date = selector.xpath('//*[@id="post-date"]/text()').extract_first('')

            try:
                post_date = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(post_date, "%Y-%m-%d"))
            except Exception:
                pass

            styles = selector.xpath('//style/text()').extract()
            styles = CssUtil.compressCss(styles).replace('\'', '"').replace('\\', '\\\\')
            styles = CssUtil.clearUrl(styles)
            styles = CssUtil.clearBackgroundColor(styles, ['#f3f3f3'])

            post_user = selector.xpath('//*[@id="post-user"]/text()').extract_first('')
            content_html = selector.xpath('//*[@id="js_content"]')
            if not len(content_html):
                self.logDao.info(u'不存在内容：' + source_url)
                return
            # 去除内部不需要的标签
            content_items = content_html.xpath('*')
            if not len(content_items):
                self.logDao.info(u'不存在内容：' + source_url)
                return

            # content_items_new = []
            # for item in content_items:
            #     itemStr = item.extract()
            #     if u'订阅微信' in itemStr:
            #         continue
            #     content_items_new.append(item)
            # content_items = content_items_new

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

            # 得到hashCode1
            hash_code = self.checkDao.getHashCode(title, wx_account, 1)

            self.saveFile(hash_code, body)

            # 去除 image 的 alt title
            selector = Selector(text=content_html)
            imgAltTitles = selector.xpath('//img/@alt|//img/@title').extract()
            # 处理提示块img的 alt title, 关注//img/@alt|//img/@title
            for imgAltTitle in imgAltTitles:
                if imgAltTitle.strip(' '):
                    content_html = content_html.replace(imgAltTitle, '')

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

    def getStatus(self):
        try:
            with open("catchStatus.json", 'r') as load_f:
                aa = json.load(load_f)
                return aa.get('status')
        finally:
            if load_f:
                load_f.close()

    def saveStatus(self, status):
        try:
            with open("catchStatus.json", "w") as f:
                json.dump({'status': status}, f)
        finally:
            if f:
                f.close()


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
