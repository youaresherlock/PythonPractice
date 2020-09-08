#!usr/bin/python
# -*- coding:utf8 -*-
import requests


url = 'https://www.api.github.com'
response = requests.get(url)

print(response.status_code)
print(response.encoding)
# response.context bytes类型
# response.text = response.content.decode('按照chardet
# 模块推测出的编码字符集进行解码的结果') str
print(response.json())

