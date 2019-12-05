#!usr/bin/python
# -*- coding:utf8 -*-

import gevent.monkey
gevent.monkey.patch_all() # 修改内置的一些库为非阻塞

import gevent
import requests

def fetch(i):
    url = 'http://httpbin.org/get'
    resp = requests.get(url)
    print(resp.json(), i)

def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Asynchronous:')
asynchronous()
