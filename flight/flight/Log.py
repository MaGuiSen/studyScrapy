# -*- coding: utf-8 -*-
import json
import os
import time


class Log(object):
    """
    保存日志
    """
    def save(self,fileName, msgDict):
        try:
            with open(os.path.join(os.path.dirname(__file__) + "/file/"+fileName+".json"), "w") as f:
                timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                json.dump(dict({'time': timeStr}, **msgDict), f)
        finally:
            if f:
                f.close()

    def saveTotal(self, msgDict):
        self.save("total", msgDict)