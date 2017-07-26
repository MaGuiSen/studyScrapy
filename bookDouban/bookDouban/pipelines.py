# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
from scrapy import Request
from libMe.util import EncryptUtil
from scrapy.pipelines.images import ImagesPipeline

from libMe.util import TimerUtil
from libMe.util import FileUtil
from libMe.util.FileUtil import UploadUtil


class MysqlPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        print 'heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
        pass


class MyImagesPipeline(ImagesPipeline):
    def __init__(self, store_uri, download_func=None, settings=None):
        super(MyImagesPipeline, self).__init__(store_uri, download_func=None, settings=None)
        botName = 'weixin'  # 注意需要更改。。。

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url['url'])

    def item_completed(self, results, item, info):
        # [{path:'', url:''}]
        image_urls = []
        for ok, x in results:
            if ok:
                url = x['url']
                path = x['path']
        return item


class MyImageDownLoad(object):
    @classmethod
    def from_settings(cls, settings):
        savePath = settings['IMAGES_STORE']
        botName = settings['BOT_NAME']
        return cls(botName, savePath)  # 相当于dbpool付给了这个类，self中可以得到

    def __init__(self, botName, savePath):
        self.botName = botName
        self.savePath = savePath

    def getImageUrlNew(self, ok, url, path=''):
        image_url_new = {
            'ok': ok,
            'x': {
                'url': url,
                'path': path
            }
        }
        return image_url_new

    def process_item(self, item, spider):
        image_urls = []
        for image_url in item['image_urls']:
            url = image_url.get('url')
            urlHash = EncryptUtil.md5(url)
            path = 'full/' + str(urlHash) + '.jpg'
            detailPath = self.savePath + '/' + path
            # 创建目录
            saveDir = self.savePath+'/full'
            if not FileUtil.dirIsExist(saveDir):
                FileUtil.createDir(saveDir)

            if FileUtil.fileIsExist(detailPath):
                image_url_new = {
                    'ok': True,
                    'x': {
                        'url': url,
                        'path': path
                    }
                }
            else:
                try:
                    fileResponse = requests.get(url, timeout=10)
                    req_code = fileResponse.status_code
                    req_msg = fileResponse.reason
                    if req_code == 200:
                        open(detailPath, 'wb').write(fileResponse.content)
                        image_url_new = {
                            'ok': True,
                            'x': {
                                'url': url,
                                'path': path
                            }
                        }
                    else:
                        print '下载图片失败', url
                        image_url_new = {
                            'ok': False,
                            'x': {
                                'url': url,
                            }
                        }
                except Exception, e:
                    print e
                    print '下载图片失败', url
                    image_url_new = {
                        'ok': False,
                        'x': {
                            'url': url,
                        }
                    }
            image_urls.append(image_url_new)
            # 空转2s
            TimerUtil.sleep(2)

        for image_url in image_urls:
            ok = image_url.get('ok', False)
            if ok:
                x = image_url.get('x', {})
                print ok, x['url']
                print ok, x['path']
                # 上传照片
            else:
                print 'error'
        item['image_urls'] = image_urls
