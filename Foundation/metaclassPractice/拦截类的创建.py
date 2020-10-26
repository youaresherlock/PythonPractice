#!usr/bin/python
# -*- coding:utf8 -*-
"""
元类作用:
    1. 拦截类的创建
    2. 修改类
    3. 返回修改之后的类
"""


def upper_attr(cls, bases, attrs):
    print(cls, bases, attrs)
    new_attrs = {}
    for key, value in attrs.items():
        if not key.startswith('__'):
            new_attrs[key.upper()] = value
    return type(cls, bases, new_attrs)


class UpperAttr(type):

    def __new__(mcs, name, bases, attrs):
        print(mcs, name, bases, attrs)
        new_attrs = {}
        for key, value in attrs.items():
            if not key.startswith('__'):
                new_attrs[key.upper()] = value
        return super().__new__(mcs, name, bases, new_attrs)


class People(object, metaclass=UpperAttr):

    name = 'clarence'
    age = 18

    def show_info(self):
        print('show_info')


p = People()
print(p.NAME)
p.SHOW_INFO()












