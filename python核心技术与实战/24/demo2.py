#!usr/bin/python
# -*- coding:utf8 -*-
import os
import psutil

a = None


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def func():
    show_memory_info('initial')
    global a
    a = [i for i in range(10000000)]
    show_memory_info('after a created')


func()
show_memory_info('finished')


"""
global a 表示将 a 声明为全局变量。那么，即使函数返回后，
列表的引用依然存在，于是对象就不会被垃圾回收掉，依然占用大量内存
"""


