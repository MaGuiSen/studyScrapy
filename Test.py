# -*- coding: utf-8 -*-
# # import datetime
# # from apscheduler.schedulers.blocking import BlockingScheduler
# #
# # def tt():
# #     print 1
# #
# # def tt2():
# #     print 2
# #
# # scheduler = BlockingScheduler(daemonic=False)
# # # 先马上开始执行
# # scheduler.add_job(tt, 'date')
# # # 后再抓取之后的某个时间段开始间隔执行
# # scheduler.add_job(tt2, 'interval', seconds=100,
# #                   start_date=datetime.datetime.now() + datetime.timedelta(seconds=2))
# # scheduler.start()
# import time
#
# post_date = '2017-07-24 18:09:00'
# try:
#     post_date = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(post_date, "%Y-%m-%d %H:%M:%S"))
# except Exception:
#     pass
# print post_date
# # import requests
# #
# # result = requests.get('http://mp.weixin.qq.com/profile?src=3&timestamp=1501135271&ver=1&signature=Eh4M*cPhiH3jlAIc5oEFJ9jrheYhxfUS4qVDJXNkdx8*IhB8VuuxdhHz-26cRm7x1eAleQkPyvrDJbap*COCJg==',
# #                        timeout=10,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'})
# # req_code = result.status_code
# # print result.content
# # import webbrowser
# #
# # url = 'http://mp.weixin.qq.com/profile?src=3&timestamp=1501134928&ver=1&signature=Z8gLeXZ4R09gTTsC*Gcezxtso7phoO9CDXJYms2LbugRThJ05H0OYbWXQz**k6CSm-zj6ENur-G-Q9jiF222Fg=='
# # webbrowser.open(url)
# # print webbrowser.get()
import re

value = '''
html{-ms-text-size-adjust:100%;-webkit-te
xt-size-adjust:100%;line-height:1.6}body{-webkit-touch-
callout:none;font-family:-apple-system-font,"Helvetica Neue"
,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-ser
if;background:#f3f3f3;line-height:inherit}body.rich_me
dia_empty_extra{background-color:#f3f3f3}body.rich_media_empty_
extra .rich_media_area_primary:before{display:none}h1,h2,h3,h4,h5,
h6{font-weight:400;font-size:16px}*{margin:0;padding:0}a{color:#60
7fa6;text-decoration:none}.rich_media_inner{font-size:16px;word-wr
ap:break-word;-webkit-hyphens:auto;-ms-hyphens:auto;hyphens:auto}.
rich_media_area_primary{position:relative;padding:20px
 15px 15px;background-color:#fff}.rich_media_area_primary:b
 efore{content:" ";position:absolute;left:0;top:0;width:100
 %;height:1px;border-top:1px solid #e5e5e5;-webkit-transfor
 m-origin:0 0;transform-origin:0 0;-webkit-transform:scaleY
 (0.5);transform:scaleY(0.5);top:auto;bottom:-2px}.rich_med
 ia_area_primary .original_img_wrp{display:inline-block;fon
 t-size:0}.rich_media_area_primary .original_img_wrp .tips_
 global{display:block;margin-top:.5em;font-size:14px;text-a
 lign:right;width:auto;overflow:hidden;text-overflow:ellips
 is;white-space:nowrap;word-wrap:normal}.rich_media_area_ex
 tra{padding:0 15px 0}.rich_media_title{margin-bottom:10px;
 line-height:1.4;font-weight:400;font-size:24px}.rich_media
 _meta_list{margin-bottom:18px;line-height:20px;font-size:0
 }.rich_media_meta_list em{font-style:normal}.rich_media_me
 ta{display:inline-block;vertical-align:middle;margin-right
 :8px;margin-bottom:10px;font-size:16px}.meta_original_tag{
 display:inline-block;vertical-align:middle;padding:1px .5e
 m;border:1px solid #9e9e9e;color:#8c8c8c;border-top-left-r
 adius:20% 50%;-moz-border-radius-topleft:20% 50%;-webkit-b
 order-top-left-radius:20% 50%;border-top-right-radius:20%
 50%;-moz-border-radius-topright:20% 50%;-webkit-border-top
 -right-radius:20% 50%;border-bottom-left-radius:20% 50%;-m
 oz-border-radius-bottomleft:20% 50%;-webkit-border-bottom-
 -radius:20% 50%;border-bottom-right-radius:20% 50%;-moz-bo
 rder-radius-bottomright:20% 50%;-webkit-border-bottom-righ
 t-radius:20% 50%;font-size:15px;line-height:1.1}.meta_ente
 rprise_tag img{width:30px;height:30px !important;display:b
 lock;position:relative;margin-top:-3px;border:0}.rich_medi
 a_meta_text{color:#8c8c8c}span.rich_media_meta_nickname{di
 splay:none}.rich_media_thumb_wrp{margin-bottom:6px}.rich_m
 edia_thumb_wrp .original_img_wrp{display:block}.rich_media
 _thumb{display:block;width:100%}.rich_media_content{overfl
 ow:hidden;color:#3e3e3e}.rich_media_content *{max-width:10
 0% !important;box-sizing:border-box !important;-webkit-box
 -sizing:border-box !important;word-wrap:break-word !import
 ant}.rich_media_content p{clear:both;min-height:1em}.rich_
 media_content em{font-style:italic}.rich_media_content fie
 ldset{min-width:0}.rich_media_content .list-paddingleft-2{
 padding-left:30px}.rich_media_content blockquote{margin:0;
 padding-left:10px;border-left:3px solid #dbdbdb}img{height
 :auto !important}@media screen and device-aspect-ratio:2/3
 ,screen and device-aspect-ratio:40/71{.meta_original_tag{p
 adding-top:0}}@media(min-device-width:375px) and (max-devi
 ce-width:667px) and (-webkit-min-device-pixel-ratio:2){.mm
 _appmsg .rich_media_inner,.mm_appmsg .rich_media_meta,.mm_
 appmsg .discuss_list,.mm_appmsg .rich_media_extra,.mm_appm
 sg .title_tips .tips{font-size:17px}.mm_appmsg .meta_origi
 nal_tag{font-size:15px}}@media(min-device-width:414px) and
  (max-device-width:736px) and (-webkit-min-device-pixel-r
  atio:3){.mm_appmsg .rich_media_title{font-size:25px}}@me
  dia screen and (min-width:1024px){.rich_media{width:740p
  x;margin-left:auto;margin-right:auto}.rich_media_inner{p
  adding:20px}body{background-color:#fff}}@media screen an
  d (min-width:1025px){body{font-family:"Helvetica Neue",H
  elvetica,"Hiragino Sans GB","Microsoft YaHei",Arial,sans
  -serif}.rich_media{position:relative}.rich_media_inner{b
  ackground-color:#fff;padding-bottom:100px}}.radius_avata
  r{display:inline-block;background-color:#fff;padding:3px
  ;border-radius:50%;-moz-border-radius:50%;-webkit-border
  -radius:50%;overflow:hidden;vertical-align:middle}.radiu
  s_avatar img{display:block;width:100%;height:100%;border
  -radius:50%;-moz-border-radius:50%;-webkit-border-radius
  :50%;background-color:#eee}.cell{padding:.8em 0;display:
  ;position:relative}.cell_hd,.cell_bd,.cell_ft{display:ta
  ble-cell;vertical-align:middle;word-wrap:break-word;word
  -break:break-all;white-space:nowrap}.cell_primary{width:
  2000px;white-space:normal}.flex_cell{padding:10px 0;disp
  lay:-webkit-box;display:-webkit-flex;display:-ms-flexbox
  ;display:flex;-webkit-box-align:center;-webkit-align-ite
  ms:center;-ms-flex-align:center;align-items:center}.flex
  _cell_primary{width:100%;-webkit-box-flex:1;-webkit-flex
  :1;-ms-flex:1;box-flex:1;flex:1}.original_tool_area{disp
  lay:block;padding:.75em 1em 0;-webkit-tap-highlight-colo
  r:rgba(0,0,0,0);color:#3e3e3e;border:1px solid #eaeaea;m
  argin:20px 0}.original_tool_area .tips_global{position:r
  elative;padding-bottom:.5em;font-size:15px}.original_too
  l_area .tips_global:after{content:" ";position:absolute;
  left:0;bottom:0;right:0;height:1px;border-bottom:1px sol
  id #dbdbdb;-webkit-transform-origin:0 100%;transform-ori
  gin:0 100%;-webkit-transform:scaleY(0.5);transform:scale
  Y(0.5)}.original_tool_area .radius_avatar{width:27px;hei
  ght:27px;padding:0;margin-right:.5em}.original_tool_area
   .radius_avatar img{height:100% !important}.original_too
   l_area .flex_cell_bd{width:auto;overflow:hidden;text-ov
   erflow:ellipsis;white-space:nowrap;word-wrap:normal}.or
   iginal_tool_area .flex_cell_ft{font-size:14px;color:#8c
   8c8c;padding-left:1em;white-space:nowrap}.original_tool
   _area .icon_access:after{content:" ";display:inline-blo
   ck;height:8px;width:8px;border-width:1px 1px 0 0;border
   -color:#cbcad0;border-style:solid;transform:matrix(0.71
   ,0.71,-0.71,0.71,0,0);-ms-transform:matrix(0.71,0.71,-0
   .71,0.71,0,0);-webkit-transform:matrix(0.71,0.71,-0.71,
   0.71,0,0);position:relative;top:-2px;top:-1px}.weui_loa
   ding{width:20px;height:20px;display:inline-block;vertic
   al-align:middle;-webkit-animation:weuiLoading 1s steps(
   12,end) infinite;animation:weuiLoading 1s steps(12,end) i
   nfinite;background:transparent url("") no-repeat;-webkit-
   background-size:100%;background-size:100%}@-webkit-keyfra
   mes weuiLoading{0%{-webkit-transform:rotate3d(0,0,1,0)}10
   0%{-webkit-transform:rotate3d(0,0,1,360deg)}}@keyframes w
   euiLoading{0%{-webkit-transform:rotate3d(0,0,1,0)}100%{-w
   ebkit-transform:rotate3d(0,0,1,360deg)}}.gif_img_wrp{disp
   lay:inline-block;font-size:0;position:relative;font-weigh
   t:400;font-style:normal;text-indent:0;text-shadow:none 1p
   x 1px rgba(0,0,0,0.5)}.gif_img_wrp img{vertical-align:top
   }.gif_img_tips{background:rgba(0,0,0,0.6) !important;filt
   er:progid:DXImageTransform.Microsoft.gradient(
   =0,startColorstr="#99000000",endcolorstr = "#99000000");b
   order-top-left-radius:1.2em 50%;-moz-border-radius-toplef
   t:1.2em 50%;-webkit-border-top-left-radius:1.2em 50%;bord
   er-top-right-radius:1.2em 50%;-moz-border-radius-topright
   :1.2em 50%;-webkit-border-top-right-radius:1.2em 50%;bord
   er-bottom-left-radius:1.2em 50%;-moz-border-radius-bottom
   left:1.2em 50%;-webkit-border-bottom-left-radius:1.2em 50
   %;border-bottom-right-radius:1.2em 50%;-moz-border-radius
   -bottomright:1.2em 50%;-webkit-border-bottom-right-radius
   :1.2em 50%;line-height:2.3;font-size:11px;color:#fff;text
   -align:center;position:absolute;bottom:10px;left:10px;min
   -width:65px}.gif_img_tips.loading{min-width:75px}.gif_img
   _tips i{vertical-align:middle;margin:-.2em .73em 0 -2px}.
   gif_img_play_arrow{display:inline-block;width:0;height:0;
   border-width:8px;border-style:dashed;border-color:transpa
   rent;border-right-width:0;border-left-color:#fff;border-l
   eft-style:solid;border-width:5px 0 5px 8px}.gif_img_loadi
   ng{width:14px;height:14px}i.gif_img_loading{margin-left:-
   4px}.gif_bg_tips_wrp{position:relative;height:0;line-heig
   ht:0;margin:0;padding:0}.gif_bg_tips_wrp .gif_img_tips_gr
   oup{position:absolute;top:0;left:0;z-index:9999}.gif_bg_t
   ips_wrp .gif_img_tips_group .gif_img_tips{top:0;left:0;bo
   ttom:auto}.rich_media_global_msg{position:fixed;top:0;lef
   t:0;right:0;padding:1em 35px 1em 15px;z-index:2;background-color:#c6e0f8;color:#8c8c8c;fo
   nt-size:13px}.rich_media_global_msg .icon_closed{position:absolute;right:15px;top:50%;margin-top:-5px;line-height:300px;overflow:hidden;-webkit-tap-highlight-color:rgba(0,0,0,0);background:transparent url("") no-repeat 0 0;width:11px;height:11px;vertical-align:middle;display:inline-block;-webkit-background-size:100% auto;background-size:100% auto}.rich_media_global_msg .icon_closed:active{background-position:0 -17px}.preview_appmsg .rich_media_title{margin-top:1.9em}@media screen and (min-width:1024px){.rich_media_global_msg{position:relative;margin:0 20px}.preview_appmsg .rich_media_title{margin-top:0}}.pages_reset{color:#3e3e3e;line-height:1.6;font-size:16px;font-weight:400;font-style:normal;text-indent:0;letter-spacing:normal;text-align:left;text-decoration:none}.weapp_element,.weapp_display_element,.mp-miniprogram{display:block;margin:1em 0}.share_audio_context{margin:16px 0}.weapp_text_link{font-size:17px}.weapp_text_link:before{content:"";display:inline-block;line-height:1;background-size:12px 12px;background-repeat:no-repeat;background-image:url("");vertical-align:middle;font-size:11px;color:#888;border-radius:10px;background-color:#f4f4f4;margin-right:6px;margin-top:-4px;background-position:center;height:20px;width:20px}.weui-mask{position:fixed;z-index:1000;top:0;right:0;left:0;bottom:0;background:rgba(0,0,0,0.6)}.weui-dialog{position:fixed;z-index:5000;width:80%;max-width:300px;top:50%;left:50%;-webkit-transform:translate(-50%,-50%);transform:translate(-50%,-50%);background-color:#fff;text-align:center;border-radius:3px;overflow:hidden}.weui-dialog__hd{padding:1.3em 1.6em .5em}.weui-dialog__title{font-weight:400;font-size:18px}.weui-dialog__bd{padding:0 1.6em .8em;min-height:40px;font-size:15px;line-height:1.3;word-wrap:break-word;word-break:break-all;color:#999}.weui-dialog__bd:first-child{padding:2.7em 20px 1.7em;color:#353535}.weui-dialog__ft{position:relative;line-height:48px;font-size:18px;display:-webkit-box;display:-webkit-flex;display:flex}.weui-dialog__ft:after{content:" ";position:absolute;left:0;top:0;right:0;height:1px;border-top:1px solid #d5d5d6;color:#d5d5d6;-webkit-transform-origin:0 0;transform-origin:0 0;-webkit-transform:scaleY(0.5);transform:scaleY(0.5)}.weui-dialog__btn{display:block;-webkit-box-flex:1;-webkit-flex:1;flex:1;color:#3cc51f;text-decoration:none;-webkit-tap-highlight-color:rgba(0,0,0,0);position:relative}.weui-dialog__btn:active{background-color:#eee}.weui-dialog__btn:after{content:" ";position:absolute;left:0;top:0;width:1px;bottom:0;border-left:1px solid #d5d5d6;color:#d5d5d6;-webkit-transform-origin:0 0;transform-origin:0 0;-webkit-transform:scaleX(0.5);transform:scaleX(0.5)}.weui-dialog__btn:first-child:after{display:none}.weui-dialog__btn_default{color:#353535}.weui-dialog__btn_primary{color:#0bb20c}.rich_media_content{font-size:18px}
'''
# color = '#f3f3f3'
# pAll = re.compile('background-color\s*:\s*' + color + ';?')
# matchUrls = pAll.findall(value)
# if len(matchUrls):
#     for matchUrl in matchUrls:
#         value = value.replace(matchUrl, 'reddddddddddddddddddddddddddddddddddddddddd')
# print value

a = '      '.strip(' ')
if a:
    print 1
else:
    print 2