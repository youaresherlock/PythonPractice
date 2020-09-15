# -*- coding: utf-8 -*-
import scrapy


# 登录github   起始页的url地址就是你的个人中心页面， 发送起始页url地址的请求的时候
# 需要携带cookie

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/ZuoAndroid']

    def start_requests(self):
        # 1. 获取到登录之后的cookie字符串（从浏览器进行登录 复制）
        cookie_str = "_octo=GH1.1.1982342125.1590541963; _ga=GA1.2.646792670.1590541980; _device_id=521f5cc28583a375daea36bbfbdccfc6; user_session=z2d4YyDtNXm2ILFxOG5quVvlJdwJbHxgfIJjctIsBp46NBuu; __Host-user_session_same_site=z2d4YyDtNXm2ILFxOG5quVvlJdwJbHxgfIJjctIsBp46NBuu; logged_in=yes; dotcom_user=ZuoAndroid; has_recent_activity=1; _gh_sess=ROaAehONR7mY%2FuJPlMxvo2qReDHxnzTOhgWULHQeBMIqfNj4nqfwefiT5RHZwRwCH9ajDUIWRCrLnE1KAfTJoLos3OJNRV%2FDNK%2FbrjDrBW4q2HoRbvxJZZ8BU8lwUJVZMITqmNf%2BiglVZqJmdNIvvlNENE7aUJWd1%2Fxet5p38pMM1SI%2FFXwxWfSkwJD7gUxH--xISNee6J%2FpWcVXMf--Y763b2BH6%2FWb53ySwsAt9g%3D%3D"
        # 2. 将cookie字符串转换成cookie字典
        cookie_dict = {i.split("=")[0]: i.split("=")[1] for i in cookie_str.split("; ")}
        # 3. 在构造请求对象的时候将 cookies参数携带上
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                # 重写了start_requests 指定一下解析数据的方法
                callback=self.parse,
                cookies=cookie_dict
            )

    def parse(self, response):
        with open("github.html", "w", encoding='utf-8') as f:
            f.write(response.body.decode())
