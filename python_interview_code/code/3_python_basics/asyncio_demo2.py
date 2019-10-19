#!usr/bin/python
# -*- coding:utf8 -*-

import threading
import asyncio

@asyncio.coroutine
def hello():
    print("Hello World! {}".format(threading.currentThread()))
    yield from asyncio.sleep(1)
    print("Hello Again! {}".format(threading.currentThread()))


# 获取EventLoop
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()












