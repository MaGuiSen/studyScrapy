# -*- coding: utf-8 -*-
import re

value = """
 document.domain="qq.com";
    var biz = "MjM5NzU2NDk0MA==" || "";
    var src = "3" ;
    var ver = "1" ;
    var timestamp = "1499763652" ;
    var signature = "KLT6ktu9rfezVeeLGvpIdWXukt757RDgCymg7L1wR2wd*Ajl26L69Uc6xPJUxOBL2bb0nPcShFKpGqnMTfKLVA==" ;
    var name="skylixiaofeng"||"sky";
        var msgList = {"list":[{"app_msg_ext_info":{"author":"ILOVEWAR3","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meeSz2OeuAuDSPkybv*enBDZMHN8vt5lCcVJG0wr*YGPc7KcE7iiRnURI4mfUwCWfpfYCdFC7nNjvPjdDXd2-O7M=","copyright_stat":101,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0EsK4ia3pEHn75SS6iaen5jJjmVf0ohOQALHHgxo8aLt3pYgDhzCPw5LBfQarNt47YsVIJg01j8dYSA/0?wx_fmt=jpeg","digest":"魔兽争霸15周年特别纪念篇！满满的都是回忆","fileid":504430380,"is_multi":1,"multi_app_msg_item_list":[{"author":"老实的小编","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meeSz2OeuAuDSPkybv*enBDbbvfmGIbMBCgKMEpehU7rewLIe6or20ztyQYXjKGMw1FhLBPlpYMJ3W884y7LQnCI=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0EsK4ia3pEHn75SS6iaen5jJj9iaJ2Pj7ep1yvWcK3paVCG6tugRvMNrgW97Tf6Iia1SfDZ9ZmgcWnWng/0?wx_fmt=jpeg","digest":"魔兽人皇Sky的天梯行：这把打出了血性，正面硬刚直接带走暗夜","fileid":504430379,"source_url":"https://v.qq.com/x/page/h0523t2esh7.html","title":"人皇Sky的天梯行：谁说造塔只能猥琐，人族打暗夜一样可以刚正面"}],"source_url":"http://www.toutiao.com/c/user/6641741156/#mid=6641741156","subtype":9,"title":"魔兽争霸3十五周年特别纪念篇！满满的都是青春的回忆"},"comm_msg_info":{"content":"","datetime":1499696617,"fakeid":"2397564940","id":1000000363,"status":2,"type":49}},{"app_msg_ext_info":{"author":"老实的小编","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meVDQWg5FJnGcqPlxelie9hAssltFMrd5rnoFd4sTYVNo*sTPoqcy0zmUSYlCvJCPwOipFt9ecXwqpV-6Tgz8iqY=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0GRpge0DiauBrgIk0wslQvtum6n36dFa9PO5QQq2o6ceiaAWmRYPFG1GyJ7MILvBsWS4KedrMKk4m0g/0?wx_fmt=jpeg","digest":"Fly100%勇夺桂冠！钛度杯War3大师赛总决赛完美落幕！","fileid":0,"is_multi":0,"multi_app_msg_item_list":[],"source_url":"http://www.toutiao.com/c/user/6641741156/#mid=6641741156","subtype":9,"title":"兽人永不洗头，Fly100%碾压120豪夺冠军！钛度杯第一季总决赛完美落幕"},"comm_msg_info":{"content":"","datetime":1499614261,"fakeid":"2397564940","id":1000000362,"status":2,"type":49}},{"app_msg_ext_info":{"author":"钛度杯","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8mebi4nRqkrBEP0K1fxRklMGPEYNmND0RhSb6OhKpyVT5sf7Qb7KTDypov3NUYVFvkaVXpRWDoSkEEZrj-2HkN7uc=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_png/dYWeJThDC0HSx7Oeg1icUNJSDo0RZmKTafmYjsiaYIovhNs8SmmicojbXlb2ne6tfgNHia26S8jydX1gibF3KlLeDBQ/0?wx_fmt=png","digest":"钛度杯War3大师赛总决赛：Fly与120究竟鹿死谁手？","fileid":504430368,"is_multi":1,"multi_app_msg_item_list":[{"author":"老实的小编","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8mebi4nRqkrBEP0K1fxRklMGOXw1QIJTu2pm1rzHnklgaIDO50tzTD61YmZ0zGqu1GNqv1SwG5Rxx9gdkcf9HChbw=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0ExiaeZWibpKH1ghWcibmuTtELX4s4NccIqGlrWTs7TCPYdFib4EzTtFsWnjeUp5KiceX0RvhtYSgGCahA/0?wx_fmt=jpeg","digest":"福利大放送，本周Sky微信中奖名单公布！","fileid":504429580,"source_url":"","title":"福利丨本周Sky微信每周中奖名单公布！"}],"source_url":"http://www.toutiao.com/c/user/6641741156/#mid=6641741156","subtype":9,"title":"新鬼王与老兽王の究极对决，钛度杯总决赛冠军争夺战明晚启动！"},"comm_msg_info":{"content":"","datetime":1499525737,"fakeid":"2397564940","id":1000000361,"status":2,"type":49}},{"app_msg_ext_info":{"author":"钛度杯","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meZaTsuuuykEsJYlSYJIstJw2wM33O9KtEWzB*iRWbpxo4waN99tn3S*60qxJGL6jXO7y2MI3TNdnWBU2SavPnaY=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0H0ry3jcrBnOxBPKfY9hexJFeOW14R2wZW5rmXWibD2Eprib28XJcib8xJhVicDHuj4PytDEibmodaWo8Q/0?wx_fmt=jpeg","digest":"钛度杯War3大师赛总决赛八强首轮前瞻！","fileid":504430358,"is_multi":1,"multi_app_msg_item_list":[{"author":"老实的小编","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meZaTsuuuykEsJYlSYJIstJyFPOFXkAW-9*V-2AbJOs8xGDrZsJS0Qv7wflwhPfwP6yxPi8wSbWkhhFT1PNJ3ZUI=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_png/dYWeJThDC0HP5SM9bsx3Af7nFS3MeJq6ibp4IQNAtNPs0YSBK8GRuDPvWCUmdLpN5v6l2Z5qCdTBNEutlupJjow/0?wx_fmt=png","digest":"当然是选择远离她啊！","fileid":504430339,"source_url":"https://v.qq.com/x/page/a0523tugw75.html","title":"人皇Sky鬼王TED“盖特杯”集锦：绿帽子的大战"}],"source_url":"http://www.toutiao.com/c/user/6641741156/#mid=6641741156","subtype":9,"title":"钛度杯War3大师赛总决赛正式打响！各路大神激情碰撞"},"comm_msg_info":{"content":"","datetime":1499427827,"fakeid":"2397564940","id":1000000360,"status":2,"type":49}},{"app_msg_ext_info":{"author":"老实的小编","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meb2fTQz*Y12oXmukXIhhD2DdTC6HQARRk7EPOSfzFGWs4LL4eEGK1j6zqQ38aQ9sWwRyW2VXzr3khsD3q8pzLYw=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0EHxrwT5Y2C4dR5kg3Xc5JrGH7sGKThtLAlq7o3R1RhHEch4tIMTFGgBGAibXPDRibiby7MQzUx9zNHg/0?wx_fmt=jpeg","digest":"最近都在谈王者荣耀乱象，其实十几年前的魔兽、CS也经历过如此...","fileid":504430350,"is_multi":1,"multi_app_msg_item_list":[{"author":"钛度杯","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meb2fTQz*Y12oXmukXIhhD2D8sDPHTAT0bVgn0bjUp3ovqo4wRFYorNDetJiQ3PM4xembSiql5Z*yX5GTfQNlYVc=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0GF8aUPTfuNDfW1mjoKSb0QJLlszsd6dLnCWGakugWWIFCJ6VibPiasPHGbrzx3MWd4BHZI6jXIf2Ww/0?wx_fmt=jpeg","digest":"钛度杯War3大师线上赛是由SKY发起并赞助的魔兽争霸顶级联赛，赛事每三个月一个赛季，每赛季由三届常规赛和一","fileid":0,"source_url":"http://www.haogegebisai.com/special/S016","title":"钛度杯总决赛对阵出炉！120、Fly、infi、玉米等上演强强对话"},{"author":"老实的小编","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meb2fTQz*Y12oXmukXIhhD2COlw4Yf6M2cMqNwWn1GBuqw0WxyAz6WUHyEn7M5wTa3EkuUeRrMt7oKStoPJwHcnA=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0EHxrwT5Y2C4dR5kg3Xc5JrDsxjumVY7iaCaU7cF8oCiajTwMOAVOxuZaXoRP9kB1u8z5gnwz85AeUw/0?wx_fmt=jpeg","digest":"今日视频：暗夜兽族经典战术吹风流重现天日！","fileid":0,"source_url":"https://v.qq.com/x/page/u05226u4yr5.html","title":"人皇Sky鬼王TED“盖特杯”：暗夜兽族经典战术吹风流"}],"source_url":"http://www.toutiao.com/c/user/6641741156/#mid=6641741156","subtype":9,"title":"最近都在聊王者荣耀，敢问哪个在中国火爆过的游戏没有经历过“磨难”呢？"},"comm_msg_info":{"content":"","datetime":1499353412,"fakeid":"2397564940","id":1000000359,"status":2,"type":49}},{"app_msg_ext_info":{"author":"不老实的彪哥","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meeQIuyj51oIx7cW*7zMOFxFsQE14husVR10BlBjnViWNLlXY985Iy14q9al6SexORBDA3wJRHFsgAQdWYFwSmno=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_png/dYWeJThDC0HP5SM9bsx3Af7nFS3MeJq6ibp4IQNAtNPs0YSBK8GRuDPvWCUmdLpN5v6l2Z5qCdTBNEutlupJjow/0?wx_fmt=png","digest":"为了让你们点开这部视频，TED赔上了自己两个月的零花钱...","fileid":504430339,"is_multi":1,"multi_app_msg_item_list":[{"author":"老实的小编","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meeQIuyj51oIx7cW*7zMOFxFBhGQAKAeFmtnnL9gtSrDCpTN3nEH-uZNyayz55nR0le1k7kGWH8kZG0RqgewnoKA=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0HP5SM9bsx3Af7nFS3MeJq6DbT9qYqgWZlE8238fFgq081icmicmdGSoicziaoxDQuEUlCEiaBwK8q28Hw/0?wx_fmt=jpeg","digest":"XIAOKK对阵BO，剑圣大战恶魔猎手！","fileid":504430338,"source_url":"https://v.qq.com/x/page/r0522qvuu0r.html","title":"《盖特杯》精彩回顾第二弹：XIAOKK对阵BO，剑圣大战恶魔猎手"}],"source_url":"https://v.qq.com/x/page/x0521cyogxm.html","subtype":9,"title":"为了让你们点开这部视频，TED赔上了自己两个月的零花钱..."},"comm_msg_info":{"content":"","datetime":1499265809,"fakeid":"2397564940","id":1000000358,"status":2,"type":49}},{"app_msg_ext_info":{"author":"不老实的彪哥","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meQOXKs*dY164vY*s4a2zzBpUvjEORH7mhZrfuKa8VCacrN2TUiTjbwC-CnjucVgBLK3zBTWqwAPxnRnuxacRWyw=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0HyLVBs5daXVVSgVHfELzPl0RvGQGAGxwdxts8s5f5oLq6qxjeV9oiagO6wPTb2DJj6MY6A2bC6RGg/0?wx_fmt=jpeg","digest":"《星际争霸》已经重制快上线了，咱的魔兽争霸还会远吗？","fileid":504430327,"is_multi":1,"multi_app_msg_item_list":[{"author":"老实的小编","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meQOXKs*dY164vY*s4a2zzBoSo3fUk6Fp8GxaMPJeRBiMBHkUuU7SIz4OPYxkPuP6kWtTH1wJl5QfucFSA1DX2Uo=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_png/dYWeJThDC0Fe0X77zn6ibv3WlWLI2lhBjD1JwdokKyUjUwEdUXtCov3gXXD5KTyAm3fFfX5Y5iaF4HERcol5m1vA/0?wx_fmt=png","digest":"大魔王120第一，FoCuS跻身前五！","fileid":504430103,"source_url":"http://www.toutiao.com/c/user/6641741156/#mid=6641741156","title":"2017年6月选手排名：大魔王120第一，FoCuS跻身前五！"},{"author":"","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meQOXKs*dY164vY*s4a2zzBorRZdO*5nA3ozsbiD6x3VZzXj4GgvrG01Yk1Vn4rdJKzOYb6Xgmr6UmoKkVYrXqQY=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0Gne9SZXVhRYVZ6FOdq3xDdzh2whnX5dgI1Hl4ibr5zuWUWzTia29CGxLyBrCCUK8U80SJnYEHawFKg/0?wx_fmt=jpeg","digest":"FoCuS连胜三局登基，120陨落...","fileid":504430170,"source_url":"http://www.haogegebisai.com/special/S016","title":"钛度杯常规赛#3回顾：FoCuS登基，120陨落..."},{"author":"昨天失误的小编","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meQOXKs*dY164vY*s4a2zzBqi5RNMiRrR2JEjoPSJIR6*Dm*wJw7CK1*LwF*IHdCD5EpsnwXKY1c-huNvhEAnPgM=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_png/dYWeJThDC0HR0UCkJ97ibKPFN5TtKHJQEGwKYNPKzmyzACrpR68jb5NaOo2nSb2H63SKhgNoJ0T5wC9GZeichVmg/0?wx_fmt=png","digest":"打的兽族喊爸爸，战术火魔塔一波流！","fileid":504429597,"source_url":"https://v.qq.com/x/page/h0521qdtz4w.html","title":"人皇Sky的天梯行0704：打的兽族喊爸爸，战术火魔塔一波流"}],"source_url":"http://www.toutiao.com/c/user/6641741156/?tab=weitoutiao#mid=6641741156","subtype":9,"title":"星际都已经重制快上线了，咱的魔兽争霸还会远吗？"},"comm_msg_info":{"content":"","datetime":1499177834,"fakeid":"2397564940","id":1000000357,"status":2,"type":49}},{"app_msg_ext_info":{"author":"有钛度的小编","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meejsXF7xG6zHlTae7RK5FQlyhCnhpOe9YAmfqO2GjuQ9Um9UdX80FeSGoJIBqwsDbP*GORP7JWC30u46A7ASXvM=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0ECwUB2pw0WRv1o3w7RfM7q90abUC8ZS5Z5ibNrABFAP9wFUR37m43sNgxkhB07WliacjahaRYicCZmQ/0?wx_fmt=jpeg","digest":"无良小编搞事！蛋总公开澄清此前广州日报采访内容！","fileid":504430044,"is_multi":1,"multi_app_msg_item_list":[{"author":"锐派War3","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meejsXF7xG6zHlTae7RK5FQnAq3MeAumZW-RhbwCNiUVDTu9O0oh3cZO5MIMIG4nU15IPOX5WSA*KAAWH12gfqj8=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0Gne9SZXVhRYVZ6FOdq3xDdzh2whnX5dgI1Hl4ibr5zuWUWzTia29CGxLyBrCCUK8U80SJnYEHawFKg/0?wx_fmt=jpeg","digest":"恭喜FoCuS完胜120蝉联冠军！","fileid":504430170,"source_url":"http://www.haogegebisai.com/special/S016","title":"钛度杯常规赛#3结局出人意料，FoCuS完胜120蝉联冠军！"}],"source_url":"http://www.toutiao.com/c/user/6641741156/#mid=6641741156","subtype":9,"title":"无良小编搞事情！这一次我们的TH000蛋总真的怒了"},"comm_msg_info":{"content":"","datetime":1499088453,"fakeid":"2397564940","id":1000000356,"status":2,"type":49}},{"app_msg_ext_info":{"author":"钛度震惊君","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meSySDI6Lc*QY*-keGy*TwNGYehsA0owSWdJb8gPIVJ0U6gOvD9ndm1Wj*dk0bb*5k6y7Kl3HIzoVCv96TCy9K2M=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0EoMe3085ppKLS78kl6WFtAuL2TAEkoYfZl1apbnqiaUpKe0m2Bbe7WM8vL5r07huN3NUjO8nsCBLw/0?wx_fmt=jpeg","digest":"美兽王Lyn神突遭横祸，手掌骨折被迫休战","fileid":504430221,"is_multi":1,"multi_app_msg_item_list":[{"author":"锐派War3","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meSySDI6Lc*QY*-keGy*TwNEHZ76QHaJ3WgCaXA8IbTOpQHFdc9Bjudy2jpj0mTJ-CIkgE42SJqq5KIrXHTjJP9Q=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0FvMESq4vbZ5DxokVt7WXHT7S7MJDhIxppTzGx8orwTDmW8eQibbtzIribJHmXQ7FhnyptjxE6ibgZicQ/0?wx_fmt=jpeg","digest":"短王爷，你的良心不会痛吗！","fileid":0,"source_url":"","title":"首届盖特杯回顾：TED绝杀Sky，特短队5:4险胜天王队"}],"source_url":"http://www.toutiao.com/c/user/6641741156/#mid=6641741156","subtype":9,"title":"难以置信！美兽王Lyn神突遭横祸，手掌骨折被迫休战"},"comm_msg_info":{"content":"","datetime":1499005346,"fakeid":"2397564940","id":1000000355,"status":2,"type":49}},{"app_msg_ext_info":{"author":"老实的小编","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meZeScjOz91fwvy*6XvXWU9c9pWoC70uoUWd56oiy02Lix-F5fqfRnkCcvHzyE*QgCfIGied3vGiJ0IXsvAvYUP4=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_png/dYWeJThDC0H4NTstzJQdp7sWfqYiar17pVdOQAnQib5QV3Ogxzo6a0ZwYliccwCZjmASic1bgfIV6Rle1Gj2HnbGQw/0?wx_fmt=png","digest":"自古深情留不住，总是套路得人心","fileid":0,"is_multi":1,"multi_app_msg_item_list":[{"author":"锐派War3","content":"","content_url":"/s?timestamp=1499766106&amp;src=3&amp;ver=1&amp;signature=0CV1L9lq*Cxd4DWtZmLHbZwnglLF2ujgD1-As2qhxkIbluS*qoy7SNK8KARK5SN5oM1RnDyTO6NiJ-rICj8meZeScjOz91fwvy*6XvXWU9dxOmr-OpnQGu-VA2gp3b24Pv4yBupYthWiqGenYidkPefyWVoYeSTTQ0tEGmJJB3k=","copyright_stat":100,"cover":"http://mmbiz.qpic.cn/mmbiz_jpg/dYWeJThDC0FkrpOTBP8wI9socH0Ik3iaJ987JELmTCmppvoMqsoO3x5MiabXic7XBB4aHHlzR9cZvg3AYGNDmu37A/0?wx_fmt=jpeg","digest":"钛度杯常规赛#3战报速递：浪漫，FoCuS和120晋级半决赛","fileid":504430088,"source_url":"http://www.haogegebisai.com/special/S016","title":"钛度杯常规赛#3战报速递：浪漫，FoCuS和120晋级半决赛"}],"source_url":"http://www.toutiao.com/c/user/6641741156/#mid=6641741156","subtype":9,"title":"震精！前世界冠军疯狂晒老照片，然而最大的亮点居然是..."},"comm_msg_info":{"content":"","datetime":1498921544,"fakeid":"2397564940","id":1000000354,"status":2,"type":49}}]};
        seajs.use("sougou/profile.js");

"""

p1 = re.compile('\s*document.*;\s*')
p2 = re.compile('\s*var\s*biz\s*=.*;')
p3 = re.compile('\s*var\s*src\s*=.*;')
p4 = re.compile('\s*var\s*ver\s*=.*;')
p5 = re.compile('\s*var\s*timestamp\s*=.*;')
p6 = re.compile('\s*var\s*signature\s*=.*;')
p7 = re.compile('\s*var\s*name\s*=.*;')
p8 = re.compile('var\s*msgList\s*=.*;')

matchList = p8.findall(value)
for match in matchList:
    match = match.lstrip("var msgList = ")
    print match