#!usr/bin/python
# -*- coding:utf8 -*-


class Student:
    def __init__(self, name):
        self.name = name

    def __contains__(self, item):
        return item.name in self.name


s1 = Student('clarence')
s2 = Student('cla')
print(s2 in s1)  # True