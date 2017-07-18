# # -*- coding: utf-8 -*-
# import re
#
# from scrapy import Selector
#
# value = """
#
# <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
# <html>
# <head>
# <meta content="text/html; charset=gb2312" http-equiv="Content-Type">
# <title>滚动新闻__腾讯网</title>
# <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7">
# <meta http-equiv="Pragma" content="no-cache" />
# <meta http-equiv="Expires" content="-1">
# <style>
# body{margin:0;padding:0;background-color:#FFF;font-family:"宋体";}
# form,input,select,ul,li,p,h1,h2,h3,h4,h5,h6,p{margin:0;padding:0;}
# ul,li{list-style:none;}
# body,td,select,input,div{font-size:12px;line-height:21px; color:#333;}
# img,a img{ border:none}
# a{ color:#0B3B8D; text-decoration:none}
# a:hover{ color:#c00; text-decoration:underline;}
#
# .box_hr4,.box_hr5,.box_hr6,.box_hr8,.box_hr10,.box_hr12{clear:both;margin:0 auto; overflow:hidden;font-size:0;line-height:0; background:#fff;}
# .box_hr4{height:4px;}.box_hr5{height:5px;}.box_hr6{height:6px;}.box_hr8{height:8px;}.box_hr10{height:10px;}.box_hr12{height:12px;}
# .cl{clear:both;}
#
# .box_hr9,.box_hr16,.box_hr22{ clear:both; overflow:hidden; font-size:1px}
# .box_hr9{ height:9px}.box_hr16{ height:16px}.box_hr22{ height:22px}
#
# .wrap_960{ width:960px}
# .bor_ddd{border:#ddd 1px solid;}
# .pad_l_2{padding-left:2px;}.pad_l_6{padding-left:6px;}.pad_l_8{padding-left:8px;}
# .hr_dot{ width:375px;height:15px; margin-left:3px; overflow:hidden;background:url(http://mat1.qq.com/news/images1/index09/news_nbg1.gif) 0 -945px repeat-x;}
# .more{padding:0 10px 0 0; background: url(http://mat1.qq.com/news/images1/index09/news_nbg1.gif) -174px 9px no-repeat;}
#
# .wrapper { width:960px;margin:0 auto;clear:both;}
# .main{ float:left; width:698px;padding-bottom:20px; border:1px solid #DEDEDE;}
# .main ul{ padding:14px 0;}
# .sidebar{ float:right; width:250px;}
#
# .goto_top{text-align:right;padding-right:30px;}
# .goto_top a{color:#0B3B8D;font-size:14px;}
#
# /*顶部导航*/
# #Top-Article-QQ{height:22px;background:#F8F8F8;border-bottom:1px solid #E6E6E6}
# #Top-Article-QQ li{float:right;color:#A1A0A0}
# #Top-Article-QQ li span{padding:0px 6px}
# #Top-Article-QQ a{color:#A1A0A0}
# #Top-Article-QQ #setIndex{height:22px;background:url(http://mat1.gtimg.com/news/2009/tomies/split_v1.png) no-repeat -299px -68px;margin-left:10px;margin-right:12px;_display:inline}
# #Top-Article-QQ #setIndex a{padding-left:13px}
# /*面包屑*/
# .Crumbs-Article-QQ {float:left;padding-left:4px;padding-top:9px;padding-bottom:3px}
# .Crumbs-Article-QQ img{float:left;margin:0}
# .Crumbs-Article-QQ span {float:left;height:22px;padding-left:14px;padding-top:9px;color:#000}
# .Crumbs-Article-QQ span em{color:#7E7E7E}
# .Crumbs-Article-QQ span a:visited{color:#0B3B8C}
# /*导航*/
# .nav{clear:both;width:938px;height:32px;padding:0 17px 0 5px;margin:0 auto 8px;overflow:hidden;background:url(http://mat1.qq.com/news/images1/index09/news_nbg2.gif) no-repeat}
# .nav ul{float:left;width:825px;margin:0;padding:0;padding-top:7px}
# .nav li{float:left;padding:0 5px;height:19px;overflow:hidden}
# .nav li.sep{width:2px;padding:0;font-size:1px;background:url(http://mat1.qq.com/news/images1/index09/news_nbg2.gif) 0 -39px no-repeat}
# .nav li a,.nav li a:visited{padding:3px 5px 3px 6px;font-size:14px;color:#F2F2F2;line-height:21px;background:none}
# .nav .txtlink{float:right;width:113px;padding-top:8px;height:17px;overflow:hidden;text-align:right}
# .nav .txtlink a,.nav .txtlink a:visited{padding:3px 2px 3px 3px;color:#E6CAC3;line-height:19px;background:none}
# .nav li a:hover,.nav .txtlink a:hover{color:#F2F2F2;background:#900002;text-decoration:none}
# .nav .txtlink span{margin-left:6px}
#
# .CalendarWrapper{width:248px;padding-bottom:11px;font-family:Tahoma,Arial;color:#3C3C3C;border:1px solid #DEDEDE;background:#FFFFFF}
# .CalendarWrapper a{color:#3C3C3C;text-decoration:none}
# .CalendarWrapper a:hover{color:#c00;text-decoration:none}
# .CalendarWrapper .CalendarHead{width:222px;height:19px;overflow:hidden;margin:0 auto;padding:8px 0;line-height:21px;border-bottom:1px solid #CDCFD3}
# .CalendarWrapper .CalendarHead h3{font-size:14px;text-align:center;font-weight:bold}
# .CalendarWrapper .CalendarHead .btn{display:block;width:19px;height:17px;padding-top:2px;overflow:hidden;line-height:17px;font-family:宋体;font-size:12px;text-align:center;background:url(http://mat1.gtimg.com/news/2009/calendar_btn_v1.gif) no-repeat}
# .CalendarWrapper .CalendarCon table{border-collapse:separate;border-spacing:2px}
# .CalendarWrapper .CalendarCon th,.CalendarWrapper .CalendarCon td{width:30px;text-align:center;line-height:19px;font-weight:normal}
# .CalendarWrapper .CalendarCon th.saturday{color:#008000}
# .CalendarWrapper .CalendarCon th.sunday{color:#CC0000}
# .CalendarWrapper .CalendarCon a,.CalendarWrapper .CalendarCon em,.CalendarWrapper .CalendarCon span{display:block;width:30px;height:30px;overflow:hidden;color:#3C3C3C;line-height:31px;background:#F0F0F0}
# .CalendarWrapper .CalendarCon span{ color:#C3C3C3}/* 今天日期后的标签 */
# .CalendarWrapper .CalendarCon em{ background:#CCCCCC}/* 选中日期的标签 */
# .CalendarWrapper .CalendarCon a.today,.CalendarWrapper .CalendarCon em.today{ font-style:normal;background:#C6C9E7}/* 今天日期在标签中加class=&quot;today&quot; */
# .CalendarWrapper .CalendarCon a:hover{ background:#CCCCCC;text-decoration:none}
# .todayBtn{width:238px;height:34px;padding-right:12px;font-size:14px;color:#C3C3C3;line-height:34px;text-align:right}/* 当前是今天的时候去掉“今日新闻”外面的a标签即可 */
# .todayBtn a{color:#0B3B8D}
#
# .curPosition{ height:34px; padding:2px 0 0 20px; margin-bottom:20px; line-height:34px; background:#FAFAFA}
# .inputTxt{ width:212px; height:18px; padding:1px 5px 0; line-height:18px; border:1px solid #C2C2C2}
# .inputBtn{ width:40px; height:21px; border:0; background:url(images/searchBtn.gif) no-repeat; cursor:pointer}
# .titbox{ height:42px; padding-top:20px;padding-left:54px; line-height:29px; font-size:14px}
# .titbox h1{ float:left; margin-right:25px; font-family:黑体; font-size:20px; line-height:25px; font-weight:normal}
# .titbox h1 .ffv{ font-family:Verdana}
#
# .newslist ul{margin-left:54px;}
# .newslist li{line-height:24px;color:#0B3B8D;}
# .newslist a{font-size:14px;}
# .newslist a:visited{color:#800080;text-decoration:none;}
# .newslist a:hover{text-decoration:underline;}
# .pub_time {color:#9C9C9C;}
#
# .pageNav{ clear:both; height:22px;margin:18px 0;padding-left:60px; font-family:Arial, Helvetica, sans-serif; font-size:14px}
# .pageNav a,.pageNav strong,.pageNav span{ display:block; float:left; padding:0 8px; overflow:hidden; margin-right:5px; background:#fff}
# .pageNav a,.pageNav span{ height:20px; line-height:22px; border:1px solid #CCDBE4}
# .pageNav a.f12,.pageNav strong.f12,.pageNav span{ font-size:12px}
# .pageNav a:hover{ text-decoration:none}
# .pageNav strong{ height:22px; line-height:24px}
# .pageNav .mor{border:0;padding:0;height:21px;line-height:21px}
# .pageNav .na{color:#DBE1E6}
#
# .crumbs_nav {width:960px; margin:0 auto;clear:both;}
# .crumbs_nav .logo{padding:9px 0 3px 4px;}
# .crumbs_nav .logo img{float:left; border:none;}
# .crumbs_nav .crumbs{float:left;height:22px;padding:9px 0 0 14px; font-size:12px; }
# .crumbs_nav .crumbs a{color:#0B3B8C;text-decoration:none;}
# .crumbs_nav .crumbs a:hover{text-decoration:underline;}
# .crumbs_nav .crumbs em{font-style:normal;font-weight:normal;}
# .crumbs_nav .toolbar{float:right;}
# </style><!--[if !IE]>|xGv00|895ad8fe300a725405fdaf70cf4a1efa<![endif]--><!--[if !IE]>|xGv00|8562b5198b819aae2599422d037fbd8e<![endif]-->
# </head>
# <body>
# <a name="top"></a><script>
# function ResumeError() {return true;}
# window.onerror = ResumeError;
# </script>
# <style>
# #channel_nav{margin:0 auto 10px!important}
# #main_nav_qq .main{border:none}
# #channel_nav .Form-Crumbs-Article-QQ .txtArea{line-height:16px}
# #channel_nav .ft{width:958px!important}
# </style>
# <!--迷你导航-->
# <style>
# /*全站迷你导航 v20120718 1kpx @austinjin*/
# body{font-family:"宋体","Arial Narrow",sans-serif;-webkit-text-size-adjust:100%;}
# #mini_nav_qq_wrap{width:100%;height:25px;background:url(http://mat1.gtimg.com/www/images/nav/mini_bg.png) top left repeat-x}
# #mini_nav_qq{width:1000px;height:25px; margin:0 auto;padding:0;font-size:12px;font-family:"宋体","Arial Narrow",sans-serif;clear:both;}
# #mini_nav_qq div{color:#666;line-height:24px;}
# #mini_nav_qq .mini_nav_fl{float:left;}
# #mini_nav_qq ul,#mini_nav_qq li{margin:0;padding:0;list-style:none;}
# #mini_nav_qq .first{padding-left:4px;}
# #mini_nav_qq .first a{padding-right:13px;background:url(http://mat1.gtimg.com/www/images/nav/mini_arrow.png)  right -1px no-repeat;}
# #mini_nav_qq .end{border:none;}
# #mini_nav_qq ul{padding:7px 3px 0 0;}
# #mini_nav_qq li{float:left;padding:0 8px;*padding-top:1px;border-right:#ddd 1px solid;line-height:12px;color:#666;}
# #mini_nav_qq a{color:#666;font-family:"宋体","Arial Narrow",sans-serif; text-decoration:none;}
# #mini_nav_qq a:visited{color:#666;}
# #mini_nav_qq a:hover{color:#666; text-decoration: underline;}
# #mini_nav_qq em a{font-family:Arial,sans-serif; }
# </style>
# <div id="mini_nav_qq_wrap">
# <div id="mini_nav_qq">
# 	<div class="mini_nav_fl" bossZone="miniNav">
# 		<ul>
# 			<li class="first"><a href="http://www.qq.com/" target="_blank">腾讯网首页</a></li><li><a href="http://www.qq.com/map/" target="_blank">网站导航</a></li><li class="end"><a href="http://mail.qq.com/" target="_blank">邮箱</a></li>
# 		</ul>
# 	</div>
# 	<style type="text/css">
# /*导航微博登录 v20120209 1.0.7 mblogin*/
# #site_nav_mblogin{float:right;height:25px;padding-right:8px;line-height:24px;color:#666;font-size:12px;font-family:"宋体","Arial Narrow",sans-serif;}
# #site_nav_mblogin div{float:left;}
# #site_nav_mblogin .mblog_logo{width:20px;height:24px;background:url(http://mat1.gtimg.com/www/images/nav/wblogin_bt_v3.png) -90px 5px no-repeat; }
# #site_nav_mblogin .mblog_logo span{display:none;}
# #site_nav_mblogin .mblog_login_info span{padding-right:12px;}
# #site_nav_mblogin .mblog_login_info em{font-family:Arial;font-style:normal;padding-right:12px;}
# #site_nav_mblogin .mblog_login_button span,#site_nav_mblogin .mblog_enter_button span{*padding-left:1px;_padding-left:1px;text-align:center;color:#fff;}
# #site_nav_mblogin .mblog_login_button,#site_nav_mblogin .mblog_enter_button{position:relative;z-index:10000;width:57px;height:17px;margin-top:2px;margin-right:12px;padding-top:2px;background:url(http://mat1.gtimg.com/www/images/nav/wblogin_bt_v3.png) 0 0 no-repeat;cursor:pointer;text-align:center;line-height:17px;overflow:visible;color:#fff;}
# #site_nav_mblogin .mblog_enter_button{display:none;}
# #site_nav_mblogin .mblog_login_text{*padding-top:1px;_padding-top:1px;}
# #site_nav_mblogin .mblog_loginout_text{display:none;*padding-top:1px;_padding-top:1px;}
#
# #site_nav_mblogin a{color:#666; text-decoration:none;}
# #site_nav_mblogin a:visited{color:#666;}
# #site_nav_mblogin a:hover{color:#666; text-decoration: underline;}
# #site_nav_mblogin .mblog_login_info em a,#site_nav_mblogin .mblog_login_info em a:visited,#site_nav_mblogin .mblog_login_info em a:hover{color:#0B3B8C}
# #site_nav_mblogin .mblog_login_info a.mbAtMe,#site_nav_mblogin .mblog_login_info a.mbAtMe:visited,#site_nav_mblogin .mblog_login_info a.mbAtMe:hover{color:#BD0A01;}
# #site_nav_mblogin .mblog_enter_button a,#site_nav_mblogin .mblog_enter_button a:visited,#site_nav_mblogin .mblog_enter_button a:hover{color:#fff;line-height:17px;}
#
# #site_nav_mblogin .mbCardUserInfo {position: absolute;z-index:999999;left:-160px; top:0;width:236px;margin-top: 26px; text-align:left;text-indent:0;overflow:visible;}
# #site_nav_mblogin .mbCardUserDetail div{line-height:18px;}
# #site_nav_mblogin .mbCardUserInfo{height:auto;padding:10px 24px 10px 10px;background:#ffffce;border:#f0e5ba 1px solid;color:#666;}
# #site_nav_mblogin .mbCardUserInfo .arrowBox{position:absolute;width:15px;height:8px;left:0;top:0;margin:-8px 0 0 180px;font-size:1px;line-height:1px;background:url(http://mat1.gtimg.com/www/images/nav/wblogin_bt_v3.png) 0 -30px no-repeat;celar:both;zoom:1;}
# #site_nav_mblogin .mbCardUserInfo .arrowBox div{font-size:1px;line-height:1px;}
# #site_nav_mblogin .mbCardUserInfo .mbClose {position:absolute;top:0;right:0;width:15px;height:15px;margin:4px;background:url(http://mat1.gtimg.com/www/images/nav/wblogin_bt_v3.png) 0 -45px no-repeat;font-size:1px;line-height:1px;cursor:pointer;}
# #site_nav_mblogin .mbCardUserInfo .mbClose span{display:none;}
# #site_nav_mblogin .mbCardUserInfo .mbCardUserDetail .mbTxt1,#site_nav_mblogin .mbCardUserInfo .mbCardUserDetail .mbUserNick,#site_nav_mblogin .mbCardUserInfo .mbCardUserDetail .mbFriends{color:#666;}
# #site_nav_mblogin .mbCardUserInfo .mbCardUserDetail .mbReg{padding-left:180px;text-align:left;}
# #site_nav_mblogin .mbCardUserInfo .mbCardUserDetail .mbReg,#site_nav_mblogin .mbCardUserInfo .mbCardUserDetail .mbReg a,#site_nav_mblogin .mbCardUserInfo .mbCardUserDetail .mbReg a:visited{color:#2b4a78;text-decoration:underline;}
#
# #site_nav_mblogin .mbCardUserInfo {-moz-border-radius: 6px;-moz-box-shadow: 2px 2px 2px #f0e5ba;-webkit-border-radius: 6px;-webkit-box-shadow: 2px 2px 2px #f0e5ba;}
#
# @media screen and (-webkit-min-device-pixel-ratio:0) {
# /* Safari 3.0 and Opera 9 rules here */
# #site_nav_mblogin{font-family:宋体, STSong;}
# }
#
# /*=S 浮动层 */
# .share_layer { overflow:hidden; padding:7px; position:absolute; z-index:999999;zoom:1;font-size:12px; font-family:Arial, Sans-Serif; }
# .share_layer ul, .share_layer ul li { list-style-type:none; }
# .share_layer img { border:0 none; }
# .share_layer a { text-decoration:none; }
# .share_layer a:hover { text-decoration:underline; }
# .share_layer button,.share_layer label { cursor:pointer; border:0 none; }
# .share_layer input,.share_layer  button { font-size:12px; font-family:Arial, Sans-Serif; }
# .share_layer_main{ border:1px solid #b5c1ca; background-color:#FAFCFF; position:relative; z-index:5}
# .share_layer_title { height:24px; background:#EEF4F6 url(http://mat1.gtimg.com/www/images/nav/loginpop_tbg.png) repeat-x; cursor:move; border-bottom:1px solid #CED3E4; }
# .share_layer_title h3 { float:left; margin:0;padding:3px 0 0 12px; color:#666; font-size:13px;font-weight:normal; line-height:18px; overflow:hidden; font-family:Arial, Helvetica, sans-serif;}
# .share_layer_title .mblogo{ padding-left:24px;background:url(http://mat1.gtimg.com/www/images/nav/wblogin_bt1.png) -84px 6px no-repeat;}
# .share_layer .bt_close { background:url(http://imgcache.qq.com/qzonestyle/qzone_app/app_news_share_v1/pop_bg.png) no-repeat 0 -39px; width:9px; height:10px;cursor:pointer; position:absolute; right:10px; top:11px; z-index:5px;}
# .share_layer_cont a:link, .share_layer_cont a:visited { color:#5F5F5F; text-decoration:underline; }
# .share_layer_cont a:hover, .share_layer_cont a:active { color:#494949; }
# .share_layer_cont { color:#000000; background-color:#FAFCFF;}
# .share_layer_hint { color:#9E9E9E; font-style:normal; }
# .global_tip_button { text-align:center; clear:both; width:100%;}
# .bt_tip_sure, .bt_tip_cancel { background-image:url(http://imgcache.qq.com/qzonestyle/qzone_app/app_news_share_v1/pop_bg.png); background-repeat:no-repeat; background-position:0 -58px; font-size:12px; line-height:19px; width:48px; height:23px; margin-right:6px; *overflow:visible;
# _padding-top:3px; _line-height:12px; cursor:pointer; }
# *:lang(zh) .bt_tip_sure, .bt_tip_cancel {padding-top /*\**/:4px\9}
# .bt_tip_cancel { color:#4D637F; background-color:#F3F4F5; background-position:-54px -58px; }
# .icon_hint_warn, .icon_hint_succeed { background:transparent url(http://imgcache.qq.com/qzonestyle/qzone_app/app_news_share_v1/pop_bg.png) no-repeat; display:-moz-inline-stack; display:inline-block; height:15px; width:15px; vertical-align:middle; }
# .icon_hint_warn { background-position:-39px -37px; _vertical-align:-2px; }
# .icon_hint_succeed { background-position:-18px -37px; }
# .layer_popup { background-color:#FFFFFF; border:2px solid #6792bc; }
# .icon_hint_warn span, .icon_hint_succeed span { display:none; }
# .share_layer .bg {position:absolute;top:0;left:0;height:100%;padding:500px;zoom:1;}
# .share_layer .del_fri{font-weight:bold;display:-moz-inline-stack;display:inline-block;line-height:9px;width:11px;height:10px;position:absolute;top:6px;right:10px;cursor:pointer; font-family:"Comic Sans MS","Verdana", cursive; color:#99ADBA;}
# .share_layer .del_fri:hover{text-decoration:none; color:#666666;}
# .share_layer_title .none { display:none !important; }
# /*=E 浮动层 */
# </style>
# 	<div id="site_nav_mblogin" class="site_nav_mblogin" bossZone="mbLogin">
# 		<div class="mblog_logo"><span>腾讯微博蒲公英</span></div>
# 		<div class="mblog_login_info" id="mblog_logined_info"></div>
# 		<div class="mblog_login_button" id="mblog_login_button"><span>登录微博</span><div class="mbCardUserInfo" id="mbCarduserNotLogin" style="display: none;">
# 				<div class="arrowBox"><div class="arrow"></div></div>
# 				<div class="mbClose"><a href="#"><span>关闭</span></a></div>
# 				<div class="mbCardUserDetail">
# 					<div class="mbConTxt">
# 						<span class="mbTxt1">加入微博，记录点滴，分享感动，握手明星</span>
# 					</div>
# 					<div class="mbReg"><a target="_blank" href="http://t.qq.com?pref=qqcom.toptips">开通微博</a></div>
# 				</div>
# 			</div>
# 		</div>
# 		<div class="mblog_enter_button" id="mblog_enter_button"><span>进入微博</span></div>
# 		<div class="mblog_login_text" id="mblog_login_text"><a href="http://t.qq.com/reg/index.php?pref=qqcom.mininav" target="_blank">注册</a></div>
# 		<div class="mblog_loginout_text" id="mblog_logout_text"><a href="javascript:void(0)" target="_blank">退出</a></div>
# 	</div>
#
# <script src="http://mat1.gtimg.com/www/mb/js/portal/mi.MiniNav_13090403.js" charset="utf-8"></script>
#
#
# <!--搜狗搜索-->
# <style type="text/css">
# #sosoSearch{width:154px;height:18px;float:right;margin-right:15px;display:inline;border:1px solid #d7d7d7;margin-top:5px;}
# #searchKey{width:129px;height:18px;float:left;border:0;margin:0;padding:0;}
# #searchBtn{width:24px;height:18px;float:right;border:0;text-indent:-9999px;cursor:pointer;background:url(http://mat1.gtimg.com/www/images/qq2012/ztSougouBtn.png) no-repeat;}
# .soso-smart-m{position:absolute;z-index:9999;margin:0;background:#fff;border:1px solid #ccc;cursor:default;}
# .soso-smart-m td{font-size:13px;line-height:22px;font-family:"微软雅黑";}
# /* 未选中行的样式 */
# .soso-smart-a{}
# /* 选择行的样式 */
# .soso-smart-b{background:#D8ECFF;}
# /* 文本样式 */
# .soso-smart-c{padding-left:3px;white-space:nowrap;text-align:left;overflow:hidden;}
# </style>
# <form role="search" action="http://www.sogou.com/tx" id="sosoSearch" name="soso_search_box" method="get" target="_blank">
# 	<input id="sogouSite" type="hidden" name="site" value="qq.com" />
# 	<input type="text" id="searchKey" title="请输入关键词" name="query" x-webkit-speech x-webkit-grammar="builtin:translate" autocomplete="off" onfocus="if(this.value=='请输入关键词')this.value=''" />
# 	<button id="searchBtn" aria-pressed="false" title="按下按钮，在搜狗中搜索相关内容" onClick="submit();bossSearch('submit',2537)"><span>搜索</span></button>
# </form>
# <script type="text/javascript">
# (function(d, fname, useSuggest,isChannelPage,pid) {
# 	var frm = d.forms[fname], elems = frm.elements, input = elems['query'];
# 	var IS_MSIE = navigator.userAgent.toLowerCase().indexOf('msie') != -1 && !window.opera;
# 	var isIE6 = navigator.userAgent.toLowerCase().indexOf('msie 6.0') != -1;
# 	var sHost = location.host||'www.qq.com',sitePrefix='www';
# 	var CPID = new Array();
# 	if(sHost){
# 		var arr = sHost.replace(/\.qq\.com$/i,'').split('.');
# 		sitePrefix = arr[0];
# 		document.getElementById("sogouSite").value = sitePrefix + ".qq.com";
# 	}
# 	createHiddenInput('hdq',"sogou-wsse-b58ac8403eb9cf17-0100",false);
# 	var scField = createHiddenInput('sourceid',"sugg",false);
#     var sub = document.getElementById("sub");
# 	if(typeof sosoArticlKey != 'undefined' && sosoArticlKey.length){
# 		setFieldValue(input,sosoArticlKey);
# 	}
# 	function createHiddenInput(name, value, disabled) {
# 		if(elems[name]) {
# 			elems[name].value = value;
# 			if(disabled) elems[name].disabled = 'disabled';
# 			else elems[name].removeAttribute('disabled');
# 			return elems[name];
# 		}
# 		try{
# 			var element = document.createElement('<input name="'+name+'" />');
# 		}catch(e){}
#
# 		if(!element || element.nodeName.toUpperCase() != 'INPUT'){
# 			var element = document.createElement('input');
# 		}
# 		element.type = 'hidden';
# 		element.name = name;
# 		element.value = value;
# 		if(disabled)
# 			element.disabled = disabled;
# 		frm.appendChild(element);
# 		return element;
# 	}
#
# 	function disableHidden(inpt) {
# 		inpt.disabled = 'disabled';
# 	}
# 	function setFieldValue(field, val) {
# 		field.value = val;
# 	}
# 	if(useSuggest) {
# 		var fnToRun = function() {
# 			var fileLoaded = function() {
# 			  if (IS_MSIE && ac.readyState != "complete" && ac.readyState != "loaded") return;
# 			  if(!sososmart) return;
# 			  var divs = frm.getElementsByTagName('div');
# 			  var inputWrap;
# 			  for(var i=0,len=divs.length;i<len;i++){
# 			  	if(divs[i].className != 'inputWarp') continue;
# 			  	inputWrap = divs[i];
# 			  	break;
# 			  }
# 			  sososmart.init(frm,input,true,'',true,inputWrap,null,null,CPID[0],scField);
# 			}
# 			var ac = d.createElement('script');
# 			ac.type = 'text/javascript';
# 			ac.async = true;
# 			ac.src = 'http://mat1.gtimg.com/www/js/qq2012/suggestionZT.v1.0.1.js';
# 			var s = d.getElementsByTagName('script')[0];
#
# 			if(IS_MSIE && !window.opera) {
# 				ac.onreadystatechange = fileLoaded;
# 			} else {
# 				ac.onload = fileLoaded;
# 			}
# 			s.parentNode.insertBefore(ac, s);
# 		};
# 		if(IS_MSIE){
# 			if(window.attachEvent){
# 				window.attachEvent('onload',fnToRun,false);
# 			}else{
# 				window.addEventListener('load',fnToRun);
# 			}
# 		}else{
# 			fnToRun();
# 		}
# 	}
# })(document, 'soso_search_box', true,true, "sogou-wsse-b58ac8403eb9cf17-0100");
#
#
# function bossSearch(zoneID,bossID){
#     //var bossID = 2537;
#     try{
# 		var a=document.cookie.match(new RegExp('(^|)pgv_pvid=([^;]*)(;|$)'));
# 		var pvid=(a==null?"":"F"+unescape(a[2]));
# 		a=document.cookie.match(new RegExp('(^|)o_cookie=([^;]*)(;|$)'));
# 		var iQQ=(a==null?"":unescape(a[2]));
# 		var iurl = 'http://btrace.qq.com/kvcollect?BossId='+bossID+'&sOp='+zoneID+'&sBiz=zt.qq.com&iQQ='+iQQ+'&sLocalUrl='+escape(location.href)+'&ext1='+pvid+'&ext2=&'+Math.random();
# 		var gImageSerach = new Image(1,1);
# 		gImageSerach.src = iurl;
# 	}catch(e){}
# }
#
# function smartboxClick(){
# 	bossSearch("smartbox",2537)
# }
# </script><!--[if !IE]>|xGv00|b59ac84256a86fb6e209deab0d5021ea<![endif]-->
# </div>
# </div>
# <!--t20120606--><!--[if !IE]>|xGv00|9d60830460dc624365aaab96b1c11507<![endif]-->
# <style>
# /*全站主导航 v20120620 1kpx*/
# #main_nav_qq{width:984px;height:42px;margin:0 auto;padding:7px 8px 6px 8px;font-size:12px;font-family:"宋体","Arial Narrow";clear:both;}
# #main_nav_qq ul,#main_nav_qq li{margin:0;padding:0;list-style:none;}
# #main_nav_qq a{color:#000;font-family:"宋体","Arial Narrow"; text-decoration:none;}
# #main_nav_qq a:visited{color:#000;}
# #main_nav_qq a:hover{color:#db0010; text-decoration: underline;}
# #main_nav_qq a.lchot{color:#db0010;}
# #main_nav_qq a.lchot:visited{color:#db0010;}
# #main_nav_qq .main{float:left;width:147px;padding:0 10px 0 16px;background:url(http://mat1.gtimg.com/www/images/nav/nav_2.png) right center no-repeat; text-align:center;}
# #main_nav_qq .main strong{padding-right:6px;}
# #main_nav_qq .w_1{padding-left:3px;}
# #main_nav_qq .w_2{width:156px;}
# #main_nav_qq .w_5{width:110px;}
# #main_nav_qq .w_6{width:115px;padding-right:0;background:none;}
# #main_nav_qq ul{display:block; clear:both;zoom:1;}
# #main_nav_qq li{float:left;padding-right:10px;line-height:21px; background:none;}
# #main_nav_qq li.end{padding-right:0;}
# #main_nav_qq .en{font-family:Arial,Tahoma,Verdana,sans-serif;}
# #main_nav_qq .mblog{padding-right:11px;background:url(http://mat1.gtimg.com/www/iskin960/mblog_blog_w.png) right top no-repeat;}
# </style>
#
# <div id="main_nav_qq" bossZone="mainNav">
# 	<div class="main w_1">
# 			<ul>
# 				<li><strong><a target="_self" href="http://news.qq.com/">新闻</a></strong></li>
# 				<li><a target="_self" href="http://pp.qq.com/">图片</a></li>
# 				<li><a target="_self" href="http://view.news.qq.com/">评论</a></li>
#                 <li><a target="_self" href="http://mil.qq.com/">军事</a></li>
# 			</ul>
# 			<ul>
# 				<li><strong><a target="_self" href="http://finance.qq.com/">财经</a></strong></li>
# 				<li><a target="_self" href="http://finance.qq.com/stock/">股票</a></li>
# 				<li><a target="_self" href="http://finance.qq.com/hk/">港股</a></li>
# 				<li><a target="_self" href="http://finance.qq.com/fund/">基金</a></li>
# 			</ul>
# 	</div>
# 	<div class="main">
#    			 <ul>
# 				<li><strong><a target="_self" href="http://v.qq.com/">视频</a></strong></li>
# 				<li><a target="_self" href="http://v.qq.com/tv/">热剧</a></li>
# 				<li><a target="_self" href="http://v.qq.com/variety/">综艺</a></li>
# 				<li><a target="_self" href="http://v.qq.com/paike/">拍客</a></li>
# 			</ul>
#
# 			<ul>
# 				<li><strong><a target="_self" href="http://sports.qq.com/">体育</a></strong></li>
# 				<li><a href="http://sports.qq.com/isocce/Spain.htm" target="_self">西甲</a></li>
# 				<li><a target="_self" href="http://sports.qq.com/lottery/">彩票</a></li>
# 				<li><a target="_self" href="http://sports.qq.com/csocce/csl/index.htm">中超</a></li>
# 			</ul>
# 	</div>
# 	<div class="main">
#     		<ul>
# 				<li><strong><a target="_self" href="http://ent.qq.com/">娱乐</a></strong></li>
# 				<li><a target="_self" href="http://ent.qq.com/star/">明星</a></li>
# 				<li><a target="_self" href="http://ent.qq.com/movie/">电影</a></li>
# 				<li><a target="_self" href="http://yue.qq.com/">音乐</a></li>
# 			</ul>
# 			<ul>
# 				<li><strong><a target="_self" href="http://lady.qq.com/">女性</a></strong></li>
# 				<li><a target="_self" href="http://luxury.qq.com/">时尚</a></li>
# 				<li><a target="_self" href="http://health.qq.com/">健康</a></li>
# 				<li><a target="_self" href="http://baby.qq.com/">育儿</a></li>
# 			</ul>
# 	</div>
# 	<div class="main">
# 			<ul>
# 				<li><strong><a target="_self" href="http://auto.qq.com/">汽车</a></strong></li>
# 				<li><a target="_self" href="http://data.auto.qq.com/car_brand/index.shtml">车型</a></li>
# 				<li><a target="_self" href="http://house.qq.com/">房产</a></li>
# 				<li><a target="_self" href="http://c.l.qq.com/lclick?seq=20120810000275&loc=hdjc">家居</a></li>
# 			</ul>
# 			<ul>
# 				<li><strong><a target="_self" href="http://tech.qq.com/">科技</a></strong></li>
# 				<li><a target="_self" href="http://digi.tech.qq.com/" class="lchot">数码</a></li>
# 				<li><a target="_self" href="http://digi.tech.qq.com/mobile/">手机</a></li>
# 				<li><a target="_self" href="http://hea.qq.com">家电</a></li>
# 			</ul>
# 	</div>
# 	<div class="main">
# 			<ul>
# 				<li><strong><a target="_self" href="http://book.qq.com/">读书</a></strong></li>
# 				<li><a target="_self" href="http://edu.qq.com/">教育</a></li>
#                 		<li><a target="_self" href="http://yc.qq.com/">小说</a></li>
#                 		<li><a target="_self" href="http://abroad.qq.com/">出国</a></li>
#
# 			</ul>
# 			<ul>
# 				<li><strong><a target="_self" href="http://games.qq.com/">游戏</a></strong></li>
# 				<li><a target="_self" href="http://comic.qq.com/">动漫</a></li>
# 				<li><a target="_self" href="http://astro.lady.qq.com/">星座</a></li>
# 				<li><a target="_self" href="http://trip.elong.com/">旅游</a></li>
# 			</ul>
# 	</div>
# 	<div class="main w_6 end">
# 			<ul>
# 				<li><strong><a target="_self" href="http://www.paipai.com/">购物</a></strong></li>
# 				<li><a target="_self" href="http://blog.qq.com/">博客</a></li>
# 				<li class="end"><a target="_self" href="http://cul.qq.com/">文化</a></li>
# 			</ul>
# 			<ul>
# 				<li><strong><a target="_self" href="http://gongyi.qq.com/">公益</a></strong></li>
# 				<li><a target="_self" href="http://kid.qq.com/">儿童</a></li>
# 				<li class="end more"><a target="_self" href="http://www.qq.com/map/">更多>></a></li>
# 			</ul>
# 	</div>
# </div><!--[if !IE]>|xGv00|b28ef20c827fc68630e42f418aedb015<![endif]-->
#
# <!--[if !IE]>|xGv00|e82c45ae498d4fbd374338574241f4b1<![endif]--><script type="text/javascript" src="http://imgcache.qq.com/qzone/biz/comm/js/qbs.js"></script>
# <script type="text/javascript">
# var TIME_BEFORE_LOAD_CRYSTAL = (new Date).getTime();
# </script>
# <script src="http://ra.gtimg.com/web/crystal/v2.8Beta07Build071/crystal-min.js" id="l_qq_com" arguments="{'extension_js_src':'http://ra.gtimg.com/web/crystal/v2.8Beta07Build071/crystal_ext-min.js', 'jsProfileOpen':'false', 'mo_page_ratio':'0.01', 'mo_ping_ratio':'0.01', 'mo_ping_script':'//ra.gtimg.com/sc/mo_ping-min.js'}"></script>
# <script type="text/javascript">
# if(typeof crystal === 'undefined' && Math.random() <= 1) {
#   (function() {
#     var TIME_AFTER_LOAD_CRYSTAL = (new Date).getTime();
#     var img = new Image(1,1);
#     img.src = "http://dp3.qq.com/qqcom/?adb=1&dm=tech&err=1002&blockjs="+(TIME_AFTER_LOAD_CRYSTAL-TIME_BEFORE_LOAD_CRYSTAL);
#   })();
# }
# </script>
# <style>.absolute{position:absolute;}</style>
# <!--[if !IE]>|xGv00|2aa1984c50ef83d09fb459ec2203d70e<![endif]-->
#
# <div class="kjad2" style="position:relative">
#     <!--Tech_scroll_Width1_div AD begin...."l=Tech_scroll_Width1&log=off"-->
# <div id="Tech_scroll_Width1" style="width:960px;height:90px;" class="l_qq_com" ></div>
# <!--Tech_scroll_Width1 AD end --><!--[if !IE]>|xGv00|6472cac4d09fd562142c2b98b7e5ad1b<![endif]-->
#
# </div>
#   <style>
# .nopadding{padding:0!important}
# .undis,.undisplay{display:none!important}
# h1,h2,h3{font-weight:normal}
# a{color:#222}
# .wryh,.wryh a{font-family:'微软雅黑'!important}
# a:hover{color:#c00}
# a:focus{outline:0}
# .bold{font-weight:bold}
# .zuo{float:left}
# .you{float:right}
# img{border:0}
# .Q-tpList p{padding-right:10px}
# .Q-tpList li a,#ping .hd a{font-family:"宋体","Arial Narrow",HELVETICA}
# .layout{width:1000px;background:#fff;color:#222;font-family:"微软雅黑","Arial Narrow",HELVETICA}
# .Q-g16 .chief{width:660px}
# .Q-g16 .extra{width:300px}
# .noh{content:normal!important;text-decoration:none}
# .mt15{margin-top:15px}
# .mainnav{width:995px;height:35px;line-height:35px;margin:0 auto;padding-left:5px;background:#379be9;overflow:hidden}
# .mainnav li{float:left;background:url(http://img1.gtimg.com/tech/pics/hv1/214/72/1569/102042799.png) no-repeat right}
# .mainnav li.wpd{background:0}
# .mainnav li a{color:#fff;font-family:"微软雅黑","Arial Narrow",HELVETICA;font-size:16px;padding:0 14px;display:block;text-align:center;margin-right:1px}
# .mainnav li a:hover{background:#1873de;color:#fff;text-decoration:none}
# .mainnews{width:660px;overflow:hidden}
# .mainnews .pica{width:380px;height:300px;position:relative}
# .picd img{width:200px!important;height:130px!important}
# .mainnews .pica a{display:block}
# .mainnews .pica span a{display:block;color:#2662a3;font-family:"微软雅黑","Arial Narrow",HELVETICA;line-height:26px}
# .mainnews .pica span a:hover{color:#c00;text-decoration:none}
# .mainnews .pica span{display:block;position:absolute;left:5px;bottom:10px;cursor:pointer;height:auto;font-size:20px;color:#2662a3;padding:7px 5px 7px 0;width:370px;font-family:"微软雅黑","Arial Narrow",HELVETICA;line-height:26px}
# .mainnews .pica a span:hover{text-decoration:none;color:#c00}
# .chief .mainnews .pica img{width:380px;height:220px}
# .mainnews .fonta{margin-left:15px;overflow:hidden}
# .mainnews .fonta ul{width:680px}
# .mainnews .fonta .bordernone{border:0}
# #ping{width:660px;height:147px;border-top:1px solid #d2dceb;border-bottom:1px solid #d2dceb;margin-top:8px;position:relative}
# .ping_sm:hover{text-decoration:none}
# .kjrp{font-family:"微软雅黑";position:absolute;top:2px;left:90px;color:#000!important;display:block;cursor:pointer}
# #ping .hd{height:36px;line-height:36px;background:#e9eef4;padding:0 10px}
# #ping .hd img{margin-top:5px}
# #ping .hd a{color:#658aaf}
# #ScA2{overflow:hidden;zoom:1;height:110px;position:relative;width:660px}
# #ScA2 li{float:left;width:290px;height:82px;padding:0 5px;margin-top:5px}
# #ScA2 li .Q-tpList .xgm_zzxx{margin-top:10px;height:25px;overflow:hidden}
# #ScA2 .count{overflow:hidden;float:left}
# #ScA2 .cols2{position:absolute;top:20px;left:68px;overflow:hidden;zoom:1;width:666px}
# #ScA2 .cols{position:absolute;width:99999px}
# #ScA2 .prev{width:7px;height:13px;background:url(http://mat1.gtimg.com/tech/2012/2012keji/sjleft.png) no-repeat;display:block;position:absolute;top:47px;left:15px;cursor:pointer}
# #ScA2 .next{width:7px;height:13px;background:url(http://mat1.gtimg.com/tech/2012/2012keji/sjright.png) no-repeat;display:block;position:absolute;top:47px;left:650px;cursor:pointer}
# #ScA2 a.prev:hover{display:block}
# #ScA2 .wr{height:283px;position:relative;overflow:hidden}
# #ScA2 a.next:hover{display:block}
# #ScA2 .wr{height:283px;position:relative;overflow:hidden}
# #ScA2 .count{float:left}
# #ScA2 li .Q-tpList{width:290px;height:87px;overflow:hidden}
# #ScA2 li .Q-tpList a{font-family:"微软雅黑","Arial Narrow",HELVETICA;color:#222;font-size:14}
# #ScA2 li .Q-tpList a:hover{color:#c00;text-decoration:none}
# #ScA2 li .Q-tpList p{margin-top:10px;height:25px;overflow:hidden}
# #ScA2 li .Q-tpList img{width:80px;height:80px}
# #ScA2 li .q1{margin-right:15px}
# #ScA2 .prevMouseClass{background:url(http://mat1.gtimg.com/tech/2012/2012keji/sjleft.png) no-repeat}
# #ScA2 .nextMouseClass{background:url(http://mat1.gtimg.com/tech/2012/2012keji/sjright.png) no-repeat}
# .plArea{height:auto;clear:both;margin:20px auto 0 auto;position:relative}
# .plArea .closeBtn{width:15px;height:15px;clear:both;position:absolute;right:15px;top:8px;z-index:2}
# .plArea .closeBtn a{display:block;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/plbg.png) 0 -15px;width:15px;height:15px}
# .plArea .closeBtn a:hover{background-position:0 0}
# .plArea li{padding:18px 0;border-bottom:1px dotted #b8b9b9}
# .plArea li span{float:none}
# .plArea li span a{color:#4c7caa}
# .plArea li p{display:inline;line-height:24px;padding:0}
# .plContent{margin:0 auto;clear:both;position:relative}
# #pop_reply,#top_reply,.plContent .bd h2{width:630px;margin:0 auto}
# .plContent .hd{padding-right:38px;height:32px;overflow:hidden}
# .plContent .hd h2,.plContent .bd h2{font-family:"微软雅黑","Arial",HELVETICA;font-size:15px;color:#222}
# .plContent .bd h2{margin-bottom:10px}
# .plContent .hasCom{float:right;color:#666;height:32px;line-height:32px}
# .plContent .hasCom a{color:#4c7caa;margin-left:5px;width:60px;height:16px;margin-top:7px;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/plbg.png) 0 -130px no-repeat;float:right;text-indent:-10000px}
# .plContent .hasCom a:hover{background-position:-66px -130px}
# .plContent .hasCom em{color:#ff9000;font-weight:normal}
# .plContent .hasCom span{float:right}
# .plDinfo{clear:both}
# .plDinfo .logoinFrm{height:270px}
# .plDinfo textarea{width:618px;height:65px;border:1px solid #d8d8d8;outline:0;resize:none;padding:5px}
# .plDinfo textarea.fonts{color:#8c8d8e}
# .plDinfo .commt-sub{height:48px;line-height:48px;clear:both;position:relative;_left:15px}
# .plDinfo .commt-sub span.tips{color:#ff9000;position:absolute;right:90px}
# .plDinfo .commt-sub a{font-weight:normal;color:#455e85;font-family:simsun}
# .plDinfo .commt-sub input{vertical-align:middle}
# .plDinfo .commt-sub .submit{position:absolute;top:13px;width:56px;height:24px;border:0;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/plbg.png) -62px -156px no-repeat;right:0;text-indent:-10000px;cursor:pointer}
# .plDinfo .commt-sub .submiton{position:absolute;top:13px;width:56px;height:24px;border:0;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/plbg.png) 0 -156px no-repeat;right:0;text-indent:-10000px;cursor:pointer}
# .plDinfo .commt-sub a{color:#4c7caa}
# .plDinfo .commt-sub .fontsline{color:#999;position:absolute;right:72px;top:3px}
# .plDinfo .commt-sub .fontsline strong{font-size:26px;font-family:Georgia,Tahoma,Arial;font-weight:normal;padding:0 4px;position:relative;top:-5px;vertical-align:middle}
# .plDinfo div.comm_logined input{float:left;vertical-align:middle;margin-top:17px;*margin-top:12px;margin-right:3px}
# .plDinfo .cmt_status{color:#666;margin-left:107px;display:inline}
# .hotlist .newsinfo{position:relative;margin-bottom:20px}
# #login_list{height:auto}
# #cmt_jump_form{display:none}
# .newplArea{border:1px solid #e9e9e9;background:#f8f7f7;padding-top:0;border-bottom:0}
# .newplArea .login{float:left;margin-top:6px;line-height:20px}
# .newplArea .login img{float:left;vertical-align:middle;border-radius:2px}
# .newplArea .login .logoA{float:left;width:52px;height:19px;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/plbg.png) -58px -101px;text-indent:-10000px;margin-left:13px}
# .newplArea .login .logoA:hover{background-position:0 -101px}
# .newplArea .login a{font-family:"simsun"}
# .newplArea .login a.weiboName{color:#4468a1;margin:0 10px}
# .newplArea .login a.quitLogin{color:#8c8d8e}
# .newplArea .login a:hover{color:#c00}
# .newplArea .sucssTip{border:1px solid #e9e9e9;height:50px;line-height:50px;background:#fff;padding-left:18px;clear:both}
# .newplArea .sucssTip span{font-size:14px;color:#666;padding:5px 0 5px 30px;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/plbg.png) -60px -10px no-repeat}
# .plContent .bd h2{font-size:18px;font-family:"微软雅黑";color:#222;border-bottom:1px solid #eaeaea;height:35px;line-height:35px}
# .plContent .bd h2 span{float:left;border-bottom:2px solid #4197c9;padding-right:50px;padding-left:10px;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/plbg.png) 87px -61px no-repeat}
# .newplArea li{overflow:hidden;width:630px;margin:0 auto}
# .newplArea li .imgico{float:left;margin-top:3px;border-radius:2px}
# .newplArea li .fontsInfo{float:left;width:595px;font-size:14px;color:#666;margin-left:10px;display:inline}
# .newplArea li .fontsInfo a{color:#455e85;font-weight:800}
# .newplArea li .fontsInfo .timeDate{font-size:12px;color:#8c8d8e;margin-top:10px}
# .newplArea .morePl{height:25px;line-height:25px;background:#ebebeb;text-align:center}
# .newplArea .morePl a{color:#455e85;font-family:simsun}
# .newplArea .seeall{width:60px;height:16px;position:absolute;right:43px;top:8px;z-index:2}
# .newplArea .seeall a{display:block;width:60px;height:16px;color:#fff;font-family:'simsun';background:url(http://mat1.gtimg.com/digi/2012/shuma2013/plbg.png) 0 -130px no-repeat}
# .yellowColor{color:#ff9000}
# .plDinfo .commt-sub label{padding-top:6px;color:#333;float:left;color:#8c8d8e;font-size:13px}
# .plDinfo .commt-sub label input{vertical-align:0;margin-right:5px}
# .hottitle{width:660px;height:50px;line-height:50px;overflow:hidden;border:1px solid #e5e5e5;border-width:1px 0 1px 0;clear:both;margin-top:15px}
# .hottitle strong{color:#333;font-size:14px;height:48px;line-height:48px;margin-top:1px;background:#f9f9f9;width:80px;text-align:center;margin-right:10px}
# .hottitle ul{width:560px;line-height:50px;float:left}
# .hottitle ul li a{font-size:14px;padding:2px 6px;font-family:"宋体","Arial Narrow",HELVETICA}
# .hottitle ul li{float:left}
# .hottitle ul li a:hover{color:#fff!important;background:#2f91ff;text-decoration:none}
# .hottitle ul li a.on{background:#2f91ff;color:#fff}
# .hotlist h3 a{line-height:34px;padding:3px 2px}
# .hotlist p{font:12px/22px "宋体","Arial Narrow",HELVETICA;color:#666;padding:8px 0}
# .hotlist .newsinfo,.newsinfo a{color:#999;font-family:"宋体","Arial Narrow",HELVETICA}
# .hotbread .hottitle h2{font-size:12px;line-height:60px;padding-top:0}
# .hotbread .hottitle a{font-size:15px}
# .hotbread .hottitle a:hover{background:0;color:#222}
# .hotbread .hottitle strong{font-weight:normal;line-height:60px}
# .hotlist .newsinfo a{font-family:Arial;padding-left:20px;background:url("http://mat1.gtimg.com/tech/2012/2012keji/bg.png") 0 -48px no-repeat}
# .hotlist .newsinfo a:hover{background-position:0 -23px;text-decoration:none;color:#455e85}
# .hotlist .newsinfo em a{padding:0;background:0;color:#455e85;font-weight:normal;padding:2px 4px}
# .hotlist .newsinfo em a:hover{color:#fff;background:#4196e6}
# .hotlist .Q-tpList .pic img{border:1px solid #ccc}
# .hotlist .Q-tpList{padding:20px 0 0 0;border-bottom:1px solid #e9e9e9}
# #pageZone{padding-top:40px;overflow:hidden}
# #pageZone span{float:left;width:34px;height:34px;line-height:34px;border:1px solid #e2e2e2;text-align:center;margin-right:5px;font-size:14px;cursor:pointer}
# #pageZone span:hover{background:#258cff;color:#fff;text-decoration:none}
# #pageZone .Disabled{width:85px}
# #pageZone .Disabled a{display:block;width:85px}
# #pageZone span.isNow{background:#258cff;color:#fff}
# #pageZone span.count{display:none}
# #pageZone span.dot{border:0}
# #pageZone span a{display:block;height:34px}
# #pageZone span a:hover{color:#fff;text-decoration:none}
# .title .hd{height:40px;background:url(http://mat1.gtimg.com/tech/2012/2012keji/bg.png) 0 -257px no-repeat;line-height:35px;padding-left:10px}
# .title .hd h2 a,.title .hd h2{font-size:18px}
# .title .hd h2 a:hover{text-decoration:none}
# .title em a{font-family:"微软雅黑","宋体","Arial Narrow",HELVETICA}
# .people .bd{padding-top:15px}
# .people .Q-tpList{margin-bottom:29px}
# .people .Q-tpList p{font-family:"宋体","Arial Narrow",HELVETICA;color:#666}
# .science .hotuse .hd h2 a{font-size:16px}
# .science .hotuse .Q-tpList .pic img{border:0}
# .fontsl{padding:10px}
# .fontsl li a{font-size:14px}
# .fontsl li{line-height:24px}
# #focus2{margin-bottom:10px}
# .ued_focus_main a{display:none;background:#000}
# .ued_focus_main .current,.ued_focus_sub .current{display:block}
# .fs_A{margin:0 auto;width:300px;height:264px;margin-bottom:30px;position:relative;background:#000}
# .fs_A img{display:inline-block;border:1px solid #cbcbcb;width:298px;height:220px}
# .fs_A .fstitle{height:44px;line-height:44px;font-size:16px;background:#fff}
# .fs_A .fstitle span a{text-decoration:none}
# .fs_A i{font-style:normal}
# .fs_A .ued_focus_main{position:absolute;overflow:hidden;background:#000;left:0;top:40;width:100%}
# .fs_A .ued_focus_text{position:absolute;left:0;bottom:-1px;height:35px;font:bold 14px/35px "微软雅黑","Arial Narrow",HELVETICA;text-align:center;color:#fff;width:100%;background:rgba(0,0,0,0.4);filter:progid:DXImageTransform.Microsoft.gradient(GradientType = 0,startColorstr = '#40000000',endColorstr = '#40000000') \9}
# .fs_A .ued_focus_text a{display:none;outline:0;color:#fff;text-decoration:none}
# .fs_A .ued_focus_text a:hover{background:#2f91ff}
# .fs_A .ued_focus_text .current{display:block;color:#fff}
# .fs_A .ued_focus_sub{display:none}
# .f_preBtn,.f_nextBtn{position:absolute;cursor:pointer;width:21px;height:21px;top:12px}
# .fs_A .f_preBtn{right:28px}
# .fs_A .f_nextBtn{right:0}
# .fs_A .f_preBtn a,.fs_A .f_nextBtn a{width:21px;height:21px;display:block;background:url(http://mat1.gtimg.com/tech/2012/2012keji/bg.png) -116px -205px no-repeat;overflow:hidden}
# .fs_A .f_preBtn a{background:url(http://mat1.gtimg.com/tech/2012/2012keji/bg.png) -116px -226px no-repeat}
# .fs_A .f_preBtn a:hover{background-position:-137px -226px}
# .fs_A .f_nextBtn a:hover{background-position:-137px -205px}
# .hotuse{border-top:1px solid #cdd7e3;border-bottom:1px solid #cdd7e3}
# .hotuse .hd{background:0;padding:0;height:45px;line-height:42px}
# .hotuse .hd a{font-size:16px;text-decoration:none}
# .hotuse .bd{padding-bottom:15px}
# .hotuse .bd .Q-tpList p{font-family:"宋体","Arial Narrow",HELVETICA;color:#666;padding:5px 10px 0 5px}
# .hotuse .Q-tpList{margin-bottom:20px}
# .hotuse em a{font-family:"微软雅黑","Arial Narrow",HELVETICA}
# .hyq .Q-tpList{margin-bottom:30px}
# .hyq .Q-tpList em{display:block;line-height:26px;padding-bottom:8px;font-weight:normal}
# .hyq .Q-tpList em a{text-decoration:none}
# .hyq .Q-tpWrap em{padding-bottom:0}
# .hyq ul{padding-top:15px}
# .hyq li{padding-left:12px;background:url(http://mat1.gtimg.com/tech/2012/2012keji/icodot.png) 0 10px no-repeat;height:23px;overflow:hidden}
# .hyq .topb{border-top:1px solid #cdd7e3;padding-top:10px}
# .footer{background:#edf2f8;width:1000px;margin-top:70px;width:100%;display:block;clear:both;border-top:1px solid #cdd7e3}
# .footer0{background:#fff}
# .footer0 .tcopyright{background:0;border-top:1px solid #e9e9e9}
# .fooinner{width:1000px;margin:0 auto;color:#222}
# .fooinner .hd h2{height:50px;line-height:50px;font-family:"微软雅黑","Arial Narrow",HELVETICA}
# .fooinner .hd h2 a{color:#222;font-size:18px}
# .footer .Q-tpList .pic img{border-color:#2f3438}
# .footer #listZone img{width:100px;height:65px}
# .ent{padding-bottom:10px;border-bottom:1px solid #d7e0ee}
# .ent .Q-tpList em a{color:#28508e;font-family:"宋体","Arial Narrow",HELVETICA;font-weight:normal}
# .ent .Q-tpList em a:hover{text-decoration:none;color:#258cff}
# .ent .bigpic{width:495px}
# .ent .bigpic .pic{margin-right:15px}
# .ent .bigpic em{line-height:30px}
# .ent .Q-tpList p{margin-top:5px}
# .ent .smallpic{width:505px}
# .ent .smallpic em{line-height:15px}
# .ent .smallpic .Q-tpList{padding-bottom:17px}
# .ent .smallpic em a{font-size:14px;color:#555;font-family:"微软雅黑","Arial Narrow",HELVETICA;line-height:1.6em}
# .ent .smallpic .Q-tpList{width:245px;float:left;margin:0 0 14px 7px;display:inline}
# .ent .smallpic p a{color:#258cff}
# .friend{border-bottom:0;padding-bottom:15px}
# .friend .bd{font-family:Tahoma;color:#666;font-size:12px}
# .friend .bd a{color:#333;font-family:Tahoma;line-height:26px;padding:0 4px;*padding:0 4px 0 3px}
# .friend .bd a:hover{text-decoration:none;color:#258cff}
# .kjad2{margin:10px auto 0 auto;width:1000px;height:90px;clear:both}
# .Q-tpList .Q-tpWrap{font-family:"宋体","Arial Narrow",HELVETICA;line-height:21px;color:#666}
# .fooinner .Q-tpList .Q-tpWrap{color:#222}
# .v{background-image:url(http://mat1.gtimg.com/www/images/qq2012/icobg_1.4.png);background-repeat:no-repeat;padding-left:20px!important;background-position:left -270px;margin-left:10px!important}
# .v_rw{background:url(http://img1.gtimg.com/tech/pics/hv1/242/252/1157/75298427.png) no-repeat right -214px;background-position:0 5px;padding-left:23px}
# .rw_zf_h{background:url("http://mat1.gtimg.com/tech/00Jamesdu/index/rw_zf_h.jpg") no-repeat right;padding-left:50px;background-position:0 3px}
# .t{background:url("http://mat1.gtimg.com/www/iskin960/tico.png") no-repeat right center;padding-right:13px}
# #hotnews div.Q-tpList:hover{background:#f9fafd}
# a.dujia{background:url(http://mat1.gtimg.com/tech/2010/dj.gif) right center no-repeat;padding-right:37px}
# #tcopyright{width:1000px;margin:15px auto 0 auto;padding:10px 0;font-size:12px;line-height:28px;color:#666;text-align:center;overflow:hidden;clear:both;background:url(http://mat1.gtimg.com/tech/2012/2012keji/line00.png) center top no-repeat}
# #tcopyright .en{font-family:Arial}
# #tcopyright a{color:#666;text-decoration:none;font-family:"宋体","Arial Narrow",HELVETICA}
# #tcopyright a img{display:none}
# #tcopyright a:hover{color:#bd0a01;text-decoration:underline}
# #tab .hd{height:74px;padding:0;margin-top:15px}
# #tab h2{background:url(http://mat1.gtimg.com/tech/2012/2012keji/titleph.png) no-repeat;padding-left:10px;width:290px}
# #cardBtn1{height:38px;width:300px;background:url(http://mat1.gtimg.com/tech/2012/2012keji/title_bgg.png) top repeat-x;display:block;clear:both;border-top:1px solid #a8a8a8}
# #cardBtn1 li{width:100px;height:38px;float:left;text-align:center;color:#333;font-size:14px}
# #cardBtn1 li.current{background:url(http://mat1.gtimg.com/tech/2012/2012keji/plhover.png) center bottom no-repeat;color:#232323}
# #cardBtn1 li span{display:block;cursor:pointer;background:url(http://mat1.gtimg.com/tech/2012/2012keji/fengexian.png) right no-repeat}
# #tab #t0 span{background:0}
# #cardBody1{border:1px solid #e6e6e6;border-top:2px solid #e6e6e6}
# #cardBody1 li{padding:10px 0;border-bottom:1px solid #e6e6e6;overflow:hidden}
# #cardBody1 li a.picaa{padding-right:10px}
# .f18 a:hover{text-decoration:none;color:#fff;background:#4196e6}
# .hotlist .newsinfo a{font-family:Arial;background:url("http://mat1.gtimg.com/tech/2012/2012keji/bg.png") 0 -48px no-repeat}
# .plBtn span{display:block;padding-left:22px;height:20px;padding-bottom:10px;width:auto;background:url(http://mat1.gtimg.com/tech/00Jamesdu/2014/index/remark/3.png) 0 0 no-repeat;font-weight:800;float:right;cursor:pointer}
# .plBtn span.sf1{width:18px;height:20px;background:url(http://mat1.gtimg.com/tech/00Jamesdu/2014/index/remark/1.png) 0 0 no-repeat!important;font-weight:800;padding-left:0}
# .plBtn span.sf2{background-position:0 -74px}
# .plBtn span.lj1,.plBtn span.lj2,.plBtn span.lj3{height:20px}
# .plBtn span.lj1{padding-left:20px;background:url(http://mat1.gtimg.com/tech/00Jamesdu/2014/index/remark/3.png)0 0 no-repeat!important;padding-top:0;color:#ff9000;font-weight:800}
# .plBtn span.lj2{padding-left:26px;background:url(http://mat1.gtimg.com/tech/00Jamesdu/2014/index/remark/3.png) 0 0 no-repeat;color:#ff9000}
# .plBtn span.lj3{padding-left:26px;background:url(http://mat1.gtimg.com/tech/00Jamesdu/2014/index/remark/3.png) 0 0 no-repeat;color:#ff9000}
# .plArea li p .lk_jiav{display:inline-block;vertical-align:baseline;padding:0 0 0 32px;font-size:12px;color:#888;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/linkai/jiav.gif) no-repeat 8px 0;height:20px;line-height:17px;}
# .plArea li p .lk_city{color:#777;margin-left:10px;display:inline-block;height:18px;line-height:17px;}
# .mainnews .pica span a img{width:81px!important;height:25px!important}
# .mainnews .pica span .tmt_tech{float:left!important;margin-top:0;*margin-top:-4px;margin-right:5px}
# .f18 a:hover{text-decoration:none;color:#fff;background:#4196e6}
# .hotlist .newsinfo a{font-family:Arial;background:url("http://mat1.gtimg.com/tech/2012/2012keji/bg.png") 0 -48px no-repeat}
# .fPic ul li{list-style-type:none;padding:0;margin:0; width:300px;height:220px;float:left}
# .mainnews .pica span a:hover{color:#258cff}
# .people{margin-top:6px;margin-bottom:5px}
# #ScA3 .count .form a{width:200px!important;text-align:left!important}
# #ScA3 li{position:relative}
# #ScA3 li .form{position:absolute;bottom:17px;right:60px;height:auto!important}
# #ScA3 li .form a{height:auto!important}
# a{font-family:"微软雅黑","Arial",HELVETICA}
# .title .hd{background:url(http://mat1.gtimg.com/tech/newIndex2012/newPng.png) no-repeat 0 35px;padding-left:0}
# .title .hd h2 a{padding:0 10px;border-bottom:3px solid #258cff;display:block}
# .title .hd h2 a:hover{border-bottom:3px solid #1e617d}
# .hyq .hd h2,.science .hd h2,.peoTalk .hd h2{padding-left:10px}
# #focus4{background:0;height:234px}
# #focus4 .ued_focus_main{width:300px;height:191px;display:none}
# #focus4 .focus_tit4{width:300px;height:191px;left:0}
# #focus4 .ued_focus_text{width:300px;height:191px;left:0;background:url(http://mat1.gtimg.com/tech/newIndex2012/djtBg.png) no-repeat}
# #focus4 .ued_focus_text a:hover{background:0}
# #focus4 .ued_focus_text .current{color:#666;font-size:12px;font-family:"宋体";text-align:left;padding:20px 25px 0 30px;font-weight:400}
# #focus4 .ued_focus_text .current .cont{color:#000;font-family:"微软雅黑";font-size:16px;padding:0 0 20px 10px;height:105px;display:block}
# #focus4 .ued_focus_text .current .cont strong{font-weight:400;font-size:22px}
# .hotuse .hd{border-bottom:1px solid #dbdbdb;margin-bottom:0}
# .hotuse{border-bottom:1px solid #dbdbdb;border-top:0}
# .science .bd{height:270px;overflow:hidden}
# #tab h2{background:url(http://mat1.gtimg.com/tech/00Jamesdu/201404/newpng.png) no-repeat 0 35px;margin-bottom:15px}
# .hyq .topb{border-top:1px solid #dbdbdb}
# #cardBtn1{background:url(http://mat1.gtimg.com/tech/newIndex2012/zakNavBg.png) repeat-x;height:30px}
# #cardBtn1 li{height:30px;line-height:30px}
# #cardBtn1 li span{background:url(http://mat1.gtimg.com/tech/newIndex2012/zakNavline.png) no-repeat right 0}
# #cardBtn1 li.current{background:url(http://mat1.gtimg.com/tech/newIndex2012/botcur.png) center bottom no-repeat;height:33px}
# .phb{background:#f7f7f7}
# .phb .tabBody ul li{height:35px;line-height:18px;width:280px;position:relative;overflow:hidden;zoom:1;border-bottom:1px solid #e6e6e6}
# .phb .tabBody ul li img{border:1px solid #dadada}
# .phb .tabBody ul li a{color:#1d1d1d;padding-right:5px;font-size:14px}
# .phb .tabBody ul li a:hover{color:#fa6768!important}
# .phb .tabBody ul li .num{display:block;width:48px;text-align:center;color:#dadada;font-size:22px;float:left;font-family:Verdana,Geneva,sans-serif;height:35px;line-height:35px}
# .n_hot{color:#fa6768!important}
# .n_hei em,.n_hei em a{color:#fa6768!important}
# .phb .tabBody ul li em{position:absolute;right:5px;bottom:0}
# .phb .tabBody ul li a:hover{color:#fa6768!important}
# .phb .tabBody ul li em,.phb .tabBody ul li em a{font-size:12px;color:#258cff;font-family:"Arial","宋体",HELVETICA;padding-right:0!important}
# .phb .tabBody ul li span{height:35px;overflow:hidden}
# .phb .plph_1 ul li em a:hover{color:#c00}
# .n_hei a{color:#000!important}
# #cardBody1 li{width:100%}
# .qislu .hd{margin-bottom:5px}
# .hotlist h3.f18{font-size:20px}
# .hotlist h3 a{color:#000}
# .hotlist p.l23 a{background:url(http://mat1.gtimg.com/tech/newIndex2012/newPng.png) no-repeat 27px -99px;*background-position:27px -96px;_background-position:27px -97px;padding-right:20px;padding-bottom:1px;color:#2662a3;margin-left:5px;zoom:1}
# .hotlist p a:hover{color:#c00}
# .plBtn{position:relative;right:auto;display:inline;border:solid #ccc;border-width:0 1px;height:18px;padding:0 7px 0 7px;overflow:hidden}
# .plBtn span{display:inline;float:none}
# .newsinfo .fl{display:block;float:inherit;position:relative;padding-bottom:5px}
# .newsinfo .tag{overflow:hidden;zoom:1;padding-top:10px}
# .newsinfo .tag em{height:22px;line-height:22px;font-size:14px;font-family:"微软雅黑";color:#fff;margin-right:8px;display:block;float:left}
# .newsinfo .tag em a{background:#258cff url(http://mat1.gtimg.com/tech/newIndex2012/tagcur.png) no-repeat right 0;color:#fff;line-height:22px;display:block;height:22px;float:left;padding:0 15px 0 5px;font-family:"微软雅黑"}
# .newsinfo .tag em a:hover{background:#1e617d url(http://mat1.gtimg.com/tech/newIndex2012/tagcurHoverW.png) no-repeat right 0}
# .newsinfo .newplArea{clear:both}
# .newplArea{clear:both}
# .fuzixun{background:url(http://mat1.gtimg.com/tech/newIndex2012/fuzixun.png) no-repeat;width:63px;height:64px;_background:0;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,sizingMethod=crop,src='http://mat1.gtimg.com/tech/newIndex2012/fuzixun.png')}
# .diezhao{background:url(http://img1.gtimg.com/tech/pics/hv1/4/254/1655/107681149.png) no-repeat;width:63px;height:64px;_background:0;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,sizingMethod=crop,src='http://img1.gtimg.com/tech/pics/hv1/4/254/1655/107681149.png')}
# .shipin{background:url(http://mat1.gtimg.com/tech/newIndex2012/shipin.png) no-repeat;width:63px;height:64px;_background:0;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,sizingMethod=crop,src='http://mat1.gtimg.com/tech/newIndex2012/shipin.png')}
# .dujia{background:url(http://mat1.gtimg.com/tech/newIndex2012/dujia.png) no-repeat;width:63px;height:64px;_background:0;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,sizingMethod=crop,src='http://mat1.gtimg.com/tech/newIndex2012/dujia.png')}
# .zhuanfang{background:url(http://mat1.gtimg.com/tech/dc_new/zhuanfang.png) no-repeat;width:64px;height:63px;_background:0;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,sizingMethod=crop,src='http://mat1.gtimg.com/tech/dc_new/zhuanfang.png')}
# .bizwz{background:url(http://mat1.gtimg.com/tech/00Jamesdu/2015/en/bi/images/bi.png) no-repeat;width:64px;height:63px;_background:0;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,sizingMethod=crop,src='http://mat1.gtimg.com/tech/00Jamesdu/2015/en/bi/images/bi.png')}
# .recode{background:url(http://mat1.gtimg.com/tech/00Jamesdu/2015/en/recode/images/recode.png) no-repeat;width:64px;height:63px;_background:0;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,sizingMethod=crop,src='http://mat1.gtimg.com/tech/00Jamesdu/2015/en/recode/images/recode.png')}
# .tnwzwz{background:url(http://mat1.gtimg.com/tech/00Jamesdu/2015/en/tnw/tnw.png) no-repeat;width:64px;height:63px;_background:0;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,sizingMethod=crop,src='http://mat1.gtimg.com/tech/00Jamesdu/2015/en/tnw/tnw.png')}
# .diezhao,.fuzixun,.shipin,.dujia,.zhuanfang,.bizwz,.recode,.tnwzwz{text-indent:-999em;overflow:hidden;position:absolute;left:-4px;top:1px;z-index:9999999}
# .hotlist .Q-tpList .Q-tpListInner{position:relative;width:100%}
# #listZone .Q-tpList .pic{position:relative;z-index:100;margin-top:4px}
# .rwzpeople .Q-tpList{height:101px;margin-bottom:21px}
# .updateTime{padding-left:3px}
# .fs_A{z-index:10;background:#fff}
# .hotlist .newsinfo{position:relative;z-index:79}
# .hotlist .newsinfo .aTime{padding-right:5px}
# .science .bd{position:relative}
# .science .fstitle{font-size:16px;position:absolute;z-index:999;left:0;top:0;height:44px;line-height:44px}
# .fs_D1{width:298px;height:250px;position:relative;top:15px}
# .fs_D1 .fPic{left:0;padding-top:30px}
# .fs_D1 .D1fBt{overflow:hidden;zoom:1;height:16px;z-index:10}
# .fs_D1 .shadow{width:100%;position:absolute;bottom:0;left:0;z-index:9999;height:34px;display:block;line-height:34px;text-align:center;zoom:1}
# .fs_D1 .shadow a{text-decoration:none;color:#fff;font-size:14px;font-weight:bolder;overflow:hidden;margin-left:10px}
# .fs_D1 .fcon{width:100%;float:left;display:none;background:#000}
# .fs_D1 .fcon img{display:block;width:298px;height:220px}
# .fs_D1 .fbg{width:304px;background:#000;bottom:0;left:0;position:absolute;height:21px;text-align:center;display:none}
# .fs_D1 .fbg div{margin:4px auto 0;overflow:hidden;zoom:1;height:14px}
# .fs_D1 .D1fBt a{display:inline-block;background:url(http://mat1.gtimg.com/news/base2011/foucs/img/A_tip.png);width:14px;height:14px;position:relative;margin:0 2px;outline:0;text-decoration:none}
# .fs_D1 .D1fBt .current,.fs_D1 .D1fBt a:hover{background:url(http://mat1.gtimg.com/news/base2011/foucs/img/A_tip_current.png)}
# .fs_D1 .D1fBt img{display:none}
# .fs_D1 .D1fBt i{display:none;font-style:normal}
# .fs_D1 .prev,.fs_D1 .next{position:absolute;width:21px;height:21px;top:0}
# .fs_D1 .prev a,.fs_D1 .next a{display:block;width:21px;height:21px}
# .fs_D1 .prev{right:30px}
# .fs_D1 .prev a{background:url(http://mat1.gtimg.com/tech/2012/2012keji/bg.png) -116px -226px no-repeat}
# .fs_D1 .prev a:hover{background-position:-137px -226px}
# .fs_D1 .next{right:0}
# .fs_D1 .next a{background:url(http://mat1.gtimg.com/tech/2012/2012keji/bg.png) -116px -205px no-repeat}
# .fs_D1 .next a:hover{background-position:-137px -205px}
# .covermask{position:absolute;z-index:5;width:298px;height:34px;background:#000;opacity:.6;filter:alpha(opacity=60);left:0;bottom:0;*bottom:-1px;zoom:1}
# .infomap{position:relative;padding-bottom:15px}
# .infomap .fstitle{font-size:16px;position:absolute;z-index:999;left:0;top:0;height:44px;line-height:44px}
# .fs_D1 .prev2,.fs_D1 .next2{position:absolute;width:21px;height:21px;top:0}
# .fs_D1 .prev2 a,.fs_D1 .next2 a{display:block;width:21px;height:21px}
# .fs_D1 .prev2{right:30px}
# .fs_D1 .prev2 a{background:url(http://mat1.gtimg.com/tech/2012/2012keji/bg.png) -116px -226px no-repeat}
# .fs_D1 .prev2 a:hover{background-position:-137px -226px}
# .fs_D1 .next2{right:0}
# .fs_D1 .next2 a{background:url(http://mat1.gtimg.com/tech/2012/2012keji/bg.png) -116px -205px no-repeat}
# .fs_D1 .next2 a:hover{background-position:-137px -205px}
# #ScA3{height:220px;position:relative;width:300px;top:8px}
# #ScA3 li{float:left;width:300px;height:191px;padding:0 5px;margin-top:5px;background:url(http://mat1.gtimg.com/tech/dc_new/jryBg.png) 0 bottom no-repeat}
# #ScA3 li .Q-tpList .xgm_zzxx{margin-top:10px;height:25px;overflow:hidden}
# #ScA3 .count{overflow:hidden;float:left;height:191px}
# #ScA3 .cols2{position:absolute;top:20px;left:68px;overflow:hidden;zoom:1;width:666px}
# #ScA3 .cols{position:absolute;width:99999px}
# #ScA3 .prev3{width:21px;height:21px;background:url(http://mat1.gtimg.com/tech/2012/2012keji/bg.png) -116px -226px no-repeat;display:block;position:absolute;right:30px;cursor:pointer;top:0}
# #ScA3 .next3{width:21px;height:21px;background:url(http://mat1.gtimg.com/tech/2012/2012keji/bg.png) -116px -205px no-repeat;display:block;position:absolute;top:0;right:0;cursor:pointer}
# #ScA3 a.prev3:hover{display:block;background-position:-137px -226px}
# #ScA3 .wr{height:283px;position:relative;overflow:hidden}
# #ScA3 a.next3:hover{display:block;background-position:-137px -205px}
# #ScA3 .wr{height:283px;position:relative;overflow:hidden}
# #ScA3 .count{float:left}
# #ScA3 li .Q-tpList{width:300px;height:185px;overflow:hidden;cursor:pointer}
# #ScA3 li .Q-tpList .Q-tpWrap{height:185px}
# #ScA3 li .Q-tpList a{font-family:"微软雅黑","Arial Narrow",HELVETICA;color:#222;display:block;width:300px;height:185px}
# #ScA3 li .Q-tpList a:hover{color:#c00;text-decoration:none}
# #ScA3 li .Q-tpList p{margin-top:10px;height:25px;overflow:hidden}
# #ScA3 li .Q-tpList img{width:80px;height:80px}
# #ScA3 li .q1{margin-right:15px}
# #ScA3 .prevMouseClass3{background-position:-137px -226px}
# #ScA3 .nextMouseClass3{background-position:-137px -205px}
# #ScA3 .count .cont a{color:#000;font-family:"微软雅黑";font-size:14px;padding:20px 60px 20px 45px;height:115px;width:200px;display:block;line-height:32px;text-align:justify}
# #ScA3 .count .cont strong{font-weight:400;font-size:20px}
# #ScA3 .count .form a{color:#666;display:block;padding-left:40px;width:200px;text-align:right;font-family:"宋体"}
# .mainnews .pica{width:410px}
# .chief .mainnews .pica img{width:410px;height:300px}
# .mainnews .pica .cover{position:absolute;width:410px;height:75px;background:#000;opacity:.6;filter:alpha(opacity=60);bottom:0;z-index:5}
# .mainnews .pica span{z-index:10;left:10px;width:390px;*bottom:0}
# .mainnews .pica span a{color:#fff}
# .mainnews .pica span a img{width:78px;height:21px;width:78px!important;height:21px!important;margin-top:2px}
# .mainnews .fonta{margin-left:0}
# .rwzpeople .bd{overflow:hidden;height:220px}
# .rwzpeople .Q-tpList{margin-bottom:15px}
# .pingandqsl{overflow:hidden;zoom:1;border-bottom:1px solid #dcdcdc}
# .pingandqsl .mod1{width:300px;float:right;overflow:hidden}
# .pingandqsl .mod1 .hd{height:36px;padding-top:10px;line-height:36px;font-family:"微软雅黑";color:#000;border-bottom:3px solid #258cff;padding-bottom:2px}
# .pingandqsl .mod1 .hd h2{font-size:19px}
# .cate_box .fr{position:absolute;bottom:5px;left:110px}
# #pingpart .fr{left:80px}
# .mr10{margin-right:20px}
# .pingandqsl .mod1 ul{margin-top:10px;font-family:"黑体"}
# .pingandqsl .mod1 li a{background:url(http://mat1.gtimg.com/tech/2012/2012keji/dot.png) no-repeat 0 center;font-size:14px;padding-left:15px;color:#000}
# .pingandqsl .mod1 li a:hover{color:#c00}
# #pingpart .hd img{border:0}
# .hotuse{border-bottom:1px solid #dcdcdc}
# .infomap{border-top:1px solid #dcdcdc}
# .fontsl li{background:url(http://mat1.gtimg.com/tech/2012/2012keji/dot.png) no-repeat 0 center;padding-left:15px}
# #ScA4{height:180px;position:relative;width:300px;top:0}
# #ScA4 li{float:left;width:290px;height:180px;padding:0 5px;background:#f9fafd}
# #ScA4 .count{float:left;height:191px}
# #ScA4 .cols2{position:absolute;top:20px;left:68px;overflow:hidden;zoom:1;width:666px}
# #ScA4 .cols{position:absolute;width:99999px}
# #ScA4 .prev4,.ks_tabs .prev11,.ks_tabs .prev22,.ks_tabs .prev33{width:21px;height:21px;background:url(http://mat1.gtimg.com/tech/2012/2012keji/bg.png) -116px -226px no-repeat;display:block;position:absolute;right:30px;cursor:pointer;top:-34px}
# #ScA4 .next4,.ks_tabs .next11,.ks_tabs .next22,.ks_tabs .next33{width:21px;height:21px;background:url(http://mat1.gtimg.com/tech/2012/2012keji/bg.png) -116px -205px no-repeat;display:block;position:absolute;top:-34px;right:0;cursor:pointer}
# #ScA4 .prevMouseClass4,.ks_tabs .prev11 a:hover,.ks_tabs .prev22 a:hover,.ks_tabs .prev33 a:hover,#ScA4 .prev4:hover{background-position:-137px -226px}
# #ScA4 .nextMouseClass4,.ks_tabs .next11 a:hover,.ks_tabs .next22 a:hover,.ks_tabs .next33 a:hover,#ScA4 .next4:hover{background-position:-137px -205px}
# #ScA4 .count h3{font-size:16px;font-family:"微软雅黑";padding:10px 0}
# #ScA4 .count p{line-height:26px;overflow:hidden;zoom:1;padding:5px 0}
# #ScA4 .count p span{display:block;width:26px;height:26px;text-align:center;color:#fff;background:#258cff;font-size:14px;font-family:"微软雅黑";margin-right:15px;float:left}
# #ScA4 .count p a{font-family:"宋体"}
# #ScA4 .join{text-align:right;position:relative}
# #ScA4 .join .pComment{overflow:hidden}
# #ScA4 .join .pComment,#ScA4 .join .shareTo{position:relative;top:0}
# #ScA4 .join .voteBtn{position:relative;top:-2px}
# #ScA4 .join .shareTo{margin:0 5px;bottom:0;top:auto}
# #ScA4 .shareTo .share{left:-160px;text-align:left;*top:16px}
# .shumakong{position:relative;border-top:1px solid #dcdcdc}
# .shumakong .fstitle{font-size:16px;height:44px;line-height:44px}
# .shumakong .fs_D1{top:0;height:220px;margin-bottom:10px}
# .shumakong .fPic{padding-top:0}
# .ks_tabs .prev11 a,.ks_tabs .next11 a,.ks_tabs .prev22 a,.ks_tabs .next22 a,.ks_tabs .prev33 a,.ks_tabs .next33 a{display:block;height:21px;height:21px;background-image:url(http://mat1.gtimg.com/tech/2012/2012keji/bg.png);background-repeat:no-repeat;background-position:100px 100px}
# .hotuse .bd{background:#fff;padding-bottom:20px}
# #focus2{border-top:1px solid #dcdcdc}
# .pComment a{padding-left:22px;height:18px;width:auto;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/hotico.png) 0 -124px no-repeat;font-weight:800;color:#999}
# .pComment a.sf1{padding-left:20px;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/hotico.png) 0 -164px no-repeat;font-weight:800}
# .pComment a.sf2{background-position:0 -74px}
# .pComment a.lj1{padding-left:20px;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/hotico.png) 0 -1px no-repeat;color:#ff9000;font-weight:800}
# .pComment a.lj2{padding-left:33px;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/hotico.png) 0 -37px no-repeat;color:#ff9000;padding-bottom:2px}
# .pComment a.lj3{padding-left:26px;background:url(http://mat1.gtimg.com/digi/2012/shuma2013/hotico.png) 0 -78px no-repeat;color:#ff9000;padding-bottom:2px}
# .ent .bigpic{overflow:hidden}
# .fontright ul li{overflow:hidden}
# .footer .Q-tpList .pic{_margin-right:5px}
# .fooinner,#tcopyright{background:#edf2f8}
# .fooinner{overflow:hidden;border-top:1px solid #cdd7e3}
# .footer{background:#edf2f8 url(http://mat1.gtimg.com/tech/dc_new/footborder.png) repeat-x 0 0;border-top:0}
# .jdtdBg{width:660px;position:relative}
# .jdtdBg .plLink,#ks_re a.heli_com3210{line-height:22px;background:0;border:0;font-size:12px;font-family:"宋体";font-weight:normal;color:#777}
# .jdtdBg .plLink a,#ks_re a.heli_com3210{background:url(http://mat1.gtimg.com/tech/00Jamesdu/index/pl.png) no-repeat 0 3px;line-height:18px;padding:0;padding-left:20px;color:#000}
# #ks_re a.heli_com3210{background-position:0 0;margin-left:10px;color:#8b8b8b}
# .jdtdBg .top{text-align:center;position:absolute;left:0;bottom:0}
# .jdtdBg .top img{vertical-align:middle}
# .jdtdBg h2{height:40px;padding:6px 0 10px;font-family:"微软雅黑";font-size:30px;overflow:hidden;font-weight:bold}
# .jdtdBg h2 a{color:#252525}
# .jdtdBg h2 a:hover{text-decoration:none;color:#c00}
# .jdtdBg .detail{padding:0 0 10px;overflow:hidden;color:#b0b8b9;font-family:"微软雅黑";line-height:22px;font-size:12px;color:#010101}
# .jdtdBg .detail div{width:550px;float:left;color:#666}
# .jdtdBg .detail a{color:#666}
# #heli_com321{color:#000}
# .jdtdBg .dibg{width:660px;position:relative}
# .jdtdBg .txt{padding-left:5px}
# .jdtdBg .leftImg{position:absolute;left:0;top:0;z-index:1}
# .jdtdBg .leftImgLink{position:absolute;left:0;top:0;z-index:99}
# .jdtdBg .leftImgLink a{display:block;width:265px;height:221px}
# .mainnews .fonta{overflow:hidden;border-top:1px solid #dedede}
# .mainnews .fonta li{float:left;line-height:26px;overflow:hidden;background-position:5px 21px;border-top:1px solid #e5e5e5;width:320px;height:70px;margin:-1px 0 0 0;padding:16px 20px 10px 0}
# .mainnews .fonta li a{font-size:16px;margin:16px 0 0 0;display:inline;overflow:hidden}
# .mainnews .fonta li a:hover{text-decoration:none}
# .mainnews .fonta li a.color_black{font-size:12px;color:#fff;padding:3px 5px;background:#4482ea;margin-left:10px;font-family:"宋体",Arial;letter-spacing:1px}
# .mainnews .fonta li a.color_black:hover{background:#4482ea!important}
# .mainnews .fonta li a.color_red{font-size:12px;color:#4482ea;text-decoration:underline;padding:3px 5px;margin-left:10px;font-family:"宋体",Arial}
# .mainnews .fonta li a.color_red:hover{color:#c00}
# .mainnews .fonta li a.noh,.mainnews .fonta li a.noh:hover{cursor:normal!important;background:#fb6600}
# .mb15{margin-bottom:15px}
# .mbx{border-top:0;margin-top:0}
# .mbx .fl{font-size:14px}
# .mbx .dyq{color:#ddd}
# .techTag{padding-left:0}
# .font_w_b{font-weight:bold}
# .color_black{color:#000}
# .color_red{color:#c00!important}
# .STYLE1{font-weight:bold}
# .cate_box{position:relative;height:40px;background:#f7f7f7;border-top:2px solid #626262}
# .cate_box h2{position:absolute;bottom:4px;left:0}
# #ks_qukeji .cate_box h2{bottom:4px}
# .cate_box h2 a{font-size:18px}
# .cate_box h2 a:hover{text-decoration:none}
# .cate_box .more_link{position:absolute;right:10px;bottom:4px;font-family:"宋体";color:#8b8b8b}
# .cate_box .more_link:hover{text-decoration:none;color:#C00}
# .ks_tabs .fcon_box .fcon{overflow:hidden}
# .ks_tabs .fcon_box{width:300px;height:220px;position:relative}
# .ks_tabs .fcon{display:none}
# .ks_tabs .fcon img{display:block;width:300px;height:220px;z-index:222}
# .ks_tabs .text_c{width:100%;line-height:42px;background:url(http://img1.gtimg.com/tech/pics/hv1/182/28/1590/103397072.png) repeat-x;position:absolute;bottom:0;left:0;text-align:center}
# :root .ks_tabs .text_c{filter:none;background:url(http://img1.gtimg.com/tech/pics/hv1/182/28/1590/103397072.png) repeat-x}
# .ks_tabs .text_c h3,.ks_tabs .text_c h3 a{color:#fff}
# .ks_tabs .text_c h3{margin-bottom:-5px}
# .ks_tabs .text_c .f12{color:#ccc}
# .ks_tabs .dot_box{height:15px;text-align:center;padding:17px 0}
# .ks_tabs .dot_box a{display:inline-block;height:15px;width:15px;overflow:hidden;background:url("http://mat1.gtimg.com/tech/2013ks/images/dots.png") no-repeat scroll;margin:0 5px}
# .ks_tabs .dot_box a.current{background-position:-15px 0}
# .Q-tpWrap a.pic{float:left;margin-right:10px}
# .Q-tpWrap a.pic img{border:1px solid #ebebeb}
# #ks_ping2014 .Q-tpWrap{margin:10px 0}
# #ks_ping2014 a.pic img,#ks_linkedin a.pic img{width:65px;height:65px}
# #ks_linkedin ul li{padding:5px 0 0 0;*padding:3px 0 0 0;margin:0!important;overflow:hidden;position:relative;height:87px}
# #ks_linkedin .f16 a{line-height:34px;margin-top:-10px}
# #ks_linkedin a.pic img{margin-top:10px}
# #ks_linkedin .bd{padding-top:0;height:190px!important;overflow:hidden}
# #ks_linkedin{width:300px;height:240px;overflow:hidden!important;margin-top:1px;*margin-bottom:3px}
# #ks_linkedin li.xuxnain{border-bottom:1px solid #ebebeb}
# #ks_qukeji ul img{width:300px;height:220px}
# .r_zut ul li img{width:300px;height:220px}
# .pingandqsl .bd{position:relative;width:300px;overflow:hidden}
# .pingandqsl .mod1 a{display:block;font-family:"微软雅黑";font-size:16px;line-height:34px;color:#333}
# .pingandqsl .mod1 a:hover{color:#c00}
# .pingandqsl .mod1 a img{vertical-align:top}
# .mainnews .pica .cover{opacity:.8!important;filter:alpha(opacity=80)!important}
# #ScA3 .count .form a{padding-left:10px;width:230px}
# .pingandqsl{border-bottom:0;padding-bottom:0;margin-top:2px}
# .pingandqsl .bd .cover{left:1px;width:300px}
# .trx_ti{padding-top:5px}
# #ks_digit .cate_box{border-bottom-color:#000}
# #ks_digit{background:#f7f7f7}
# #ks_infomap .cate_box{border-bottom-color:#4c85d2}
# .xxskj{padding:30px 0}
# .hotlist .Q-tpList .pic img{max-width:300px;max-height:220px}
# .dz_book img{width:56px!important;height:55px!important}
# .zlda_1 .text_c{height:55px;padding:0;width:300px}
# .zlda_1 li{position:relative}
# .zlda_1 .dz_book{position:absolute;left:0;bottom:0}
# .zlda_1 h3{padding-left:70px;line-height:60px}
# .plBtn{position:absolute;right:30px;top:0;cursor:pointer!important;border-left:0}
# .shareTo{display:inline;position:absolute;right:5px;top:0;*top:-4px}
# .shareTo .shareBtn{display:inline;cursor:pointer;position:relative;padding-left:28px;z-index:999;padding-bottom:8px;*padding-bottom:0;top:1px;*top:3px}
# .shareTo .shareBtn span img{vertical-align:top}
# .shareTo .shareBtn span{position:absolute;left:7px}
# .shareTo .shareBtn .shareshowbtn{top:-1px;*top:2px}
# .shareTo .share{position:absolute;right:0;top:16px;*top:16px;padding:8px;overflow:hidden;zoom:1;width:210px;background:#fff;border:1px solid #dbdbdb;z-index:99999;_width:208px}
# .shareTo .share a{display:block;float:left;width:24px;height:24px;margin:0 3px;text-indent:-999em;overflow:hidden;padding-left:0}
# .share a{background:url(http://mat1.gtimg.com/tech/00Jamesdu/2014/index/share.png) no-repeat!important;width:24px;height:24px}
# .share .sharewb{background-position:0 -168px!important}
# .share .shareqzone{background-position:0 -144px!important}
# .share .sharesina{background-position:0 -72px!important}
# .share .shareqqemail{background-position:0 -24px!important}
# .share .sharepengyou{background-position:0 -192px!important;display:none!important}
# .share .sharerenren{background-position:0 -48px!important}
# .share .sharekaixin{background-position:0 0!important}
# .shareTo .share{width:180px;_width:178px}
# @media screen and (-ms-high-contrast:active),(-ms-high-contrast:none){.shareTo{top:10px}
# }
# .zd_b{background:#fb6600;color:#fff;font-size:12px!important;padding:3px;width:56px;height:18px;font-family:'宋体';margin-left:8px}
# .zd_xx{font-size:14px!important;color:#2f91ff;margin-left:8px}
# .l3_bz{color:#8b8b8b;font-family:'宋体';line-height:1.6em}
# .djbl ul li{margin-top:15px}
# .djbl ul li a.pic img{margin-top:5px;width:67px;height:67px}
# .noba{background:none!important}
# .mt15{margin-top:15px}
# #ks_re{display:table;content:'';clear:both;width:300px;overflow:hidden!important;position:relative}
# .r_box .bd{padding:13px 10px 10px 10px;position:relative;background:#f7f7f7}
# #ks_re .bd{padding-top:8px}
# .r_box{overflow:hidden}
# #ks_re .bd .r_zlda{position:absolute;right:0;top:0}
# #ks_re .bd .trx_ti{font-size:16px;font-family:'微软雅黑';line-height:40px;height:40px;overflow:hidden}
# .bz_12{font-size:12px;font-family:'宋体';color:#888;line-height:20px}
# #ks_re .shangtu{overflow:hidden;display:block;position:relative}
# .noborder{border:0}
# .noborder h2{left:0}
# .ll3{background:#f7f7f7;border-top:2px solid #626262;overflow:hidden;padding:15px;height:210px}
# .ll3 .cate_box{height:20px;margin-top:3px;margin-bottom:7px}
# .bt2{border-top:2px solid #626262}
# #bijx,#ks_digit{background:#f7f7f7}
# .por{position:relative}
# .poa{position:absolute}
# .r_zk_zz .zuo img{width:62px;height:62px}
# .hotlist h3 a{color:#333;font-weight:bold}
# .hotlist .Q-tpList a.picc{display:block;width:660px}
# .hotlist .Q-tpList a.picc img{margin-bottom:10px;border:1px solid #cbcbcb;width:660px!important;height:auto!important}
# .loadmore{text-align:center}
# .loadmore a:hover{color:#C00!important}
# .nohover{cursor:normal!important}
# .zthd_1 .zthd_t{font-size:16px;color:#000!important;font-weight:bold!important}
# .addcode{padding:20px 0;margin-bottom:20px;background:#f7f7f7;border-bottom:2px solid #888;overflow:hidden}
# .cate_box h2{left:10px}
# #ks_re .cate_box{border-top:0}
# #ks_qukeji{z-index:13;margin-top:16px;background:#f7f7f7;width:300px;height:320px;overflow:hidden}
# #ks_re{z-index:1}
# #ks_qukeji h2 a{font-size:20px;font-weight:bold}
# #bussinessinsider .cate_box a,#pingpart .cate_box a,.more_link{color:#666;font:12px/20px;bottom:5px}
# #bussinessinsider .cate_box a:hover,#pingpart .cate_box a:hover{color:#c00}
# .mt20{margin-top:20px!important}
# .addcode .mod1{width:300px;padding:0 16px 0 15px;float:left}
# .addcode .mod1 img{width:300px;height:140px}
# .addcode .mod1 a.picurl{display:block;width:300px;height:140px;border:1px solid #c7c7c7}
# .addcode .mod1 a.picurl:hover{border:1px solid #c00}
# .addcode #pingpart{float:right}
# .addcode h2{position:relative;clear:both;left:0}
# .addcode h2 a{display:block;width:300px;height:40px}
# .addcode .bd .trx_ti{font-size:16px;display:block;margin:15px 0 10px 0;font-family:"微软雅黑"}
# .addcode .l3_bz{line-height:1.6em}
# #recode h2 a{background:url(http://mat1.gtimg.com/tech/00Jamesdu/2015/home/images/w4.png) no-repeat;background-position:0 5px}
# #pingpart h2 a{background:url(http://mat1.gtimg.com/tech/00Jamesdu/2015/home/images/w3.png) no-repeat;background-position:0 5px}
# #bussinessinsider h2 a{background:url(http://mat1.gtimg.com/tech/00Jamesdu/2015/home/images/w2.png) no-repeat;background-position:0 5px}
# .plBtn,.shareTo{top:25px}
# .shareTo{*top:20px}
# .hotlist .similarity{width:435px;float:right}
# .mainnews .fonta li a{text-decoration:none}
# .mainnews .fonta li a.background_red{background:#c00;padding:0 5px;color:#fff;margin-right:5px;font-size:14px;font-family:Microsoft Yahei}
# .mainnews .fonta li a.color_red{font-size:16px;font-family:Microsoft Yahei}
# .ks_re{background:#f7f7f7;padding-bottom:10px}
# #ks_re .cate_box{padding-top:10px}
# .ks_re .dingtu{z-index:5;display:block;clear:both;content:'';position:relative}
# .ks_re .dingtu img{z-index:5}
# .ks_re .author{position:relative;margin-top:-5px;z-index:100}
# .ks_re .author .f14{margin-top:25px}
# .re_tit{font-size:18px;font-family:Microsoft Yahei;line-height:36px;display:block;margin:10px 0}
# .author{clear:both;content:'';display:table;display:block;overflow:hidden}
# .author img{float:left;width: 70px;height: 70px;}
# .author .f16{font-family:Microsoft Yahei;margin:25px 0 5px 0;display:block;min-width:180px}
# .author .f16,.author .l3_bz{float:left;margin-left:15px}
# .znt .cate_box{border-top:1px solid #e0e0e0;margin:0 10px}
# .znt .cate_box h2{top:0!important;display:block;left:0}
# .znt .cate_box h2 a{display:block;overflow:hidden}
# .znt{background:#f7f7f7;margin-bottom:16px;padding-bottom:16px}
# .znt .f18{display:block;min-width:130px;margin-top:11px}
# .zn_zu .f18,.zn_zu .l3_bz{width:130px;float:right}
# .zn_zu img{width:87px;height:87px;border-radius:10px}
# .znt .bd ul{overflow:hidden}
# .znt .bd ul li{width:280px;display:none}
# .znt .bd ul li.current{display:block}
# .zn_zu{padding:0 20px}
# #ks_re .more_link{bottom:12px}
# .znt .more_link{bottom:14px}
# /*  |xGv00|55c850307b82b68395a6c2b243c8f5ad */
# </style><!--[if !IE]>|xGv00|19d22975d7a6f4ac3241b1f10ce82f54<![endif]-->
# <div class="mainnav" bosszone="Tech4Nav">
#
#   <ul><li class="nobor" bosszone="technav_1"><a class="yw" href="http://tech.qq.com/">首页</a> </li><li style="display:block;" class="three" bosszone="technav_7"><a class="it" href="http://re.qq.com/" target="_blank">企鹅智酷</a> </li><li class="two sm" bosszone="technav_9"><a class="bpw" href="http://startup.qq.com/" target="_blank">腾讯创业</a> </li><li bosszone="technav_3"><a href="http://tech.qq.com/ydhl.htm" target="_blank">移动互联</a> </li><li bosszone="technav_4"><a class="dzsw" href="http://tech.qq.com/dzsw.htm" target="_blank">电商</a> </li><li class="two" bosszone="technav_5"><a class="tx" href="http://tech.qq.com/tele.htm" target="_blank">通信</a> </li><li class="three" bosszone="technav_6"><a class="it" href="http://tech.qq.com/it.htm" target="_blank">IT业界</a> </li><li style="display:block;" bosszone="technav_13" target="_blank"><a class="hlwdj" href="http://tech.qq.com/internetfinance.htm" target="_blank">金融</a> </li><li bosszone="technav_8"><a class="sjwl" href="http://tech.qq.com/tmt/" target="_blank">解码</a> </li><li class="two sm" bosszone="technav_9"><a class="bpw" href="http://v.qq.com/tech/" target="_blank">视频</a> </li><li class="two sm" bosszone="technav_10"><a href="http://digi.tech.qq.com/" target="_blank">数码</a> </li><li style="display:block;" bosszone="technav_13"><a class="rwz" href="http://space.qq.com/" target="_blank">太空</a> </li><li class="two sm" bosszone="technav_11"><a href="http://tech.qq.com/science.htm" target="_blank">探索</a> </li><li class="three wpd" bosszone="technav_12 noba"><a href="http://kepu.qq.com/" target="_blank">科普中国</a> </li></ul>
#
# <style>
# .mainnav li a{padding:0 13px;}
# </style><!--[if !IE]>|xGv00|1d81bc800ba1f7e03c8841c3d1c8b1e4<![endif]-->
# </div>
# <!--科技频道导航-->
#
#
# <style>
# .wrapper { width:1000px!important;margin:0 auto;clear:both;}
# .curPosition,.curPosition a{
#     font-family:"微软雅黑"!important;}
# .pageNav a{font-family:"微软雅黑"!important;}
# </style><!--[if !IE]>|xGv00|7695dc6318fe7f69c6350d42091da2c8<![endif]--><div class="wrapper">
# <div class="main">
# <div class="mod curPosition">
# <div style="float:left;margin-top:5px;">您的位置:<a href="http://tech.qq.com"></a> &gt; 滚动新闻</div>
# <div style="float:right;margin-top:5px;padding-right:20px;"><form name="_AutoPlayForm_">
# <input type="radio" name="_AutoPlayRadio_" id="_AutoPlayOn_" value="on" /><label for="_AutoPlayOn_">自动(每分钟刷新一次)</label>&#160;<input type="radio" name="_AutoPlayRadio_" id="_AutoPlayOff_" value="off" /><label for="_AutoPlayOff_">手动</label>&#160;&#160;<a href="javascript:;" onclick="window.location.reload();">刷新</a>
# </form>
# <script type="text/javascript">
# //<![CDATA[
# (function(){var k;var g=60000;var l=function(a){return document.getElementById(a)};var f=function(b){var a=document.cookie.indexOf(";",b);if(a==-1){a=document.cookie.length}return unescape(document.cookie.substring(b,a))};var h=function(d){var b=d+"=",n=b.length,a=document.cookie.length;var m=0;while(m<a){var c=m+n;if(document.cookie.substring(m,c)==b){return f(c)}m=document.cookie.indexOf(" ",m)+1;if(m==0){break}}return null};var i=function(b,p){var o=arguments;var m=o.length;var d=new Date();d.setTime(d.getTime()+365*24*3600*1000);var c=(2<m)?o[2]:d;var q="/";var n="qq.com";var a=false;document.cookie=b+"="+escape(p)+((c==null)?"":("; expires="+c.toGMTString()))+((q==null)?"":("; path="+q))+((n==null)?"":("; domain="+n))+((a==true)?"; secure":"")};var j=h("qq_slist_autoplay");if(j==null||j==""||j=="on"){l("_AutoPlayOn_").checked=true;i("qq_slist_autoplay","on");k=setInterval("window.location.reload()",g)}else{l("_AutoPlayOff_").checked=true;i("qq_slist_autoplay","off");clearInterval(k)}l("_AutoPlayOn_").onclick=function(){if(this.checked==true){clearInterval(k);k=setInterval("window.location.reload()",g);i("qq_slist_autoplay","on")}else{clearInterval(k)}};l("_AutoPlayOff_").onclick=function(){if(this.checked==true){clearInterval(k);i("qq_slist_autoplay","off")}else{clearInterval(k);k=setInterval("window.location.reload()",g)}};function e(){window.location.reload()}})();
# //]]>
# </script><!--[if !IE]>|xGv00|02e8017d03c2db9dc43c1a5e1f2e6841<![endif]--></div>
# </div>
# <div class="mod titbox">
# <h1>滚动新闻</h1>
# <h1>2017年07月18日
# </h1>
# </div>
# <div class="pageNav">
# <span class="na">&lt;上一页</span><strong>1</strong><span class="na">下一页&gt;</span>
# </div>
# <div class="mod newslist"><ul><li>·<a target="_blank" href="http://tech.qq.com/a/20170718/040880.htm">今年移动视频广告开支预计达180亿美元 首超固网视频</a>　<span class="pub_time">07月18日&#160;15:18</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/040865.htm">官方报告析2016年网络用语：全是套路、洪荒之力入选</a>　<span class="pub_time">07月18日&#160;15:18</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/040407.htm">“资金不是问题”：孙宏斌话音刚落，66亿没了</a>　<span class="pub_time">07月18日&#160;15:10</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/039863.htm">中青宝周二收盘股价大涨5.32% 报收于14.66元</a>　<span class="pub_time">07月18日&#160;15:02</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/038559.htm">董明珠战斗史：打遍天下，没有掌声也会发火</a>　<span class="pub_time">07月18日&#160;14:43</span>
# </li></ul><ul><li>·<a target="_blank" href="http://tech.qq.com/a/20170718/038373.htm">中国厂商崛起促指纹芯片降价：10元钱就买一颗</a>　<span class="pub_time">07月18日&#160;14:40</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/037533.htm">这次冤枉特斯拉了 车祸当事人承认自己曾取消自动驾驶</a>　<span class="pub_time">07月18日&#160;14:26</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/037014.htm">蹂躏共享单车，你见到过哪些奇葩行为？</a>　<span class="pub_time">07月18日&#160;14:18</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/036917.htm">新CEO上任五个月就走人 谷歌光纤宽带业务前景黯淡</a>　<span class="pub_time">07月18日&#160;14:17</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/035682.htm">百家号推出“百+计划”扶持原创 每月将选优质作者提供现金奖励</a>　<span class="pub_time">07月18日&#160;13:54</span>
# </li></ul><ul><li>·<a target="_blank" href="http://tech.qq.com/a/20170718/035500.htm">科大讯飞：全资子公司少量持股商汤科技</a>　<span class="pub_time">07月18日&#160;13:49</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/034690.htm">夏普就专利问题在美国起诉海信 涉及智能电视产品</a>　<span class="pub_time">07月18日&#160;13:22</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/029630.htm">曝90后"创业大V"许豪杰疑似恋童癖 本人回应：诽谤</a>　<span class="pub_time">07月18日&#160;11:43</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/029601.htm">李嘉诚投资的这家人造蛋公司好奇葩 董事会集体出走了！</a>　<span class="pub_time">07月18日&#160;11:43</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/028782.htm">中兴通讯周二午盘股价跌超6% 报收于21.52元</a>　<span class="pub_time">07月18日&#160;11:32</span>
# </li></ul><ul><li>·<a target="_blank" href="http://tech.qq.com/a/20170718/028778.htm">神州泰岳周二午盘股价跌超6% 报收于6.90元</a>　<span class="pub_time">07月18日&#160;11:32</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/027998.htm">原360市场公关负责人赵明加盟乐信 出任集团副总裁</a>　<span class="pub_time">07月18日&#160;11:22</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/027813.htm">韩国发现朴槿惠政府新罪证：涉三星接班问题</a>　<span class="pub_time">07月18日&#160;11:20</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/027589.htm">电动汽车制造商Lucid开展D轮融资 尝试卖给福特</a>　<span class="pub_time">07月18日&#160;11:17</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/026863.htm">共享雨伞创始人：雨伞放在大街上我反而不赚钱</a>　<span class="pub_time">07月18日&#160;11:09</span>
# </li></ul><ul><li>·<a target="_blank" href="http://tech.qq.com/a/20170718/026301.htm">索尼斥资4.44亿美元收购法国音乐公司 继续扩张娱乐帝国</a>　<span class="pub_time">07月18日&#160;11:03</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/025484.htm">Model 3交车仪式本月28日举行 首批车主都是特斯拉员工</a>　<span class="pub_time">07月18日&#160;10:53</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/025085.htm">蚂蚁金服重新向美国申请收购MoneyGram 暂无IPO计划</a>　<span class="pub_time">07月18日&#160;10:48</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/024270.htm">英伟达在无人驾驶领域扩大领先优势 合作伙伴名单越来越长</a>　<span class="pub_time">07月18日&#160;10:40</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/022421.htm">Leap Motion新融资5000万美元 拟来上海设办事处</a>　<span class="pub_time">07月18日&#160;10:19</span>
# </li></ul><ul><li>·<a target="_blank" href="http://tech.qq.com/a/20170718/021584.htm">基金经理：你们认为马斯克是当代乔布斯 但特斯拉不是苹果</a>　<span class="pub_time">07月18日&#160;10:11</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/019138.htm">苹果支付在华谋求走出困境：首次推出消费补贴</a>　<span class="pub_time">07月18日&#160;09:46</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/017994.htm">一次全球性网络攻击威力有多大？最高可达530亿美元</a>　<span class="pub_time">07月18日&#160;09:35</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/013326.htm">美国华盛顿特区：保安机器人掉入水中等待人类拯救</a>　<span class="pub_time">07月18日&#160;08:52</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/011859.htm">谷歌开放量子计算机 欲将其转变成为云计算服务</a>　<span class="pub_time">07月18日&#160;08:39</span>
# </li></ul><ul><li>·<a target="_blank" href="http://tech.qq.com/a/20170718/010752.htm">雷蛇CEO陈民亮：一位商人的游戏人生</a>　<span class="pub_time">07月18日&#160;08:28</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/009317.htm">鲜花电商FlowerPlus融资谜局</a>　<span class="pub_time">07月18日&#160;08:12</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/008898.htm">乐视网公告称再次延期复牌 已停牌仨月</a>　<span class="pub_time">07月18日&#160;08:09</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/008476.htm">每秒4000密码防黑客 量子通信未来5年商业价值百亿</a>　<span class="pub_time">07月18日&#160;08:04</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/008135.htm">中国惠普低调处理 专家：出现这种漏洞“不可思议”</a>　<span class="pub_time">07月18日&#160;08:00</span>
# </li></ul><ul><li>·<a target="_blank" href="http://tech.qq.com/a/20170718/007514.htm">比特币平台乱象：洗钱、虚假交易、被诉操纵市场</a>　<span class="pub_time">07月18日&#160;07:52</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/006910.htm">快递单背后的“黑色”产业链</a>　<span class="pub_time">07月18日&#160;07:45</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/006032.htm">直播平台6000元雇佣黑客攻击“对手”</a>　<span class="pub_time">07月18日&#160;07:33</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/005659.htm">乐视与民营银行牌照渐行渐远 部分资质疑似不符合监管要求</a>　<span class="pub_time">07月18日&#160;07:29</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/005348.htm">动车组叫外卖 外送费8元退单免费</a>　<span class="pub_time">07月18日&#160;07:25</span>
# </li></ul><ul><li>·<a target="_blank" href="http://tech.qq.com/a/20170718/005066.htm">苹果今年三款iPhone或全部跳票俩月</a>　<span class="pub_time">07月18日&#160;07:22</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/004403.htm">虚拟货币以太币价格上演超级过山车 单日反弹近40%</a>　<span class="pub_time">07月18日&#160;07:14</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/003950.htm">马斯克出面捍卫特斯拉疯涨的股价 任命两名新独立董事</a>　<span class="pub_time">07月18日&#160;07:05</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/003673.htm">美国取消所有中东航空公司的笔记本电脑禁令</a>　<span class="pub_time">07月18日&#160;07:01</span>
# </li>
# <li>·<a target="_blank" href="http://tech.qq.com/a/20170718/002991.htm">Netflix第二季度净利同比增长61% 用户总数破亿</a>　<span class="pub_time">07月18日&#160;06:34</span>
# </li></ul></div>
# <div class="pageNav">
# <span class="na">&lt;上一页</span><strong>1</strong><span class="na">下一页&gt;</span>
# </div>
# <div class="goto_top"><a href="#top"><img src="http://mat1.gtimg.com/news/2009/goto_top.gif" style="margin-bottom:-3px;"> 返回顶部</a></div>
# </div>
# <div class="sidebar">        <!-- 日历控件 -->
# 		<div class="mod rightCalendar">
# 			<div id="calendar" class="CalendarWrapper"></div>
# 			<div id="todayNewsLink" class="todayBtn"></div>
# 		</div>
# 		<div class="mod add"></div>
# <!--[if !IE]>|xGv00|62b39489259a1d15686bf458f00f811d<![endif]--></div>
# <div class="box_hr22"></div>
# </div>
# <script type="text/javascript">
# 	//模板输出 列表页日期
# 	var _LISTPAGE_TIME_ = ['2017','07','18'];
# 	var _LISTPAGE_URL_ = 'http://tech.qq.com/l/$Y$M/scroll_$D.htm';
# 	var _LISTPAGE_URL_REG_ = 'http://tech.qq.com/l/$Y$M/scroll_$D.htm';
# 	var _CHANNEL_CN_ = '';
# 	var _CHANNEL_EN_ = 'tech';
# </script><script type="text/javascript">
# //<![CDATA[
# function GCalendar(u,s,r){this.container=u;this.callback;this.isStatic;this.isStaticTarget="_self";this.isStaticPath;this.clientDate=s?s:new Date();this.startDate=r?r:new Date();this.limitStartDate=new Date(2004,12-1,1);var d=this;var l=function(b){return document.getElementById(b)};var p=function(x,b){function w(A,B){function D(E,G,F){if(!E||typeof F!="string"){return}G=G?G:"";F=F?F:"";E.style[G]=F;return E}if(!B){return}if(typeof B=="string"){var z=/\s?([a-z\-]*)\:\s?([^;]*);?/gi,C;while((C=z.exec(B))!=null){D(A,C[1],C[2])}}else{if(typeof B=="object"){for(var y in B){D(A,y,B[y])}}}}var v=document.createElement(x.tag||"div"),c=v.setAttribute?true:false;for(var a in x){if(a=="tag"||a=="children"||a=="cn"||a=="html"||a=="style"||typeof x[a]=="function"){continue}if(a=="cls"){v.className=x.cls}else{if(c){v.setAttribute(a,x[a])}else{v[a]=x[a]}}}if(x.html){v.innerHTML=x.html}w(v,x.style);if(b){b.appendChild(v)}return v};var k=function(v){var v=Math.random;var c=parseInt;return Number(new Date()).toString().substring(0,9)+c(10*v())+c(10*v())};var m=k();var j=this.clientDate;var e=j.getFullYear();var n=j.getMonth()+1;var t=j.getDate();var q=this.startDate;var f=q.getFullYear();var g=q.getMonth()+1;var h=q.getDate();var o=new Date(f,g-1,1).getDay();var i=new Date(f,g,0).getDate();this.cur_year=f;this.cur_month=g;this.cur_date=q.getDate();this.weekDay=["\u65e5","\u4e00","\u4e8c","\u4e09","\u56db","\u4e94","\u516d"];this.build=function(F){var B=new Date(f,g-1,1);var v=B.getDay();var y=new Array(v>0?v:0);var x=new Date(f,g,0).getDate();var w=new Array();var D=0;var G="";for(var A=1;A<=i;A++){y.push(A)}var b=this.parseCalendarHeader();var z=this.parseCalendarWeekDay();var E=this.parseCalendarDayList(y,B);var C=p({id:"_CalendarHeader_"+m,cls:"CalendarHead"});C.appendChild(b);var c=p({id:"_CalendarCon_"+m,cls:"CalendarCon"});c.appendChild(z);c.appendChild(E);this.container.appendChild(C);this.container.appendChild(c);B=v=y=x=w=D=b=z=E=C=c=null};this.updateDate=function(c){if(c==0){return}var v=new Date(this.cur_year,this.cur_month-1+c,1);var b=new Array(v.getDay()>0?v.getDay():0);var w=v.getFullYear();var y=v.getMonth()+1;var z=new Date(this.cur_year,this.cur_month+c,0).getDate();for(var a=1;a<=z;a++){b.push(a)}this.cur_year=w;this.cur_month=y;var x=this.parseCalendarDayList(b,v);l("_CalendarYear_").innerHTML="<h3>"+w+"\u5e74"+y+"\u6708</h3>";l("_CalendarDayList_"+m).innerHTML="";l("_CalendarDayList_"+m).appendChild(x);tmp=v=z=b=x=null};this.replaceDate2isStaticPath=function(w,v,y){var x=this.isStaticPath;x=x.replace(/\$Y/g,w);x=x.replace(/\$M/g,v);x=x.replace(/\$D/g,y);return x};this.parseCalendarHeader=function(M,L,K){var z=p({tag:"table",width:"222",border:"0",align:"center",cellspacing:"0",cellpadding:"0"});var v=p({tag:"tbody"});var w=p({tag:"tr"});w.setAttribute("valign","top");var H="&lt;";var C="&gt;";var A=f+"\u5e74"+g+"\u6708";var G=[24,19,136,24,19];var x=["&lt;&lt;","&lt;",A,"&gt;","&gt;&gt;"];var J=["\u4e0a\u4e00\u5e74","\u4e0a\u4e00\u6708","","\u4e0b\u4e00\u6708","\u4e0b\u4e00\u5e74"];var D=["btn","btn","","btn","btn"];var F=[-12,-1,0,1,12];var B,N,y;function E(O,c){return function(){if(F[O]!=0){c.updateDate(F[O])}}}for(var I=0;I<5;I++){B=p({tag:"td"});B.setAttribute("width",G[I]);B.setAttribute("title",J[I]);N="a";if(I==2){N="h3";B.setAttribute("id","_CalendarYear_");B.setAttribute("align","center")}y=p({tag:N,href:"javascript:void(0)"});if(y.attachEvent){y.attachEvent("onclick",E(I,d))}else{if(y.addEventListener){y.addEventListener("click",E(I,d),false)}}y.innerHTML=x[I];y.className=D[I];B.appendChild(y);w.appendChild(B)}v.appendChild(w);z.appendChild(v);v=w=H=C=A=B=N=y=null;return z};this.parseCalendarWeekDay=function(){var x=this.weekDay;var y=p({tag:"table",width:"226",border:"0",align:"center",cellspacing:"2",cellpadding:"0"});var b=p({tag:"tbody"});var w=p({tag:"tr"});var a,v;for(var c=0;c<x.length;c++){a="";if(c==0){a="sunday"}if(c==x.length-1){a="saturday"}v=p({tag:"th",html:x[c],cls:a});w.appendChild(v)}b.appendChild(w);y.appendChild(b);x=a=b=w=v=null;return y};this.parseCalendarDayList=function(N,L){var K=N;var O=L;var I=0;var A=O.getFullYear();var M=O.getMonth()+1;var H=O.getDay()+1;var C=p({id:"_CalendarDayList_"+m});var y=p({tag:"table",width:"226",border:"0",align:"center",cellspacing:"2",cellpadding:"0"});var c=p({tag:"tbody"});var w,v,z,x;var J,D;function B(Q,P){return function(){if(typeof P.callback=="function"){P.callback(Q)}}}for(var G=0;G<6;G++){v=p({tag:"tr"});for(var E=0;E<7;E++){J=K[I++];z=p({tag:"td"});if(J==h&&this.cur_year==f&&this.cur_month==g){x=p({tag:"em",html:this.cur_date,cls:"today"})}else{if(!J){x=p({tag:""})}else{var D=new Date(A,M-1,J);if(D<=this.clientDate&&D>=this.limitStartDate){var F="javascript:void(0)";if(this.isStatic){F=this.replaceDate2isStaticPath(A,(M<10?("0"+M):M),(J<10?("0"+J):J))}else{F="javascript:void(0)"}x=p({tag:"a",html:J,href:F,target:this.isStaticTarget});if(!this.isStatic){if(x.attachEvent){x.attachEvent("onclick",B(D,d))}else{if(x.addEventListener){x.addEventListener("click",B(D,d),false)}}}}else{x=p({tag:"span",html:J})}}}z.appendChild(x);v.appendChild(z)}c.appendChild(v)}y.appendChild(c);C.appendChild(y);w=th=null;return C};this.onclick=function(b){}};
# //]]>
# </script><!--[if !IE]>|xGv00|e2496b8afa89333f912494b93a144830<![endif]-->
#
# <script type="text/javascript">var _SERVER_TIME_FULL_ = [2017,07,18,15,20,13];/* YYYY,mm,dd,HH,MM,SS */</script><!--[if !IE]>|xGv00|01e8c267813789ac441411e638363c46<![endif]-->
# <script type="text/javascript">
# //<![CDATA[
# var _LIMIT_START_DATE_ = [2009,01,01];
# //]]>
# </script><!--[if !IE]>|xGv00|243efb2caac4871247d4dbf065a6fc6d<![endif]-->
# <script type="text/javascript">
# //<![CDATA[
# //服务器时间
# var serverDate = (typeof _SERVER_TIME_FULL_ != "undefined")?new Date(_SERVER_TIME_FULL_[0],_SERVER_TIME_FULL_[1]-1,_SERVER_TIME_FULL_[2]):new Date();
# //页面起始日期
# var currentDate = (typeof _LISTPAGE_TIME_ != "undefined")?new Date(_LISTPAGE_TIME_[0],_LISTPAGE_TIME_[1]-1,_LISTPAGE_TIME_[2]):new Date();
# //网站内容起始日期
# var limitStartDate = (typeof _LIMIT_START_DATE_ != "undefined")?new Date(_LIMIT_START_DATE_[0],_LIMIT_START_DATE_[1]-1,_LIMIT_START_DATE_[2]):new Date(2004,12-1,1);
#
# (function(){//输出今日新闻链接
# 	var con = document.getElementById("todayNewsLink");
# 	var l = _LISTPAGE_URL_REG_;
# 	var _s = (typeof _SERVER_TIME_FULL_ != "undefined")?_SERVER_TIME_FULL_:null,_c = _LISTPAGE_TIME_;
# 	var c = _c?new Date(_c[0],_c[1]-1,_c[2]):new Date();//当前列表页日期
# 	var s = _s?new Date(_s[0],_s[1]-1,_s[2]):new Date();//服务器时间
# 	var y = s.getFullYear();
# 	var m = s.getMonth()+1;
# 	var d = s.getDate();
# 	m = m < 10 ? ("0"+m) : m;
# 	d = d < 10 ? ("0"+d) : d;
# 	l = l.replace(/\$Y/g,y);l = l.replace(/\$M/g,m);l = l.replace(/\$D/g,d);
# 	//alert((_s[0]+""+_s[1]-1+""+_s[2])+"\n\n"+(_c[0]+""+_c[1]-1+""+_c[2]))
# 	if(c < s){
# 		con.innerHTML = '<a href="'+l+'">&gt;&gt;今日新闻</a>'
# 	}else{
# 		con.innerHTML = '&gt;&gt; 今日新闻';
# 	}
# }
# )()
# var _calendar_ = new GCalendar(document.getElementById("calendar"),serverDate,currentDate);//日历容器，服务器时间，日历起始时间
# if(limitStartDate)	_calendar_.limitStartDate = limitStartDate;
# _calendar_.isStatic = true;
# _calendar_.isStaticPath = _LISTPAGE_URL_REG_;//$Y 4为年 $M 2位月 $D 2位天
# _calendar_.build();
#
# //]]>
# </script><!--[if !IE]>|xGv00|5951ac9d2b6861dda8f0828287e43a71<![endif]-->
# <script language="javascript" src="http://pingjs.qq.com/ping.js"></script>
# <script language="javascript">if(typeof(pgvMain) == 'function') pgvMain();</script>
#
# <!--[if !IE]>|xGv00|8562b5198b819aae2599422d037fbd8e<![endif]-->
# <script>
# 	if (typeof AD2 != 'undefined') {
# 		AD2.ping.flush();
# 	}
# </script>
# <!--[if !IE]>|xGv00|99c120ec66e42144a84b53ea7aba389d<![endif]--><!--[if !IE]>|xGv00|1325e3ec3be887214430c1485f9c30d5<![endif]--><script>
# var NavNoticeSiteName = ["sports","tech","games","cul","edu","fashion","house","auto","finance","ent"];
# </script>
# <script src="//mat1.gtimg.com/www/chrometips/notification2017_v0118.js"></script><!--[if !IE]>|xGv00|160405494288ecc3516e240c185c4fd7<![endif]-->
# <style>
# .tcopyright {width:960px;margin:0 auto;padding:8px 0;font-size:12px;line-height:28px;color:#333; text-align:center; overflow:hidden;clear:both;}
# .tcopyright .en{font-family:Arial;}
# .tcopyright a{color:#333;text-decoration: none;}
# .tcopyright a:hover{color:#bd0a01;text-decoration: underline;}
# </style>
# <div id="tcopyright" class="tcopyright" bossZone="footer" role="contentinfo">
# 	<div>
# 		<a href="http://www.tencent.com/" target="_blank" rel="nofollow">关于腾讯</a> | <a href="http://www.tencent.com/index_e.shtml" target="_blank" rel="nofollow">About Tencent</a> | <a href="http://www.qq.com/contract.shtml" target="_blank" rel="nofollow">服务协议</a> | <a href="http://www.qq.com/privacy.htm" target="_blank" rel="nofollow">隐私政策</a> | <a href="http://open.qq.com/" target="_blank" rel="nofollow">开放平台</a> | <a href="http://www.tencentmind.com/" target="_blank" rel="nofollow">广告服务</a> | <a href="http://hr.tencent.com/" target="_blank" rel="nofollow">腾讯招聘</a> | <a href="http://gongyi.qq.com/" target="_blank" rel="nofollow">腾讯公益</a> | <a href="http://service.qq.com/" target="_blank" rel="nofollow">客服中心</a> | <a href="http://news.qq.com/zt2014/2014qtnews/ccybspxd.htm
# " target="_blank" rel="nofollow">举报中心</a> | <a href="http://www.qq.com/map/" target="_blank" rel="nofollow">网站导航</a>
# 	</div>
#   	<div class="en">Copyright &copy; 1998 - 2017 Tencent. All Rights Reserved</div>
#     <div>
# 		<a href="http://www.tencent.com/" target="_blank" rel="nofollow">腾讯公司</a> <a href="http://www.tencent.com/zh-cn/le/copyrightstatement.shtml" target="_blank" rel="nofollow">版权所有</a>
# 	</div>
# </div><!--[if !IE]>|xGv00|b6614ae390f3ba6a8cbcc269055b42da<![endif]--><!--[if !IE]>|xGv00|6a38792f87c8551a6f929fd372302b76<![endif]--><!--[if !IE]>|xGv00|aa4816366c4a8cdf42d09546aa1d9439<![endif]-->
# </body>
# </html>
#
# <!--[if !IE]>|xGv00|07d2f9bffc255715480907f88ec4428f<![endif]-->
# """
# import time
#
# selector = Selector(text=value)
#
# articles = selector.xpath('//div[@class="mod newslist"]//li')
#
# for article in articles:
#     source_url = article.xpath('a/@href').extract_first('')
#     title = article.xpath('a/text()').extract_first('')
#     post_date = article.xpath('span/text()').extract_first('')
#     post_date = time.strftime('%Y', time.localtime(time.time()))+u'年'+post_date
#     print title, post_date, source_url
import time


def a():
    index = 0
    while True:
        index += 1
        for did in [-1,-2,-3,-4,-5,-6,-7,-8,-9,-0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-11,-1,-1,-1,-111,-1,-1,-1]:
            yield did
        print 1111
        time.sleep(2)

for i in a():
    print i