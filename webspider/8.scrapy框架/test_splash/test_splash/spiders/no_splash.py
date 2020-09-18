# -*- coding: utf-8 -*-
import scrapy


class NoSplashSpider(scrapy.Spider):
    name = 'no_splash'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=传智播客']

    def parse(self, response):
        with open("no_splash.html", "w") as f:
            f.write(response.body.decode())
