# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    # 讲师名字
    name = scrapy.Field()
    # 讲师的等级
    level = scrapy.Field()
    # 描述
    desc = scrapy.Field()


class JobItem(scrapy.Item):

    name = scrapy.Field()
    detail_href = scrapy.Field()
    pub_date = scrapy.Field()
