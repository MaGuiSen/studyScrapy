# -*- coding: utf-8 -*-


from libMe.util.FileUtil import UploadUtil
fileUtil = UploadUtil(u'/news/wangyi/image/', u'../../res/img/wangyi/')
fileUtil.upload([{
    "path": 'full/391ae6114d37f3a54f369c65d782a2588e625f13.jpg'
}])