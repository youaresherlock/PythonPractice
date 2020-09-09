#!usr/bin/python
# -*- coding:utf8 -*-
"""
session的使用
"""
import requests

# 准备请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}

# 登录的url地址
login_url = "http://www.jxmjc.com/login.php?"
# 登录之后访问的页面
my_url = "http://www.jxmjc.com/u.php"

# 请求体数据
data = {
    "lgt": 0,
    "pwuser": "itcast_test",
    "pwpwd": 123456,
    "hideid": 0,
    "forward": "",
    "jumpurl": "http://www.jxmjc.com/u.php?verify=7de38797",
    "m": "bbs",
    "step": 2,
    "cktime": 31536000,
}

# 创建session对象
session = requests.session()

# 使用session发送登录请求
response = session.post(login_url, headers=headers, data=data)
print(response.cookies)

# cookie_jar和cookie_dict之间的转换
cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies_dict)
cookies_jar = requests.utils.cookiejar_from_jar(cookies_dict)
print(cookies_jar)

# # 使用session再次去请求登陆之后的页面
# response = session.get(my_url, headers=headers)
#
# print(response.content.decode("gbk"))
#
# with open('login_html.html', 'w', encoding='gbk') as f:
#     f.write(response.content.decode('gbk'))



























