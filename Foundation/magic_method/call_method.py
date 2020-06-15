#!usr/bin/python
# -*- coding:utf8 -*-
"""
__call__: callable object
"""


class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("__call__")


obj = Foo()
obj()
