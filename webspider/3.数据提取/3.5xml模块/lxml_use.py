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


# 在使用etree.HTML方法的时候会将html缺失的一些标签补充上 
html = etree.HTML(text)
print(type(html))

handeled_html_str = etree.tostring(html).decode()
print(handeled_html_str)

