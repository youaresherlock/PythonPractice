#!usr/bin/python
# -*- coding:utf8 -*-

import asyncio
import datetime
import random

'''
用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用
yield from调用另一个coroutine实现异步操作
为了简化并更好地标识异步IO，从Python3.5开始引入了新的语法async和await,可以让coroutine的代码更简洁易读
1. 把@asyncio.coroutine替换为async
2. 把yield from 替换为await
'''

async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print('Loop: {} Time: {}'.format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(random.randint(0, 5))

loop = asyncio.get_event_loop()
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
loop.run_forever()

























