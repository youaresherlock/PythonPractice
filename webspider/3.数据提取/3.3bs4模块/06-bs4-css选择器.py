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

# 标签选择器 直接写标签名
# res = soup.select('a')
# print(res)

# 类选择器 .类属性对应的值
# res = soup.select('.title')
# print(res)

# id选择器 #id的值
# res = soup.select('#link2')
# print(res)

# 层级选择器 根据标签的结构一层一层写 每个层级之间用空格隔开
# res = soup.select('p b')
# print(res)

# 属性选择器 标签名[属性名=属性值]
# res = soup.select('a[id="link1"]')
# print(res)

# 先试用选择器 定位到class=title的标签，获取标签中包含的文本内容
res = soup.select("p[class='title']")
for r in res:
    print(r.get_text())
    print(r.get('name'))  # 获取属性所对应的内容



