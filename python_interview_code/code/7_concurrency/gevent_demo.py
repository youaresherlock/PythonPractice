#!usr/bin/python
# -*- coding:utf8 -*-

import gevent.monkey
gevent.monkey.patch_all() #

import gevent
import requests

def fetch(i):
    url = 'http://httpbin.org/get'
    resp = requests.get(url)
    print(len(resp.text), i)

def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Asynchronous:')
asynchronous()
