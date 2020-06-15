#!usr/bin/python
# -*- coding:utf8 -*-
"""
__slots__: 限制实例可以添加的变量
"""


def print_doc(self):
    print("haha")


class Foo:
    __slots__ = ("name", "age")
    pass


obj1 = Foo()
obj2 = Foo()
# 动态添加实例变量
obj1.name = "jack"
obj2.age = 18
obj1.sex = "male"       # 这一句会弹出错误
# 但是无法限制给类添加方法
Foo.show = print_doc
obj1.show()
obj2.show()
