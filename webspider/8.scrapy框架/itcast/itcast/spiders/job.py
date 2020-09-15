# -*- coding: utf-8 -*-
import scrapy
# LinkExtractor  连接提取器类
from scrapy.linkextractors import LinkExtractor
# CrawlSpider 爬虫类型  Rule 规则类
from scrapy.spiders import CrawlSpider, Rule


# 继承了父类CrawlSpider
class JobSpider(CrawlSpider):
    name = 'job'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do']

    # 一个元组或者列表   包含的内容就是 Rule对象 规则对象
    """
    LinkExtractor: 链接提取器，正则表达式  xpath  对url地址进行匹配的规则
    callback： 表示的就是通过链接提取器提取出来的url地址的响应回调函数（url地址响应交给哪一个函数去解析）
        可以没有此参数，没有此参数的时候表示的是：响应不会被回调函数去处理
        接收的是 方法名的字符串
    follow： 连接提取器提取出来的url地址的响应中是否还继续根据 rules 规则进行提取，True会  False不会
    """
    rules = (
        # 翻页的规则
        Rule(LinkExtractor(allow=r'\?currentPage=\d+'), follow=True),
        # 获取详情页的规则
        Rule(LinkExtractor(allow=r'/position/detail.do\?id=\d+'), callback="parse_item"),
    )
    """
    抓取 163招聘信息，进行翻页操作，在列表页中不进行数据的提取，在详情页中进行数据的提取。
    获取翻页的url地址： 不需要提取数据  不指定callback  follow=True
    获取详情页的url地址   提取数据   指定callback  
    """

    def parse_item(self, response):
        item = {}
        item["title"] = response.xpath("//h2/text()").extract_first()
        item["pub_date"] = response.xpath("//p[@class='post-date']/text()").extract_first()
        print(item)

