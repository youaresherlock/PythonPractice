# -*- coding: utf-8 -*-
import time
from pprint import pprint
from copy import deepcopy
import scrapy


# scrapy.Request
class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['bookschina.com']
    start_urls = ['http://www.bookschina.com/books/kinder/']
    base_url = "http://www.bookschina.com"

    def parse(self, response):
        # 1. 获取到所有的大分类的列表
        h2_list = response.xpath("//div[@class='categoriesList']//h2")
        # 遍历大分类的列表，获取每一个大分类
        for h2 in h2_list[:1]:
            item = {}
            # 获取大分类的名字
            item["b_cate"] = h2.xpath("./a/text()").extract_first()
            # 2. 获取到当前大分类对应的所有小分类的列表
            li_list = h2.xpath("./following-sibling::ul[1]/li")
            # 遍历小分类的列表 获取每一个小分类
            for li in li_list[:1]:
                # 小分类的名字
                item["s_cate"] = li.xpath("./a/text()").extract_first()
                # 小分类的url地址
                item["s_href"] = self.base_url + li.xpath("./a/@href").extract_first()
                # 发送小分类的url地址的请求，进入到列表页
                yield response.follow(
                    url=item["s_href"],
                    callback=self.parse_book,
                    meta={"item": deepcopy(item)}
                )

    def parse_book(self, response):
        # 接收分类页面传递来的数据
        item = response.meta["item"]
        # 获取到所有图书的列表
        li_list = response.xpath("//div[@class='bookList']//li")
        # 遍历 图书的列表 获取每一个图书的信息
        for li in li_list:
            # 图书的名字
            item["book_name"] = li.xpath(".//h2/a/text()").extract_first()
            # 图片的url地址
            item["book_img_url"] = li.xpath(".//img[@class='lazyImg']/@data-original").extract_first()
            # 作者
            item["book_author"] = li.xpath(".//a[@class='author']/text()").extract_first()
            # 出版日期
            item["book_pub_date"] = li.xpath(".//span[@class='pulishTiem']/text()").extract_first()
            # 出版社
            item["book_publisher"] = li.xpath(".//a[@class='publisher']/text()").extract_first()
            # 价格
            item["book_price"] = li.xpath(".//span[@class='sellPrice']/text()").extract_first()
            # 折扣
            item["book_discount"] = li.xpath(".//span[@class='discount']/text()").extract_first()
            # 定价
            item["book_pricing"] = li.xpath(".//del/text()").extract_first()
            # 描述信息
            item["book_desc"] = li.xpath(".//p[@class='recoLagu']/text()").extract_first()

            yield item

        # 翻页
        next_url = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_url is not None:
            time.sleep(3)
            yield response.follow(
                next_url,
                callback=self.parse_book,
                meta={"item": deepcopy(item)}
            )
