#!usr/bin/python
# -*- coding:utf8 -*-
# 加上锁
import time
import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)
        print(self)

    def __new__(cls, *args, **kwargs):
        with cls._instance_lock:
            if not hasattr(cls, '_instance'):
                cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


def task():
    obj = Singleton()
    print(id(obj))


for i in range(10):
    t = threading.Thread(target=task)
    t.start()























