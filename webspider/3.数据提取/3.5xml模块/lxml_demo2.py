#!usr/bin/python
# -*- coding:utf8 -*-
from lxml import etree


text = ''' <div> <ul> 
        <li class="item-1"><a href="link1.html">first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div> '''


element = etree.HTML(text)
# element.xpath('xpath_str')在浏览器中怎么去书写xpath 在这个方法中也怎么去书写

# 获取所有的新闻标题
title_list = element.xpath('//li/a/text()')
print(title_list)
# 获取到所有的详情页连接 href
href_list = element.xpath('//li/a/@href')
print(href_list)

news_list = []
for title in title_list:
    item = dict()
    item['title'] = title
    # list.index(x[,start[,end]]) 从列表中找出某个值第一个匹配项的索引位置 
    item['href'] = href_list[title_list.index(title)]
    news_list.append(item)

print(news_list)













