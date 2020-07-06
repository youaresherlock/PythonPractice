#!usr/bin/python
# -*- coding:utf8 -*-
import os
import gc
import psutil


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


show_memory_info('initial')

a = [i for i in range(10000000)]

show_memory_info('after a created')

del a
gc.collect()  # 清除没有引用的对象

show_memory_info('finish')
print(a)

