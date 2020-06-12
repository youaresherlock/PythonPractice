#!usr/bin/python
# -*- coding:utf8 -*-
from concurrent.futures import ThreadPoolExecutor
import time


def return_after_2_secs(message):
    time.sleep(2)
    return message


pool = ThreadPoolExecutor(3)
future = pool.submit(return_after_2_secs, message='hello')
print(future.done())
time.sleep(3)
print(future.done())
print('Result: ', future.result())

