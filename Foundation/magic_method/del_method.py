#!usr/bin/python
# -*- coding:utf8 -*-
"""
__del__:析构方法, 当对象在内存中被释放时,自动触发此方法
"""


class Foo:
    def __del__(self):
        print("__del__")


obj = Foo()  # 程序结束自动会被回收
