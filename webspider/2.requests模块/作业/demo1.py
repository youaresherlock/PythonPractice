#!usr/bin/python
# -*- coding:utf8 -*-
"""
获取新浪首页，查看response.text 和response.content.decode()的区别
"""
import requests


url = 'https://www.weibo.com/'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/54.0.2840.99 Safari/537.36"}

response = requests.get(url, headers=headers)

print(response.content)
print(response.content.decode('gbk'))

response.close()
