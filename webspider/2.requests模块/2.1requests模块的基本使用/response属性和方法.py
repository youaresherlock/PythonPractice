#!usr/bin/python
# -*- coding:utf8 -*-
import requests


url = 'http://www.itcast.cn'

response = requests.get(url)

print(response)
# 响应的url地址
print(response.url)
# 获取响应状态码
print(response.status_code)
# 获取请求头信息
print(response.request.headers)
# 获取响应头的信息
print(response.headers)
# 获取响应中携带的cookie, RequestsCookieJar类型
print(response.cookies)
# 获取请求中携带的cookie
print(response.request._cookies)

response.close()














