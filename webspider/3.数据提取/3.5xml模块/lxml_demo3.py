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

li_list = element.xpath('//li')
for li in li_list:
    title = li.xpath('./a/text()')[0]
    href = li.xpath('./a/@href')[0] if len(li.xpath('./a/@href')) > 0 else None
    print(title, href)










