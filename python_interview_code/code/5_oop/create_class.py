#!usr/bin/python
# -*- coding:utf8 -*-

# 创建类
class Person(object): # py3直接class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print('my name is {}'.format(self.name))