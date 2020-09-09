#!usr/bin/python
# -*- coding:utf8 -*-
"""
https://mil.news.sina.com.cn/roll/index.d.html
"""
import json
import requests
from bs4 import BeautifulSoup

url = 'https://mil.news.sina.com.cn/roll/index.d.html'

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content.decode(), 'html.parser')

# 层级选择器
news_list = soup.select('.linkNews li a')

news_results = []
for news in news_list:
    new_dict = dict()
    new_dict['title'] = news.get_text()
    new_dict['url'] = news.get('href')
    news_results.append(new_dict)

print(news_results)
with open('news.json', 'w') as f:
    content = json.dumps(news_results, ensure_ascii=False, indent=1)
    f.write(content)









