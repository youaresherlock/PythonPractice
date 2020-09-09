#!usr/bin/python
# -*- coding:utf8 -*-
"""
获取新浪首页，查看response.text 和response.content.decode()的区别
"""
import locale
import requests

print(locale.getpreferredencoding())  # cp936为gbk别名
url = 'https://www.sina.com.cn/'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/54.0.2840.99 Safari/537.36"}

response = requests.get(url, headers=headers)

print(response.content)
# print(response.content.decode())

# encoding 以什么编码进行写入
with open('sina.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

response.close()
















