#!usr/bin/python
# -*- coding:utf8 -*-
"""
闭包:
    1. 函数嵌套定义
    2. 内部函数使用外部函数作用域内的变量
    3. 外部函数要有返回值,返回内部函数名
"""


# 函数装饰器
def func_out(func):
    def func_in(*args, **kwargs):
        print("我是新增功能~")
        return func(*args, **kwargs)
    return func_in


@func_out # common = func_out(common)
def common():
    print("我是测试函数")


# common()


class Check(object):
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        # 添加装饰功能
        print("请先登录...")
        self.__fn()


@Check  # popular = Check(popular)
def popular():
    print("我是测试函数")


popular()































