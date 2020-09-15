# -*- coding: utf-8 -*-
import scrapy


class Github4Spider(scrapy.Spider):
    name = 'github4'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/ZuoAndroid']

    def parse(self, response):
        with open("github4.html", "wb") as f:
            f.write(response.body)
