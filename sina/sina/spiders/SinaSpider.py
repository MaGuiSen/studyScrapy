# -*- coding: utf-8 -*-
import hashlib
import random
import json

import scrapy
from scrapy import Selector
from ..items import SinaContentItem
import demjson

isEnd = False


class SinaSpider(scrapy.Spider):
    name = 'sina'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    headers = {'User-Agent': user_agent}

    def start_requests(self):
        yield scrapy.Request(url='http://tech.sina.com.cn/it/2017-06-28/doc-ifyhmtcf3013516.shtml',
                             meta={'url': 'http://tech.sina.com.cn/it/2017-06-28/doc-ifyhmtcf3013516.shtml'},
                             callback=self.parseImg)

    def parseImg(self, response):
        contentItem = SinaContentItem()
        image_url = 'http://n.sinaimg.cn/tech/crawl/20170628/7Jxu-fyhneam5299458.jpg'
        m2 = hashlib.md5()
        m2.update(image_url)
        image_hash = m2.hexdigest()
        image_urls = [{
            'url': image_url,
            'hash': image_hash
        }]

        # image_url = 'http://ww1.1i580.com/img/sytest5-2.jpg'
        # m2 = hashlib.md5()
        # m2.update(image_url)
        # image_hash = m2.hexdigest()
        # image_urls.append({
        #     'url': image_url,
        #     'hash': image_hash
        # })
        contentItem['image_urls'] = image_urls
        return contentItem
    # def start_requests(self):
    #     url = 'http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=30&spec=&type=&ch=05&k=&offset_page=0&offset_num=0&num=60&asc=&page='
    #     page = 0
    #     while not isEnd:
    #         r = random.uniform(0, 1)
    #         page += 1
    #         newUrl = url + str(page)
    #         newUrl += ('&r=' + str(r))
    #         yield scrapy.Request(url=newUrl, meta={'url': newUrl}, callback=self.parseList)

    def parseList(self, response):
        url = response.meta['url']
        data = response.body.decode('gbk')
        data = data.lstrip('var jsonData = ').rstrip(';')
        # 格式化
        data = demjson.decode(data) or {}
        list = data['list'] or []
        for item in list:
            itemTime = item['time'] or 0
            # 判断时间多久以前的不爬
            contentItem = SinaContentItem()
            channel = item['channel'] or {}
            channelName = channel['title']
            contentItem['channelName'] = channelName

            contentItem['title'] = item['title']
            contentItem['url'] = item['url']
            print item['title']
            print item['url']
            callback = None

            # item['url'] = 'http://tech.sina.com.cn/i/2017-06-28/doc-ifyhmtcf3010090.shtml'
            if 'http://tech.sina.com.cn/zl/' in item['url']:
                callback = self.parseDetail2
            else:
                callback = self.parseDetail

            yield scrapy.Request(url=item['url'],
                                 meta={'contentItem': contentItem, 'url': item['url']},
                                 callback=callback)

    def parseDetail2(self, response):
        url = response.meta['url']
        contentItem = response.meta['contentItem']
        selector = Selector(text=response.body)
        content = selector.xpath('//*[@id="artibody"]').extract_first()
        title = selector.xpath('//*[@id="artibodyTitle"]/text()').extract_first() or ''
        publishTime = selector.xpath('//*[@id="pub_date"]/text()').extract_first() or ''
        publishTime = publishTime.replace('\r\n', '').strip(' ')
        fromSource = selector.xpath('//*[@id="media_name"]/a[1]/text()').extract_first()

        main = {
            'title': title,
            'publishTime': publishTime,
            'fromSource': fromSource,
            'content': content
        }
        m2 = hashlib.md5()
        m2.update(url.encode('utf8'))
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
                content =  curSelector.xpath('//p').xpath('string(.)').extract()

            contents.append({
                'type': type,
                'image_url': image_url,
                'content': content,
                'image_hash': image_hash
            })
        contentItem['title'] = title
        contentItem['publishTime'] = publishTime
        contentItem['fromSource'] = fromSource
        contentItem['image_urls'] = image_urls
        contentItem['contents'] = contents
        return contentItem

    def parseDetail(self, response):
        url = response.meta['url']
        contentItem = response.meta['contentItem']
        selector = Selector(text=response.body)
        content = selector.xpath('//*[@id="artibody"]').extract_first()
        title = selector.xpath('//*[@id="main_title"]/text()').extract_first() or ''
        publishTime = selector.xpath('//*[@id="page-tools"]/span/span[1]/text()').extract_first() or ''
        fromSource = selector.xpath(
            '//*[@id="page-tools"]/span/span[2]/text() | //*[@id="page-tools"]/span/span[2]/a/text()').extract()
        if len(fromSource):
            fromSource = ''.join(fromSource)
        else:
            fromSource = ''

        main = {
            'title': title,
            'publishTime': publishTime,
            'fromSource': fromSource,
            'content': content
        }
        m2 = hashlib.md5()
        m2.update(url.encode('utf8'))
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
        contentItem['publishTime'] = publishTime
        contentItem['fromSource'] = fromSource
        contentItem['image_urls'] = image_urls
        contentItem['contents'] = contents
        return contentItem

    def saveFile(self, title, content):
        filename = 'html/%s.html' % title
        with open(filename, 'wb') as f:
            f.write(content.encode('utf8'))
        self.log('Saved file %s' % filename)
