#!usr/bin/python
# -*- coding:utf8 -*-
"""
使用装饰器 contextlib.contextmanager，
来定义自己所需的基于生成器的上下文管理器，用以支持 with 语句

基于类的上下文管理器更加 flexible，适用于大型的系统开发；
而基于生成器的上下文管理器更加方便、简洁，适用于中小型程序。
"""
from contextlib import contextmanager


# 基于生成器的上下文管理器
@contextmanager
def file_manager(name, mode):
    try:
        f = open(name, mode)
        yield f
    finally:
        f.close()


with file_manager('test.txt', 'w') as f:
    f.write('hello world')