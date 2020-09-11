#!usr/bin/python
# -*- coding:utf8 -*-
"""
获取贴吧的每个标题以及图片
1. 确定url地址 url: https://tieba.baidu.com/f?kw={}

2. 确定抓取的数据的位置 抓取数据的时候 先对数据进行分组 遍历提取数据
分组拿到li列表  //li[@class='']

3. 从列表页中进入到详情页中 对详情页的url地址发送请求
提取图片 //img[@class='BDE_Image']
"""
import requests
from lxml import etree


class TieBaSpider(object):

    def __init__(self, name):
        self.url = 'https://tieba.baidu.com/f?kw={}'.format(name)
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
        self.base_url = 'https://tieba.baidu.com'

    def send_request(self, url):
        """
        发送请求, 获取响应的方法
        """
        response = requests.get(url, headers=self.headers)

        return response.content

    def parse_data(self, response):
        """
        解析数据的方法
        """
        response = response.decode().replace('<!--', '').replace('-->', '')
        # 将响应的内容转换成element对象
        element = etree.HTML(response)
        # 对数据进行分组
        li_list = element.xpath("//ul[@id='thread_list']/li")

        data_list = []
        for li in li_list:
            item = dict()
            item['title'] = li.xpath(".//a[@class='j_th_tit ']/text()")[0]
            item['href'] = self.base_url + li.xpath(".//a[@class='j_th_tit ']/@href")[0]
            img_url_list = self.parse_detail_image(item['href'])
            item['image_url_list'] = img_url_list
            data_list.append(item)

        return data_list

    def parse_detail_image(self, detail_url):
        response = self.send_request(detail_url)
        element = etree.HTML(response)
        img_url_list = element.xpath("//img[@class='BDE_Image']/@src")

        return img_url_list

    def save_data(self, data_list):
        print(data_list)

    def run(self):
        # 解析数据
        response = self.send_request(self.url)
        data_list = self.parse_data(response)
        self.save_data(data_list)


if __name__ == '__main__':
    spider = TieBaSpider('一拳超人')
    spider.run()























