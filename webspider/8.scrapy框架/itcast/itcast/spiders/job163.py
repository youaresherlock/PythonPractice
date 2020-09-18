# -*- coding: utf-8 -*-
import scrapy
from itcast.items import JobItem


class Job163Spider(scrapy.Spider):
    name = 'job163'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/position/list.do']

    def parse(self, response):
        tr_list = response.xpath("//table[@class='position-tb']//tr")
        tr_list = [tr for tr in tr_list if tr_list.index(tr) % 2 != 0]
        for tr in tr_list:
            item = JobItem()
            item["name"] = tr.xpath("./td[1]/a/text()").extract_first()
            item["detail_href"] = "https://hr.163.com/" + tr.xpath("./td[1]/a/@href").extract_first()
            # 构造详情页的请求对象
            yield scrapy.Request(
                item["detail_href"],
                callback=self.parse_detail,
                meta={"item": item}
            )

        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        if next_url != "javascript:void(0)":
            # 构造完整的url地址
            next_url = "https://hr.163.com/position/list.do" + next_url
            # 构造request请求对象
            import time
            time.sleep(2)
            yield scrapy.Request(
                next_url,
                # 不指定 默认就是parse方法
                callback=self.parse
            )
    def parse_detail(self, response):
        # 接收列表页传递的数据
        item = response.meta["item"]
        item["pub_date"] = response.xpath("//p[@class='post-date']/text()").extract_first()
        yield item

