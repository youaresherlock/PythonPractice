#!usr/bin/python
# -*- coding:utf8 -*-
"""
https://mil.news.sina.com.cn/roll/index.d.html
获取”中国军情“N页的爬虫，写入json文件中, 每一页的数据写入一个json文件
"""
import os
import json
import requests
from bs4 import BeautifulSoup


class WebSpider(object):

    def __init__(self, page_count):
        print('----------------loading...-----------------')
        self.url = 'https://mil.news.sina.com.cn/roll/index.d.html'
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
        self.page_count = page_count

    def parse(self):
        for page_number in range(1, self.page_count + 1):
            self._parser_and_save(page_number)

    def _get_data(self, page_number):
        params = {'page': page_number}
        response = requests.get(self.url, headers=self.headers, params=params)

        return response.content.decode()

    def _parser_and_save(self, page_number):
        html_str = self._get_data(page_number)
        soup = BeautifulSoup(html_str, 'html.parser')
        # 层级选择器
        news_list = soup.select('.linkNews li a')

        news_results = []
        for news in news_list:
            new_dict = dict()
            new_dict['title'] = news.get_text()
            new_dict['url'] = news.get('href')
            news_results.append(new_dict)

        path = os.path.join(os.getcwd(), 'war_news')
        if not os.path.exists(path):
            os.mkdir(path)

        name = 'news_{}.json'.format(page_number)
        filepath = os.path.join(path, name)
        WebSpider._save_to_json(filepath, news_results)

        print('----------------save {} successfully!--------------'.format(name))

    @staticmethod
    def _save_to_json(filepath, obj):
        with open(filepath, 'w', encoding='utf8') as f:
            content = json.dumps(obj, ensure_ascii=False, indent=1)
            f.write(content)


if __name__ == '__main__':
    spider = WebSpider(10)
    spider.parse()









