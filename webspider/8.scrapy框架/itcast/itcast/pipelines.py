# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from pymongo import MongoClient


class MongoPipeline(object):

    def open_spider(self, spider):
        if spider.name == "teacher":
            con = MongoClient()
            self.connection = con.it.teacher

    def process_item(self, item, spider):
        if spider.name == "teacher":
            self.connection.insert(dict(item))

        return item


class ItcastPipeline:

    def open_spider(self, spider):
        """
        在爬虫开启的时候只执行一次
        :param spider: 爬虫对象
        :return:
        """
        if spider.name == "teacher":
            self.f = open("teacher.json", "a", encoding='utf-8')

    def process_item(self, item, spider):
        """
        处理爬虫中传递过来的数据的方法
        :param item:  要处理的数据
        :param spider:  当前传递数据过来的爬虫对象
        :return:
        """
        if spider.name == "teacher":
            self.f.write(json.dumps(dict(item), ensure_ascii=False, indent=2) + ",\n")
        return item

    def close_spider(self, spider):
        """
        在爬虫关闭的时候 只执行一次
        :param spider:
        :return: 爬虫对象
        """
        if spider.name == "teacher":
            self.f.close()
