#!usr/bin/python
# -*- coding:utf8 -*-
"""
__module__ 表示当前操作的对象在属于哪个模块
__class__ 表示当前操作的对象属于哪个类
"""


class Foo:
    pass


obj = Foo()
print(obj.__module__)
print(obj.__class__)
"""
__main__
<class '__main__.Foo'>
"""
