#!usr/bin/python
# -*- coding:utf8 -*-
"""
实现任意贴吧的爬虫，保存多个网页到本地  count = 5 李宇春-1.html
"""
import requests

url = 'https://tieba.baidu.com/f'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/72.0.3626.81 Safari/537.36 "
                         "SE 2.X MetaSr 1.0",
           "Cookie": "BAIDUID=A841C68D45F6AE390770C57C17E7FB2C:FG=1; TIEBA_USERTYPE=43278e022f94aa77c309f107; TIEBAUID=cb23caae14130a0d384a57f1; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1599568416; st_key_id=17; st_data=9be5de493d4cea48f029afb0e13214957bd90b9e2a1ce9cb1bfffe9ae9817768344d770b2916719a791b72cd153f601baeb398341ab653f9e321cc178fe9c5b8dcf5c30df617b547f3a5f65dd8bf78b832287fd1d0924bfec84e6449675a4f03672f0fe55932362541579e67f91d554fcf90be8871268e49cd4207eeeeb78bc9; st_sign=4f40e0b6; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1599569254"
           }

search = input('please input message...')
count = input('please input count number...')

for i in range(int(count)):
    pn = count * 50
    params = {'kw': search, 'pn': pn}
    response = requests.get(url, headers=headers, params=params)
    with open('demo3_{}.html'.format(i), 'w', encoding='utf-8') as f:
        f.write(response.content.decode())

    response.close()
