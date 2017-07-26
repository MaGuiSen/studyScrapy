# -*- coding: utf-8 -*-
import os
import threading
import requests


class FileDownLoadThread(threading.Thread):
    def __init__(self, book_id, path_fileName, loadUrl):
        threading.Thread.__init__(self)
        self.book_id = book_id
        self.path_fileName = path_fileName
        self.loadUrl = loadUrl
        self.currFilePath = os.path.dirname(__file__)

    def run(self):
        try:
            fileResponse = requests.get(self.loadUrl, timeout=5)
            req_code = fileResponse.status_code
            req_msg = fileResponse.reason
            print "图片下载返回状态 ", req_code, " 返回状态消息 ", req_msg
            if req_code == 200:
                open(self.currFilePath + self.path_fileName, 'wb').write(fileResponse.content)
                print self.book_id, "图片下载成功", self.loadUrl
            else:
                print self.book_id, "图片下载出错", self.loadUrl
        except Exception, e:
            print e
            print self.book_id, "图片下载出错Exception", self.loadUrl


thread1 = FileDownLoadThread(1, "/img/12222222.jpg", "http://n.sinaimg.cn/tech/crawl/20170725/nFQc-fyiiahz0277318.jpg")
thread1.start()


# def downloadImage(image_urls):
    # for image_url in image_urls:
    #     try:
    #         fileResponse = requests.get(image_url, timeout=10)
    #         req_code = fileResponse.status_code
    #         req_msg = fileResponse.reason
    #         print "图片下载返回状态 ", req_code, " 返回状态消息 ", req_msg
    #         if req_code == 200:
    #             open(self.currFilePath + self.path_fileName, 'wb').write(fileResponse.content)
    #             print self.book_id, "图片下载成功", self.loadUrl
    #         else:
    #             print self.book_id, "图片下载出错", self.loadUrl
    #     except Exception, e:
    #         print e
    #         print self.book_id, "图片下载出错Exception", self.loadUrl
