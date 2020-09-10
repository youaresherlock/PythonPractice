#!usr/bin/python
# -*- coding:utf8 -*-
"""
https://mil.news.sina.com.cn/roll/index.d.html
获取新浪新闻页”中国军情第一页“的爬虫设计为一个类
"""
import os
import json
import requests
from bs4 import BeautifulSoup


class WebSpider(object):

    def __init__(self):
        print('----------------loading...-----------------')
        self.url = 'https://mil.news.sina.com.cn/roll/index.d.html'
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}

    def _get_data(self, page_number):
        params = {'page': page_number}
        response = requests.get(self.url, headers=self.headers, params=params)

        return response.content.decode()

    def parser_and_save(self, page_number):
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

        filename = os.path.join(path, 'news_{}.json'.format(page_number))
        WebSpider._save_to_json(filename, news_results)

        print('----------------save successfully!--------------')

    @staticmethod
    def _save_to_json(filename, obj):
        with open(filename, 'w') as f:
            content = json.dumps(obj, ensure_ascii=False, indent=1)
            f.write(content)


if __name__ == '__main__':
    spider = WebSpider()
    spider.parser_and_save(1)









