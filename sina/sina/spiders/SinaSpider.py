# -*- coding: utf-8 -*-
import hashlib
import random
import json

import scrapy
import time
from scrapy import Selector

from libMe.db.LogDao import LogDao
from libMe.util import NetworkUtil
from libMe.util import TimerUtil

from ..items import ContentItem
import demjson


class SinaSpider(scrapy.Spider):
    name = 'sina'
    download_delay = 20  # 基础间隔 0.5*download_delay --- 1.5*download_delays之间的随机数
    handle_httpstatus_list = [301, 302, 204, 206, 403, 404, 500]  # 可以处理重定向及其他错误码导致的 页面无法获取解析的问题

    def __init__(self, name=None, **kwargs):
        super(SinaSpider, self).__init__(name=None, **kwargs)
        self.count = 0
        self.request_stop = False
        self.request_stop_time = 0
        self.logDao = LogDao(self.logger, 'sina_detail')

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
        url = 'http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=30&spec=&type=&ch=05&k' \
              '=&offset_page=0&offset_num=0&num=60&asc=&page='

        for page in range(0, 11):
            if self.request_stop:
                self.logDao.warn(u'出现被绊或者出现网络异常，退出循环')
                # 当网络出现被绊的情况，就需要停止所有的请求等待IP更换
                break
            r = random.uniform(0, 1)
            newUrl = url + str(page)
            newUrl += ('&r=' + str(r))
            self.logDao.info(u"开始抓取列表：" + newUrl)
            yield scrapy.Request(url=newUrl, meta={'url': newUrl}, callback=self.parseList)
            # 跑空线程2秒
            TimerUtil.sleep(2)

        if self.request_stop:
            # 需要发起通知 进行重新拨号
            self.logDao.warn(u'发送重新拨号信号，请等待2分钟会尝试重新抓取')
            self.request_stop_time = time.time()
            pass
        else:
            # 正常抓好之后，当前跑空线程10分钟，不影响一些还没请求完成的request
            self.logDao.info(u'请求了一轮了，但是可能还有没有请求完成，睡一会10分钟')
            TimerUtil.sleep(10 * 60)
            pass

    # TODO。。还没有找到被禁止的情况
    def parseList(self, response):
        url = response.meta['url']
        data = response.body.decode('gbk')
        data = data.lstrip('var jsonData = ').rstrip(';')
        # 格式化
        data = demjson.decode(data) or {}
        list = data['list'] or []
        self.logDao.info(u"解析列表：" + url)
        for item in list:
            itemTime = item['time'] or 0
            contentItem = ContentItem()
            channel = item['channel'] or {}
            channel_name = channel['title']
            contentItem['channel_name'] = channel_name

            contentItem['title'] = item['title']
            contentItem['source_url'] = item['url']

            # 暂时知道 两种不同的文章界面
            if 'http://tech.sina.com.cn/zl/' in item['url']:
                callback = self.parseDetail2
            else:
                callback = self.parseDetail

            self.logDao.info(u"开始抓取文章：" + item['url'])
            yield scrapy.Request(url=item['url'],
                                 meta={'contentItem': contentItem, 'source_url': item['url']},
                                 callback=callback)

    def parseDetail2(self, response):
        source_url = response.meta['source_url']
        contentItem = response.meta['contentItem']
        selector = Selector(text=response.body)
        pl_main_content = selector.xpath('//*[@id="J_Article_Wrap"]').extract_first()
        title = selector.xpath('//*[@id="artibodyTitle"]/text()').extract_first() or ''
        post_date = selector.xpath('//*[@id="pub_date"]/text()').extract_first() or ''
        post_date = post_date.replace('\r\n', '').strip(' ')
        post_user = selector.xpath('//*[@id="media_name"]/a[1]/text()').extract_first()
        tags = selector.xpath('//p[@class="art_keywords"]/a/text()').extract() or []
        tags = ','.join(tags)

        main = {
            'title': title,
            'post_date': post_date,
            'post_user': post_user,
            'pl_main_content': pl_main_content,
            'tags': tags
        }
        m2 = hashlib.md5()
        m2.update(source_url.encode('utf8'))
        urlHash = m2.hexdigest()
        self.saveFile(urlHash, json.dumps(main, encoding="utf8", ensure_ascii=False))
        contentChilds = selector.xpath('//*[@id="artibody"]/child::*').extract()

        image_url = ''
        content = ''
        type = ''
        image_hash = ''
        contents = []
        image_urls = []
        for child in contentChilds:
            image_url = ''
            content = ''
            type = ''
            image_hash = ''
            curSelector = Selector(text=child)
            # 特别的网站 http://tech.sina.com.cn/d/2017-06-28/doc-ifyhmtrw4294617.shtml
            # http://tech.sina.com.cn/zl/post/detail/i/2017-06-28/pid_8511506.htm
            if 'img_wrapper' in child or 'img' in child:
                # 有的页面没有 img_wrapper,只有img
                # 图片形
                # 获取图片摘要，下载图片，替换图片名称
                type = 'img'
                image_url = curSelector.xpath('//img/@src').extract_first()
                content = curSelector.xpath('//span/text()').extract_first()
                # image_url = image_url[0] if image_url and len(image_url) else ''

                m2 = hashlib.md5()
                m2.update(image_url)
                image_hash = m2.hexdigest()
                image_urls.append({
                    'url': image_url,
                    'hash': image_hash
                })
            elif 'strong' in child:
                # 标题形
                type = 'title'
                content = curSelector.xpath('//strong/text()').extract_first()

            elif 'gb2312, simkai;' in child:
                # 小描述形
                type = 'shortInfo'
                content = curSelector.xpath('//span/text()').extract_first()

            elif '"pictext" align="center"' in child:
                # 小描述形
                type = 'centerContent'
                content = curSelector.xpath('//p/text()').extract_first()

            else:
                # 默认
                type = 'normalContent'
                content = curSelector.xpath('//p').xpath('string(.)').extract()

            contents.append({
                'type': type,
                'image_url': image_url,
                'content': content,
                'image_hash': image_hash
            })
        contentItem['title'] = title
        contentItem['post_date'] = post_date
        contentItem['post_user'] = post_user
        contentItem['image_urls'] = image_urls
        contentItem['page_content'] = contents
        contentItem['tags'] = tags
        return contentItem

    def parseDetail(self, response):
        source_url = response.meta['source_url']
        contentItem = response.meta['contentItem']
        selector = Selector(text=response.body)
        pl_main_content = selector.xpath('//*[@id="pl_main_content"]').extract_first()
        title = selector.xpath('//*[@id="main_title"]/text()').extract_first() or ''
        post_date = selector.xpath('//*[@id="page-tools"]/span/span[1]/text()').extract_first() or ''
        post_user = selector.xpath(
            '//*[@id="page-tools"]/span/span[2]/text() | //*[@id="page-tools"]/span/span[2]/a/text()').extract()
        tags = selector.xpath('//p[@class="art_keywords"]/a/text()').extract() or []
        tags = ','.join(tags)

        if len(post_user):
            post_user = ''.join(post_user)
        else:
            post_user = ''

        main = {
            'title': title,
            'post_date': post_date,
            'post_user': post_user,
            'pl_main_content': pl_main_content,
            'tags': tags
        }
        m2 = hashlib.md5()
        m2.update(source_url.encode('utf8'))
        urlHash = m2.hexdigest()
        self.saveFile(urlHash, json.dumps(main, encoding="utf8", ensure_ascii=False))
        contentChilds = selector.xpath('//*[@id="artibody"]/child::*').extract()

        image_url = ''
        content = ''
        type = ''
        image_hash = ''
        contents = []
        image_urls = []
        for child in contentChilds:
            image_url = ''
            content = ''
            type = ''
            image_hash = ''
            curSelector = Selector(text=child)
            # 特别的网站 http://tech.sina.com.cn/d/2017-06-28/doc-ifyhmtrw4294617.shtml
            # http://tech.sina.com.cn/zl/post/detail/i/2017-06-28/pid_8511506.htm
            if 'img_wrapper' in child or 'img' in child:
                # 有的页面没有 img_wrapper,只有img
                # 图片形
                # 获取图片摘要，下载图片，替换图片名称
                type = 'img'
                image_url = curSelector.xpath('//img/@src').extract_first()
                content = curSelector.xpath('//span/text()').extract_first()
                # image_url = image_url[0] if image_url and len(image_url) else ''

                m2 = hashlib.md5()
                m2.update(image_url)
                image_hash = m2.hexdigest()
                image_urls.append({
                    'url': image_url,
                    'hash': image_hash
                })
            elif 'strong' in child:
                # 标题形
                type = 'title'
                content = curSelector.xpath('//strong/text()').extract_first()

            elif 'font-family: KaiTi_GB2312, KaiTi;' in child:
                # 小描述形
                type = 'shortInfo'
                content = curSelector.xpath('//span/text()').extract_first()

            elif '"pictext" align="center"' in child:
                # 小描述形
                type = 'centerContent'
                content = curSelector.xpath('//p/text()').extract_first()

            else:
                # 默认
                type = 'normalContent'
                content = curSelector.xpath('//p').xpath('string(.)').extract()

            contents.append({
                'type': type,
                'image_url': image_url,
                'content': content,
                'image_hash': image_hash
            })
        contentItem['title'] = title
        contentItem['post_date'] = post_date
        contentItem['post_user'] = post_user
        contentItem['image_urls'] = image_urls
        contentItem['page_content'] = contents
        contentItem['tags'] = tags
        return contentItem

    def saveFile(self, title, content):
        filename = 'html/%s.json' % title
        with open(filename, 'wb') as f:
            f.write(content.encode('utf8'))
        self.log('Saved file %s' % filename)
