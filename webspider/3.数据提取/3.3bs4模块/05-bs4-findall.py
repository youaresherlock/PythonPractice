#!usr/bin/python
# -*- coding:utf8 -*-
import re
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'html.parser')

"""
text 根据标签文本内容进行搜索 
"""
res = soup.find_all(text='Tillie')
print(res)

"""
attrs参数, 接受到的是一个字典类型 {属性名: 属性值}
limit 限制返回数据的条数
"""
# res = soup.find_all(attrs={'class': 'sister'}, limit=2)
# print(res)

"""
**kwargs key=value 
"""
# res = soup.find_all(class_='sister')
# print(res)

# 根据传入的语法规则,返回所有符合规则的标签内容
"""
name:
    1. 标签名字符串 
    2. 传入正则表达式
    3. 传入列表 
    4. True 递归的获取所有标签 
"""
# res = soup.find_all('a')
# print(res)

# 传入正则的时候,不是直接传入正则表达式的字符串
# 传入一个正则的对象
# res = soup.find_all(name=re.compile('^p'))
# print(res)

# 传入列表 同时传入多个标签
# res = soup.find_all(name=['a', 'p'])
# print(res)

# res = soup.find_all(name=True)
# for r in res:
#     print(r)
#     print('-' * 20)







