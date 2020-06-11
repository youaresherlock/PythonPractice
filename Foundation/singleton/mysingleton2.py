#!usr/bin/python
# -*- coding:utf8 -*-


class Singleton(object):
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


one = Singleton('aa')
two = Singleton('bb')
print(one.name, two.name)
print(one is two, id(one) == id(two)) # True True