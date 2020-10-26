#!usr/bin/python
# -*- coding:utf8 -*-
"""
共享属性
"""


class Singleton(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Singleton, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class Student(Singleton):
    pass


s1 = Student()
s1.name = 'clarence'
s2 = Student()
print(s2.name)  # 'clarence'
print(id(s1.__dict__), id(s2.__dict__))
