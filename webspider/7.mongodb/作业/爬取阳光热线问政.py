#!usr/bin/python
# -*- coding:utf8 -*-
"""
http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1
"""
import time
import json
import requests
from lxml import etree


class SunSpider(object):

    def __init__(self, page_count):
        self.url = "http://wz.sun0769.com/political/index/politicsNewest?id=1&page={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
        }
        self.page_count = page_count
        self.base_topic_url = "http://wz.sun0769.com"

    def send_request(self, url):
        response = requests.get(url, headers=self.headers)

        return response.content

    def parse_data(self, html_str):
        element = etree.HTML(html_str)

        li_list = element.xpath("//ul[@class='title-state-ul']/li")

        content_list = []
        for li in li_list:
            item = dict()
            item['id'] = li.xpath("./span[@class='state1']/text()")[0]
            item['title'] = li.xpath("./span[@class='state3']/a/text()")[0]
            item['topic_url'] = self.base_topic_url + li.xpath("./span[@class='state3']/a/@href")[0]
            item['published_time'] = li.xpath("./span[@class='state5 ']/text()")[0]
            item['status'] = li.xpath("./span[@class='state2']/text()")[0].strip()
            item['response_time'] = li.xpath("./span[@class='state4']/text()")[0].strip()
            content_list.append(item)

        return content_list

    def save_data(self, content_list):
        with open('sun.json', 'a', encoding="utf8") as f:
            content = json.dumps(content_list, ensure_ascii=False, indent=1)
            f.write(content)

    def run(self):
        content_list = []
        for page in range(1, self.page_count + 1):
            url = self.url.format(page)
            content = self.send_request(url)
            content_list += self.parse_data(content)
        self.save_data(content_list)


if __name__ == '__main__':
    spider = SunSpider(1)
    spider.run()




































