# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy import Selector
from libMe.db.LogDao import LogDao
from libMe.util import CssUtil
from libMe.util import EncryptUtil
from libMe.util import NetworkUtil
from libMe.util import EncodeUtil
from libMe.util import TimerUtil
from ..db.CheckDao import CheckDao
from ..items import ContentItem
from libMe.db.DataMonitorDao import DataMonitorDao


class DetailSpider(scrapy.Spider):
    name = 'diyicaijing_detail'
    # 基础间隔 0.5*download_delay --- 1.5*download_delays之间的随机数
    download_delay = 2.5
    # 可以处理重定向及其他错误码导致的 页面无法获取解析的问题
    handle_httpstatus_list = [301, 302, 204, 206, 403, 404, 500]

    def __init__(self, name=None, **kwargs):
        super(DetailSpider, self).__init__(name=None, **kwargs)
        self.count = 0
        self.request_stop = False
        self.request_stop_time = 0
        self.logDao = LogDao(self.logger, 'diyicaijing_list_detail')
        self.checkDao = CheckDao()
        # 用于缓存css
        self.css = {
            'hash': 'style'
        }
        self.dataMonitor = DataMonitorDao()
        self.isRunningStop = False

    def close(spider, reason):
        if not spider.isRunningStop:
            # 如果启动爬虫时候，还有未完成的抓取，此时不应该设置状态为停止，反之
            spider.saveStatus('stop')
        # spider.dataMonitor.updateTotal('diyicaijing_total')
        pass

    def start_requests(self):
        # 如果正在爬，就不请求
        status = self.getStatus()
        if status == 'running':
            self.isRunningStop = True
            return
        self.saveStatus('running')

        # 检测网络
        while not NetworkUtil.checkNetWork():
            # 20s检测一次
            TimerUtil.sleep(20)
            self.logDao.warn(u'检测网络不可行')

        # 检测服务器
        while not NetworkUtil.checkService():
            # 20s检测一次
            TimerUtil.sleep(20)
            self.logDao.warn(u'检测服务器不可行')

        # 进行页面访问
        newUrl = 'http://www.yicai.com/news/'
        self.logDao.warn(u'进行抓取列表:' + newUrl)
        yield scrapy.Request(url=newUrl,
                             meta={'request_type': 'diyicaijing_page_list', 'url': newUrl},
                             callback=self.parseArticleList, dont_filter=True)

    # TODO...还没有遇到被禁止的情况
    def parseArticleList(self, response):
        body = EncodeUtil.toUnicode(response.body)
        if False:
            self.logDao.info(u'访问过多被禁止')
        else:
            self.logDao.info(u'开始解析列表')
            selector = Selector(text=body)
            articles = selector.xpath('//dl[@class="f-cb dl-item"]')
            for article in articles:
                source_url = article.xpath('.//h3[@class="f-ff1 f-fwn f-fs22"]/a/@href').extract_first('')
                title = article.xpath('.//h3[@class="f-ff1 f-fwn f-fs22"]/a/text()').extract_first('')
                sub_channel = article.xpath('.//h5[@class="f-ff1 f-fwn f-fs14"]/a/text()').extract_first('')
                post_date = article.xpath('.//h4[@class="f-ff1 f-fwn f-fs14"]/span/text()').extract_first('')

                if not source_url:
                    continue

                if self.checkDao.checkExist(source_url):
                    self.logDao.info(u'文章已经存在' + title + ':' + post_date + ':' + source_url)
                    continue
                self.logDao.info(u'抓取文章' + title + ':' + post_date + ':' + source_url)

                yield scrapy.Request(url=source_url,
                                     meta={'request_type': 'diyicaijing_detail', "title": title, 'post_date': post_date,
                                           "source_url": source_url,
                                           'sub_channel': sub_channel},
                                     callback=self.parseArticle)

    def parseArticle(self, response):
        body = EncodeUtil.toUnicode(response.body)
        if False:
            self.logDao.info(u'访问过多被禁止')
        else:
            sub_channel = response.meta['sub_channel']
            title = response.meta['title']
            post_date = response.meta['post_date']
            source_url = response.meta['source_url']
            self.logDao.info(u'开始解析文章:' + title + ':' + post_date + ':' + source_url)

            selector = Selector(text=body)

            # 页面存在的css
            pageStyles = selector.xpath('//style/text()').extract()
            # 得到样式
            styleUrls = selector.xpath('//link[@rel="stylesheet"]/@href').extract()
            styleList = []
            for styleUrl in styleUrls:
                if styleUrl.startswith('//'):
                    styleUrl = 'http:' + styleUrl
                # 得到hash作为key
                styleUrlHash = EncryptUtil.md5(styleUrl)
                if not self.css.get(styleUrlHash):
                    # 不存在则去下载 并保存
                    self.css[styleUrlHash] = CssUtil.downLoad(styleUrl)
                styleList.append(self.css[styleUrlHash])
            styleList = pageStyles + styleList
            styles = CssUtil.compressCss(styleList).replace('\'', '"').replace('\\', '\\\\')

            # 替换样式里面的链接
            styles = CssUtil.clearUrl(styles)

            tags = selector.xpath('//meta[@name="keywords"]/@content').extract_first('')

            src_ref = selector.xpath('//*[@class="m-title f-pr"]/h2[@class="f-ff1 f-fwn f-fs14"]/i//text()').extract_first('')

            content_html = selector.xpath('//div[@class="m-text"]')
            if not len(content_html):
                self.logDao.info(u'不存在内容：' + source_url)
                return
            # 去除内部不需要的标签
            # 完整案例：content_html.xpath('*[not(boolean(@class="entHdPic" or @class="ep-source cDGray")) and not(name(.)="script")]').extract()
            content_items = content_html.xpath('*[not(name(.)="script") and not(name(.)="style")  and not(name(.)="iframe")]')
            if not len(content_items):
                self.logDao.info(u'不存在内容：' + source_url)
                return

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
            outHtml = """<div class="m-text">${++content++}</div>"""
            content_items = content_items.extract()
            content_items = ''.join(content_items)

            content_html = outHtml.replace('${++content++}', content_items)

            selector = Selector(text=content_html)
            # 解析文档中的所有图片url，然后替换成标识
            image_urls = []
            imgs = selector.xpath('descendant::img')

            for img in imgs:
                # 图片可能放在src 或者data-src
                image_url_base = img.xpath('@src').extract_first('')
                if image_url_base.startswith('//'):
                    image_url = 'http:' + image_url_base
                else:
                    image_url = image_url_base
                if image_url and image_url.startswith('http'):
                    self.logDao.info(u'得到图片：' + image_url)
                    image_urls.append({
                        'url': image_url,
                    })
                    content_html = content_html.replace(image_url_base, image_url)

            urlHash = EncryptUtil.md5(source_url.encode('utf8'))
            self.saveFile(urlHash, body)

            # 得到hashCode
            hash_code = self.checkDao.getHashCode(source_url)

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
            contentItem['sub_channel'] = sub_channel
            contentItem['post_user'] = ''
            contentItem['tags'] = tags
            contentItem['styles'] = styles
            contentItem['content_html'] = content_html
            contentItem['hash_code'] = hash_code
            contentItem['info_type'] = 1
            contentItem['src_source_id'] = 9
            # contentItem['src_account_id'] = 0
            contentItem['src_channel'] = '第一财经'
            contentItem['src_ref'] = src_ref
            return contentItem

    def saveFile(self, title, content):
        filename = 'html/%s.html' % title
        with open(filename, 'wb') as f:
            f.write(content.encode("utf8"))
        self.log('Saved file %s' % filename)

    def getStatus(self):
        loadF = None
        try:
            with open("catchStatus.json", 'r') as loadF:
                aa = json.load(loadF)
                return aa.get('status')
        finally:
            if loadF:
                loadF.close()

    def saveStatus(self, status):
        loadF = None
        try:
            with open("catchStatus.json", "w") as loadF:
                json.dump({'status': status}, loadF)
        finally:
            if loadF:
                loadF.close()
