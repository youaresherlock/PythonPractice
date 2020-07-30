#!usr/bin/python
# -*- coding:utf8 -*-
"""
__eq__方法如果不重写，默认比较依然是内存地址
列表重载了__eq__方法,逐个比较列表中的元素看是否相等
==会调用对象的__eq__方法,获取这个方法的比较结果
"""


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


s1 = Student('lucy', 18)
s2 = Student('lucy', 18)
s3 = Student('lucy', 20)

# s1 == s2本质是调用 p1.__eq__(p2),获取这个方法的返回结果
print(s1 == s2)  # True
print(s1 == s3)  # False