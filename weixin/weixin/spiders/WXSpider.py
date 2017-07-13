# -*- coding: utf-8 -*-
import hashlib
import re

import demjson
import scrapy
from scrapy import Selector

isEnd = False


class WXSpider(scrapy.Spider):
    name = 'wechat'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    download_delay = 20

    def __init__(self, name=None, **kwargs):
        super(WXSpider, self).__init__(name=None, **kwargs)
        self.count = 0;
    def start_requests(self):
        weChatName = [
            "BizNext",
            "QuestMobile",
            "DataBureau",
            "bi_chinese",
            "CL-Internet",
            "qqtech",
            "Talkingdata",
            "TechCrunchChina",
            "PerfectValley",
            "techweb",
            "sykong_com",
            "youxiputao",
            "GameLook_News",
            "sousuoshusheng",
            "aliresearch",
            "cnecclub",
            "zhhjrwh",
            "newrankcn",
            "almosthuman2014",
            "aitechtalk",
            "SemiconNews",
            "icbank",
            "EEinsights",
            "IDC_CN",
            "investguru",
            "gh_5906530d307c",
            "yaohaotixy",
            "dashuju36",
            "hhwwnnss",
            "ilovedonews",
            "DataScientistUnion",
            "huxiu_com"
        ]
        unKnow = ["didalive", "HIS_Technology", "CINNO_CreateMore", "ad_helper", "zhongduchongdu"];

        url = 'http://weixin.sogou.com/weixin?type=1&s_from=input&ie=utf8&_sug_=n&_sug_type_=&query='
        for name in weChatName:
            self.count += 1
            newUrl = url + name
            print name
            yield scrapy.Request(url=newUrl, meta={'url': newUrl, 'count':self.count, 'name': name, 'wechatNum': name}, callback=self.parseList)
        # http://mp.weixin.qq.com/profile?src=3&timestamp=1499763652&ver=1&signature=KLT6ktu9rfezVeeLGvpIdWXukt757RDgCymg7L1wR2wd*Ajl26L69Uc6xPJUxOBL2bb0nPcShFKpGqnMTfKLVA==
        for name in unKnow:
            newUrl = url + name

    def parseList(self, response):
        name = response.meta['name']
        count = response.meta['count']
        if "您的访问过于频繁" in response.body:
            print count, name, "被禁止"
        else:
            print count, name, "没有被禁止"
            url = response.meta['url']
            wechatNum = response.meta['wechatNum']
            selector = Selector(text=response.body)
            results = selector.xpath('//*[@id="main"]/div[4]/ul/li')
            print "列表长度", len(results)
            for result in results:
                name = result.xpath('//*[@id="sogou_vr_11002301_box_0"]/div/div[2]/p[1]/a/text()').extract_first()
                wechatNum_ = result.xpath('//p[@class="info"]/label/text()').extract_first()
                articleListUrl = result.xpath('//p[@class="tit"]/a/@href').extract_first()
                if wechatNum_ == wechatNum:
                    print "被抓", wechatNum_
                    yield scrapy.Request(url=articleListUrl, meta={'wechatNum': wechatNum}, callback=self.parseArticleList)
                    break

    def parseArticleList(self, response):
        selector = Selector(text=response.body)
        wechatNum = response.meta['wechatNum']
        name = selector.xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div/strong/text()').extract_first()
        listJS = selector.xpath('//script/text()').extract()
        for js in listJS:
            if "var msgList = " in js:
                p8 = re.compile('var\s*msgList\s*=.*;')
                matchList = p8.findall(js)
                for match in matchList:
                    match = match.lstrip("var msgList = ").rstrip(";")
                    # 格式化
                    articles = demjson.decode(match) or {}
                    articles = articles["list"] or []
                    print "格式化", "wechatNum", wechatNum, "name", name, "articles", len(articles)
                    for article in articles:
                        app_msg_ext_info = article['app_msg_ext_info'] or {}
                        detailUrl = app_msg_ext_info['content_url'] or ''
                        title = app_msg_ext_info['digest'] or ''
                        detailUrl = "http://mp.weixin.qq.com" + detailUrl
                        detailUrl = detailUrl.replace("amp;", "");
                        print wechatNum, name, title
                        yield scrapy.Request(url=detailUrl,
                                             meta={'wechatNum': wechatNum, "name": name, "title": title, "detailUrl": detailUrl},
                                             callback=self.parseArticle)
                        break
                    break

    def parseArticle(self, response):
        selector = Selector(text=response.body)
        wechatNum = response.meta['wechatNum']
        name = response.meta['name']
        title = response.meta['title']
        detailUrl = response.meta['detailUrl']
        post_date = selector.xpath('//*[@id="post-date"]/text()').extract_first()
        post_user = selector.xpath('//*[@id="post-user"]/text()').extract_first()
        content = selector.xpath('//*[@id="js_content"]')
        page = selector.xpath('//*[@id="img-content"]')
        print post_date, post_user, title

        m2 = hashlib.md5()
        m2.update(title.encode('utf8'))
        title_hash = m2.hexdigest()

        self.saveFile(title_hash, page.extract_first())

    def saveFile(self, title, content):
        filename = 'html/%s.html' % title
        with open(filename, 'wb') as f:
            f.write(content.encode("utf8"))
        self.log('Saved file %s' % filename)
