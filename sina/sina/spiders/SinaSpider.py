# -*- coding: utf-8 -*-
import json
import hashlib
import scrapy
from scrapy import Selector
from ..items import SinaContentItem

class SinaSpider(scrapy.Spider):
    name = 'sina'
    download_delay = 2

    def start_requests(self):
        urls = [
            'http://tech.sina.com.cn/t/2017-06-19/doc-ifyhfnqa4438329.shtml?cre=tianyi&mod=pctech&loc=7&r=0&doct=0&rfunc=13&tj=none&s=0&tr=1',
            'http://tech.sina.com.cn/d/v/2017-06-18/doc-ifyhfnqa4408344.shtml?cre=tianyi&mod=pctech&loc=4&r=25&doct=0&rfunc=13&tj=none&s=0&tr=25',
            'http://tech.sina.com.cn/i/2017-06-18/doc-ifyhfnqa4408196.shtml?cre=tianyi&mod=pctech&loc=1&r=25&doct=0&rfunc=13&tj=none&s=0&tr=25',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        selector = Selector(text=response.body)
        content = selector.xpath('//*[@id="artibody"]').extract()
        title = selector.xpath('//*[@id="main_title"]/text()').extract()
        publishTime = selector.xpath('//*[@id="page-tools"]/span/span[1]/text()').extract()
        fromSource = selector.xpath('//*[@id="page-tools"]/span/span[2]/text() | //*[@id="page-tools"]/span/span[2]/a/text()').extract()
        if len(fromSource):
            fromSource = ''.join(fromSource)
        else:
            fromSource = ''

        if len(publishTime):
            publishTime = publishTime[0]
        else:
            publishTime = ''

        if len(title):
            title = title[0]
        else:
            title = ''

        main = {
            'title': title,
            'publishTime': publishTime,
            'fromSource': fromSource,
            'content': content[0].encode('utf8')
        }
        self.saveFile(title[0], json.dumps(main, encoding="utf8", ensure_ascii=False))
        contentChilds = selector.xpath('//*[@id="artibody"]/child::*').extract()
        childItem = SinaContentItem()
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
            if 'img_wrapper' in child:
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
                content = curSelector.xpath('//p/text()').extract_first()

            contents.append({
                'type': type,
                'image_url': image_url,
                'content': content,
                'image_hash': image_hash
            })
        childItem['title'] = title
        childItem['publishTime'] = publishTime
        childItem['fromSource'] = fromSource
        childItem['image_urls'] = image_urls
        childItem['contents'] = contents
        yield childItem

    def saveFile(self, title, content):
        filename = '%s.html' % title
        with open(filename, 'wb') as f:
            f.write(content)
        self.log('Saved file %s' % filename)
