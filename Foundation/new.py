#!usr/bin/python
# -*- coding:utf8 -*-

"""
new()方法是在类准备将自身实例化时调用
new()方法始终都是类的静态方法, 即使没有被加上静态方法装饰器
"""


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, name, age):
        if 0 < age < 150:
            # return object.__new__(cls)
            return super(Person, cls).__new__(cls)
        else:
            return None

    def __str__(self):
        print(self.__class__, self.__class__.__name__, self.__dict__)
        return '{0}({1})'.format(self.__class__.__name__, self.__dict__)


print(Person('Tom', 10))
print(Person('Mike', 200))