#!usr/bin/python
# -*- coding:utf8 -*-
"""
装饰器版本
"""


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Student:
    pass


s1 = Student()
s2 = Student()
print(id(s1), id(s2))