#!usr/bin/python
# -*- coding:utf8 -*-
"""
爬虫获取36kr首页的新闻列表的文章内容
网址：[36kr](https://www.36kr.com/information/web_news/latest)

获取文章字段：
1. 标题
2. 标题对应的url地址
3. 标题对应的图片

最后保存：
​	把所有文本保存为json文件
​	把图片保存到本地的目录中
"""
import os
import re
import json
import requests
from jsonpath import jsonpath


class KrSpider(object):

    def __init__(self):
        self.url = 'https://www.36kr.com/information/web_news/latest'
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
        self.base_url = 'https://www.36kr.com'

    def send_request(self):
        response = requests.get(self.url, headers=self.headers)

        return response.content.decode()

    def parse_data(self, content):
        json_data = re.findall(r'<script>window.initialState=(.*?)</script>', content)[0]
        dict_data = json.loads(json_data)
        news_list = jsonpath(dict_data, '$..itemList')[0]

        results = []
        for news in news_list:
            item = {}
            if news.get('itemId') is None or news.get('route') is None or \
                news.get('templateMaterial').get('widgetTitle') is None or \
                    news.get('templateMaterial').get('widgetImage') is None:
                continue
            item['id'] = news.get('itemId')
            item['url'] = news.get('route')
            item['title'] = news.get('templateMaterial').get('widgetTitle')
            item['image'] = news.get('templateMaterial').get('widgetImage')
            results.append(item)

        return results

    def save_data(self, data):
        with open('36kr.json', 'w', encoding='utf8') as f:
            content = json.dumps(data, ensure_ascii=False, indent=1)
            f.write(content)

        if not os.path.exists('36kr_images'):
            os.mkdir('36kr_images')

        for news in data:
            response = requests.get(news['image'], headers=self.headers)
            with open('36kr_images/{}'.format(str(news['id']) + '.png'), 'wb') as f:
                f.write(response.content)

    def run(self):
        content = self.send_request()
        data_list = self.parse_data(content)
        self.save_data(data_list)


if __name__ == '__main__':
    spider = KrSpider()
    spider.run()











