#!usr/bin/python
# -*- coding:utf8 -*-
import requests


url = 'https://api.github.com/'
headers = {'User-Agent': 'clarence'}

response = requests.get(url, headers=headers)
print(response.status_code)
# 响应内容 bytes
print(response.content)
# 响应内容 str
print(response.text)
# 响应内容 dict
print(response.json())
print(response.headers['content-type'])
response.close()


















