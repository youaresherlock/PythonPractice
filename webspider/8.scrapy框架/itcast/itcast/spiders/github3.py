# -*- coding: utf-8 -*-
import scrapy


class Github3Spider(scrapy.Spider):
    name = 'github3'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            # 1. response响应对象
            response,
            # 2. 根据xpath定位到form表单
            formxpath="//div[@id='login']/form",
            # 3. 准备好form表单需要的数据
            formdata={"login": "ZuoAndroid", "password": "lyp82nlf@.."},
            callback = self.parse_login
        )

    def parse_login(self, response):
        with open("github3.html", "w", encoding="utf-8") as f:
            f.write(response.body.decode())