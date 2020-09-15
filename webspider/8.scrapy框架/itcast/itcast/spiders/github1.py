# -*- coding: utf-8 -*-
import scrapy


class Github1Spider(scrapy.Spider):
    name = 'github1'
    allowed_domains = ['github.com']
    start_urls = ['http://www.jxmjc.com/login.php?']

    def start_requests(self):
        # 1. 准备请求体数据
        data = {
            "lgt": '0',
            "pwuser": "itcast_test",
            "pwpwd": '123456',
            "hideid": '0',
            "forward": "",
            "jumpurl": "http://www.jxmjc.com/u.php?verify=7de38797",
            "m": "bbs",
            "step": '2',
            "cktime": '31536000',
        }
        yield scrapy.FormRequest(
            self.start_urls[0],
            formdata=data,
            callback=self.parse
        )

    def parse(self, response):
        with open("luntan.html", "w", encoding="utf-8") as f:
            f.write(response.body.decode('gbk'))
