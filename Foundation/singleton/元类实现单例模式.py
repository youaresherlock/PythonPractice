#!usr/bin/python
# -*- coding:utf8 -*-
"""
元类是用于创建类对象的类, 类对象创建实例对象时一定要调用call方法,
因此在调用call时候保证只创建一个实例即可,type是python的元类
"""


class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Student(metaclass=Singleton):
    pass


s1 = Student()
s2 = Student()
print(s1 is s2)
