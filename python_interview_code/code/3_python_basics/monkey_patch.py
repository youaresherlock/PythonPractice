#!usr/bin/python
# -*- coding:utf8 -*-

import socket
print(socket.socket)

print("After monkey patch")
from gevent import monkey
monkey.patch_socket()
print(socket.socket)

import select
print(select.select)
monkey.patch_select()
print("After monkey patch")
print(select.select)

# 运行时类型替换 简单实现monkey patch
import time
print(time.time())

def _time():
    return 1234

time.time = _time
print(time.time())
