#!usr/bin/python
# -*- coding:utf8 -*-

class Person:

    country = 'china' # 类变量

    def __init__(self, name):
        self.name = name  # 实例变量

    def print_name(self):
        print(self.name)

laowang = Person('laowang')
laoli = Person('laoli')
laowang.print_name()
laoli.print_name()
print(laowang.country)
print(laoli.country)