# -*- coding: utf-8 -*-
import urllib


def checkNetWork():
    '''
        检测网络
    :return:boolean
    '''
    try:
        response = urllib.urlopen('https://www.baidu.com')
        return response.code == 200
    except Exception:
        return False


def checkService():
    '''
        检测服务器
    :return:boolean
    '''
    return True

    # print checkNetWork()
