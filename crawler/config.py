# -*- coding: utf-8 -*-

init_file           = "inited"
db_file             = 'webpages.db'
log_file            = 'crawler.log'
pagerank_file       = "pagerank.dat"
inverted_index_file = "index.dat"
word_file           = "words2search.dat"
searched_word_file  = "searched_word.dat"
chromedriver_path   = r'N:/Tools/chromedriver/chromedriver.exe'

cache_dir = "cache/"

key_batch_size = 1


init_words = ["动", "播", "搬", "番", "国", "音", "影"]


bili_domain = "https://www.bilibili.com"

bili_header = {
    #"Host": "www.bilibili.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": "_uuid=8E6BD7D2-BEA6-B571-007F-9A53D5E4A39279306infoc; LIVE_BUVID=AUTO3515287137887598; fts=1528713798; sid=93p6nbpa; buvid3=8E8A2F50-57ED-43E6-A3A8-997EFE00636624047infoc; rpdid=kxlqskwwsidosiqmokqpw; im_notify_type_896086=0; stardustvideo=1; CURRENT_FNVAL=16; UM_distinctid=1675829bde8150-0345344bf8b432-4313362-144000-1675829bdeb3dc; _uuid=41918D35-5BF1-4F6A-4932-6EECFC6DBE9285494infoc; DedeUserID=896086; DedeUserID__ckMd5=2a904934164363dd; SESSDATA=7a210ddf%2C1546786964%2C0a6c54c1; bili_jct=0616688e7e788ae24eb59d05bd4ea2ad; CURRENT_QUALITY=80; _dfcaptcha=4ba8cf28f2812da54227b52f626a4ba9"
}

bili_search = [
    "https://search.bilibili.com/all?keyword=",
    "https://search.bilibili.com/video?keyword=",
    "https://search.bilibili.com/bangumi?keyword=",
    "https://search.bilibili.com/pgc?keyword=",
    "https://search.bilibili.com/live?keyword=",
    "https://search.bilibili.com/article?keyword=",
    "https://search.bilibili.com/topic?keyword=",
    "https://search.bilibili.com/upuser?keyword=",
    "https://search.bilibili.com/photo?keyword="
]

bcy_domain = "https://bcy.net"

bcy_header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "cookie": "mobile_set=no; tt_webid=6634289909824177667; Hm_lvt_330d168f9714e3aa16c5661e62c00232=1544665992; _ga=GA1.2.1889553593.1544665992; _gid=GA1.2.1848094846.1544665992; __tea_sdk__user_unique_id=6634289909824177667; PHPSESSID=f74ec7f70783fb0364a6c6cf7f0bd0c1; __tea_sdk__ssid=060962cb-214d-4bdb-8fa4-bd175b18cf85; lang_set=zh; s_v_web_id=4da95bf240251f5e4c892fe891fcc183; sid_guard=cb1d865a7525533e17920b51d8e63fd8%7C1544666087%7C5184000%7CMon%2C+11-Feb-2019+01%3A54%3A47+GMT; uid_tt=674f220de990a0ebde8ee0db0da01e22; sid_tt=cb1d865a7525533e17920b51d8e63fd8; sessionid=cb1d865a7525533e17920b51d8e63fd8; _csrf_token=46a1fb5deb8604056ca4e8065a5ac7b2; Hm_lpvt_330d168f9714e3aa16c5661e62c00232=1544666815; _gat_gtag_UA_121535331_1=1; _bcy_user_id=U2FsdGVkX1868QZsK/Y8hnpwBGh7o9g8eOv6QmBN7/5ibnFtyg6MiTxhTieFwluHQ09XlS3SAaGn7xRIHW5fOw==",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

bcy_search = [
    "https://bcy.net/search/all?k=",
    "https://bcy.net/search/group?k=",
    "https://bcy.net/search/user?k="
]

moegirl_domain = "https://zh.moegirl.org"

moegirl_header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "cookie": "_ga=GA1.2.123220650.1544666211; _gid=GA1.2.1373805944.1544666211; __cfduid=dab8870bcb48d71797d2fe5fe612030dc1544666214; _gat=1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

moegorl_search = [
    "https://zh.moegirl.org/index.php?search="
]

pixiv_domain = "https://www.pixiv.net"

pixiv_header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "max-age=0",
    "cookie": "first_visit_datetime_pc=2018-12-13+10%3A59%3A58; p_ab_id=5; p_ab_id_2=3; p_ab_d_id=2129502038; __utma=235335808.736746426.1544666400.1544666400.1544666400.1; __utmc=235335808; __utmz=235335808.1544666400.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); login_bc=1; _ga=GA1.2.736746426.1544666400; _gid=GA1.2.122712113.1544666403; PHPSESSID=6009145_676c3c676f844bde5b5381f6d900af0a; device_token=cade6ea4aeecfade84b4e2046ddafb12; privacy_policy_agreement=1; c_type=30; a_type=0; b_type=1; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; is_sensei_service_user=1; yuid_b=QBcphpU; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=6009145=1^9=p_ab_id=5=1^10=p_ab_id_2=3=1^11=lang=zh=1; __utmt=1; __utmb=235335808.9.10.1544666400",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}

pixiv_search = [
    "https://www.pixiv.net/search.php?word=",
    "https://www.pixiv.net/novel/search.php?word=",
    "https://www.pixiv.net/search_user.php?nick="
]


acfun_domain = "http://www.acfun.cn"

acfun_header = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8",
    #"Cookie": "session_id=2306229577B6269C; _did=web_833567208366D62D; uuid=0458fb33b7d509089c92da0306601c21; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167b285d8b668b-013fe00d09af86-b781636-384000-167b285d8b7109%22%7D; Hm_lvt_2af69bc2b378fb58ae04ed2a04257ed1=1544888377; clientlanguage=zh_CN; cur_req_id=1205597970514E0F_self_74b76dad2e3d41dd05bc5c996f67fdcf; cur_group_id=1205597970514E0F_self_74b76dad2e3d41dd05bc5c996f67fdcf_0; stochastic=dGxxNHhwdW51MQ%3D%3D; analytics=GA1.2.985639177.1544888667; analytics_gid=GA1.2.2121521324.1544888667; acPostHint=21b632f4313cd004f954a79920dedac70a39; auth_key_ac_sha1=1568745327; auth_key_ac_sha1_=cVcxArzq5THfP5Z3Eymxzkvic7I=; auth_key=14325513; ac_username=%E7%BB%BF%E8%8C%B6%E6%9F%9A%E6%9F%9A%E5%AD%90; ac_userimg=http://cdn.aixifan.com/dotnet/20120923/style/image/avatar.jpg; mobile_conf=2ec3; acPasstoken=ChVpbmZyYS5hY2Z1bi5wYXNzdG9rZW4ScAuSiJIlronnGTACWIdga6iDhqCZAXKYtwHBzZ0XQrllfBs9thJPqvrGlQ_BYOZ_nZgTGgzkp6y7bNtdzpOHf4A30bNlHATq-0bdSNR7rRsSZXW3gQZszJVDx-2ptB-kp_ksBRz3_-LkFBdBRHnvpeQaEjdj8KoLCXYgblbrOm9z751ihiIgLsht5aetLQYFBxzCri0RCBt6jxvELexRazNGQKQMXIsoBTAB; XSRF-TOKEN=eyJpdiI6IlE0T0wyUTJzNmtEdlNUTkxRUmVSckE9PSIsInZhbHVlIjoidGtsajhQVWhMZ1dCNE44QU9jSTBGZEhEUFwvRkZhd2RKekNLTVpEcURiQlE1RXdwMXN0VEJUSjhRd09Yb2NJXC9Fd3pMV3lZdlwvVW9XbGlKVE04ckJVanc9PSIsIm1hYyI6IjE3MWM2M2E1NjZmZjY4NWVmZjEwNWM0NmE3N2Q3ZWY2MDRkNDU2M2RkYTczNTg5ODEyZTJmNTgwMDA0YmIyNWIifQ%3D%3D; ap_session=eyJpdiI6IkVHSklBK1I3ank0cFNldTZnbndQNWc9PSIsInZhbHVlIjoiaUVhYks5ZGpRWnphdE1jcXAyZnlPR2lOYzM1cXgwM2R0a3NrbVIwRjZOY1p1MlwvZlZ3Y1ExSmJBVUhCRmtOQlpcL2dcL3R4ZTRqdTFJMkZhUFlWQnZ5b1E9PSIsIm1hYyI6IjlhMGNlYjUxNDE0ZTZmZjI5YjgzYjQ2ODNhMzhkYzc1MzVhYmQyYjFkYjg5ZGVkMWM5YmZjMTA4YzQ4MjI5MWYifQ%3D%3D; online_status=0; userLevel=0; userGroupLevel=0; checkMobile=1; checkEmail=0; Hm_lpvt_2af69bc2b378fb58ae04ed2a04257ed1=1544888738; notice_status=1"
}

acfun_search = [
    "http://www.acfun.cn/search/#type=video;query="
]


bangumi_domain = "http://bgm.tv"

bangumi_header = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8",
    "Cookie": "__cfduid=d7563bdb6a36cf2999108530759e9f2621544949179; chii_sid=U99fdp; __utma=1.1856298605.1544949189.1544949189.1544949189.1; __utmc=1; __utmz=1.1544949189.1.1.utmcsr=tech2ipo.com|utmccn=(referral)|utmcmd=referral|utmcct=/10027969; __utmt=1; chii_searchDateLine=0; __utmb=1.6.10.1544949189"
}

bangumi_search = [
    "http://bgm.tv/subject_search/"
]



search_sites = [
    {'domain': bili_domain, 'search_page': bili_search, 'header': bili_header},
    {'domain': bcy_domain, 'search_page': bcy_search, 'header': bcy_header},
    {'domain': moegirl_domain, 'search_page': moegorl_search, 'header': moegirl_header},
    {'domain': acfun_domain, 'search_page': acfun_search, 'header': acfun_header},
    {'domain': bangumi_domain, 'search_page': bangumi_search, 'header': bangumi_header},
]


accept_domains = [
    "bilibili",
    "bcy",
    "moegirl",
    "acfun",
    "bgm"
]


skip_prefix = [
    "https://bcy.net/u/",
    "https://zh.moegirl.org/Special:",
    "https://commons.moegirl.org/Special:",
    "http://space.bilibili.com/896086"
]