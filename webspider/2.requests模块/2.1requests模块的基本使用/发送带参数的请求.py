#!usr/bin/python
# -*- coding:utf8 -*-
"""
http协议传递参数的四种方式:
1. 查询字符串
2. 路径传参
3. 请求体传参
    请求体表单传参
    请求体非表单json传参
4. 请求头传参
"""
# 方式一：利用params参数发送带参数的请求
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# 这是目标url
# url = 'https://www.baidu.com/s?wd=python'

# 最后有没有问号结果都一样
url = 'https://www.baidu.com/s?'

# 请求参数是一个字典 即wd=python
kw = {'wd': 'python'}

# 带上请求参数发起请求，获取响应
response = requests.get(url, headers=headers, params=kw)

# 当有多个请求参数时，requests接收的params参数为多个键值对的字典，比如 '?wd=python&a=c'-->{'wd': 'python', 'a': 'c'}

print(response.content)
"""
# 方式二：直接发送带参数的url的请求
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

url = 'https://www.baidu.com/s?wd=python'

# kw = {'wd': 'python'}

# url中包含了请求参数，所以此时无需params
response = requests.get(url, headers=headers)
"""






















