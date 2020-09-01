#!usr/bin/python
# -*- coding:utf8 -*-
"""
setup_module和teardown_module作用于一个模块内的所有class和def, 对于
所有class和def,setup和teardown只执行一次
"""
import pytest


def setup_module():
    print("setup_module():在模块最之前执行")


def teardown_module():
    print("teardown_module：在模块之后执行")


def setup_function():
    print("setup_function():每个方法之前执行")


def teardown_function():
    print("teardown_function():每个方法之后执行")


def test_10():
    print("正在执行test10")
    x = "this"
    assert 'h' in x


def sum(a,b):
    return a+b


def test_add():
    print("正在执行test_add()")
    assert sum(3,4) == 7


class TestMethod(object):
    def setup_class(self):
        print("setup_class(self)：每个类之前执行一次")

    def teardown_class(self):
        print("teardown_class(self)：每个类之后执行一次")

    def setup_method(self):
        print("setup_method(self):在每个方法之前执行")

    def teardown_method(self):
        print("teardown_method(self):在每个方法之后执行\n")

    def add(self,a,b):
        print("这是加法运算")
        return a+b

    def test_01(self):
        print("正在执行test1")
        x = "this"
        assert 'h' in x

    def test_add(self):
        print("正在执行test_add()")