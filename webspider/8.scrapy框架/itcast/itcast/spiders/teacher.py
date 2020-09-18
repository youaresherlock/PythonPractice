# -*- coding: utf-8 -*-
import scrapy
from itcast.items import ItcastItem

# scrapy.Spider 在Scrapy框架中是所有爬虫类的父类
class TeacherSpider(scrapy.Spider):
    # 爬虫的名字 （启动爬虫的时候需要使用到这个名字）
    name = 'teacher'
    # 爬虫允许爬取域名范围
    allowed_domains = ['itcast.cn']
    # 起始页的url地址
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    # 解析起始页url地址对应的响应的方法，这个方法必须有 必须叫做parse
    # response 起始页url地址的对应的响应对象
    def parse(self, response):
        # print(response.status)
        # 1. 响应对象response可以直接去调用 xpath()
        li_list = response.xpath("//div[@class='tea_con']//li")
        # print(li_list)
        # 遍历分组去提取数据
        data_list = []
        for li in li_list:
            # item = {}
            item = ItcastItem()
            # 使用xpath方法提取出来的数据是一个 selector对象，
            # extract() 返回包含数据字符串的列表
            # extract_first() 返回列表中第一个字符串。当列表为空的返回None
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["level"] = li.xpath(".//h4/text()").extract_first()
            item["desc"] = li.xpath(".//p/text()").extract_first()
            # print(item)
            # data_list.append(item)
            # yield data_list
            yield item