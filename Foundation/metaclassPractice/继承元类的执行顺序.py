#!usr/bin/python
# -*- coding:utf8 -*-
"""
生成Student类对象；
Singleton是一个元类,调用new方法生成Student类对象
接下来执行init方法,new方法的返回值给init的cls参数,
进行Student类对象的初始化
生成Student的实例对象:
先调用Student继承的元类中的call方法, call方法必须返回
一个实例, 然后再执行Student的new和init方法
"""


class Singleton(type):

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        print('Singleton __init__')
        print(cls, name, bases, attrs)

    # mcs为元类对象
    def __new__(mcs, name, bases, attrs):
        print('Singleton __new__')
        print(mcs, name, bases, attrs)
        return super().__new__(mcs, name, bases, attrs)

    """
    在元类Singleton中重写__call__方法,__call__会抢在Student类执行
    __new__和__init__之前执行,也就为拦截类的实例化提供了可能
    """
    def __call__(cls, *args, **kwargs):
        print('Singleton __call__')
        print(cls, args, kwargs)
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Student(metaclass=Singleton):

    def __new__(cls, *args, **kwargs):
        print('Student __new__')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print('Student __init__')


s = Student()