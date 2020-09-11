#!usr/bin/python
# -*- coding:utf8 -*-
"""
糗事百科段子爬取
https://www.qiushibaike.com/text/page/1/
"""
import requests
from lxml import etree


class QiuBaiSpider(object):

    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/text/page/{}/'
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}

    def get_url_list(self):
        """
        生成13个url地址的方法
        """
        url_list = [self.base_url.format(i) for i in range(1, 14)]

        return url_list

    def send_request(self, url):
        """
        发送请求获取响应的方法
        """
        response = requests.get(url, headers=self.headers)

        return response.content

    def parse_data(self, response):
        """
        解析数据的方法
        :param response: 响应的内容
        :return: 数据
        """
        # 将响应的内容转换成element对象
        element = etree.HTML(response)
        # 对数据进行分组
        div_list = element.xpath("//div[@class='col1 old-style-col1']/div")

        data_list = []
        for div in div_list:
            item = dict()
            item['author'] = div.xpath('.//h2/text()')[0].strip()
            item['content'] = div.xpath('.//div[@class="content"]/span/text()')
            data_list.append(item)
            print(item)

        return data_list

    def run(self):
        # 1. 初始化url地址, 准备13个url地址
        url_list = self.get_url_list()
        # 2. 遍历这个url地址 发送请求 获取响应
        for url in url_list:
            response = self.send_request(url)
            # 3. 提取数据
            self.parse_data(response)
        # 4. 保存数据


if __name__ == '__main__':
    spider = QiuBaiSpider()
    spider.run()























