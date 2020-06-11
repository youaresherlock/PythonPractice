#!usr/bin/python
# -*- coding:utf8 -*-
# 利用类实现单例模式 支持多线程的单例模式
import time
import threading


class Singleton(object):
    _instance_lock = threading.Lock()
    def __init__(self):

        time.sleep(1)

    @classmethod
    def instance(cls, *args, **kwargs):
        with cls._instance_lock:
            if not hasattr(Singleton, '_instance'):
                Singleton._instance = Singleton()
                return Singleton._instance
            return Singleton._instance


def task():

    obj = Singleton.instance()
    print(obj)


for i in range(10):
    t = threading.Thread(target=task)
    t.start()