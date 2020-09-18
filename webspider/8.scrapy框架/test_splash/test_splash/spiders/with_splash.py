# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class WithSplashSpider(scrapy.Spider):
    name = 'with_splash'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=传智播客']

    def start_requests(self):
        yield SplashRequest(
            self.start_urls[0],
            callback=self.parse_splsh,
            # 指定渲染等待的最大时间
            args={"wait": 10},
            # 固定参数
            endpoint='render.html'
        )

    def parse_splsh(self, response):
        with open("with_splash.html", "wb") as f:
            f.write(response.body)
