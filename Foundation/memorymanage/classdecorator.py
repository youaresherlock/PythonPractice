#!usr/bin/python
# -*- coding:utf8 -*-
"""
闭包:
    1. 函数嵌套定义
    2. 内部函数使用外部函数作用域内的变量
    3. 外部函数要有返回值,返回内部函数名
外函数在返回内函数的引用，发现内函数使用了外函数的局部变量
该局部变量不能被销毁, 而是和内函数的引用进行绑定，存储在一个特定的空间,该空间称为闭包

绑定的时机: 外函数返回时，此时局部变量的值已经固定
"""


"""
def func():
    temp = [lambda x: x * i for i in range(4)]
    return temp 
for each in func():
    print(each(2))
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





























