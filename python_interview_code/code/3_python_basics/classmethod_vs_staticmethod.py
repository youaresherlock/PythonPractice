#!usr/bin/python
# # -*- coding:utf8 -*-

'''
python类语法中有三种方法, 实例方法、静态方法、类方法
实例方法: 只能被实例对象调用 第一个参数必须默认传实例对象, 一般习惯self
静态方法: 由@staticmethod装饰的方法 可以被类或类的实例对象调用 参数没有要求
类方法: 由@classmethod装饰的方法 可以被类或类的实例对象调用 第一个参数必须要默认传类，一般习惯用cls

'''

class Person:
    country = 'china' # class var

    def __init__(self, name):
        self.name = name

    # 类方法
    @classmethod
    def print_country(cls):
        print(cls.country)

    # 静态方法
    @staticmethod
    def join_name(first_name, last_name):
        return last_name + ' ' + first_name

    # 实例方法
    def show_name(self):
        print("my name is {}".format(self.name))

p = Person('clarence')
p.print_country()
print(p.join_name('clarence', 'sampson'))