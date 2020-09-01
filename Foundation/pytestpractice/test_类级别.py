#!usr/bin/python
# -*- coding:utf8 -*-
"""
setup_class和teardown_class作用于一个class内的所有test, 所有用例执行一次
setup和teardown
setup_method和teardown_method作用于class中的每一个test,每个test前都会指向setup
"""
import pytest


class TestMethod(object):

    def setup_class(self):
        print('setup_class(self): 每个类之前执行一次')

    def teardown_class(self):
        print('teardown_class(self): 每个类之后执行一次')

    def setup_method(self):
        print('setup_method(self): 每个方法之前执行一次')

    def teardown_method(self):
        print('teardown_method(self): 每个方法之后执行一次')

    def add(self, a, b):
        print("这是加法运算")
        return a + b

    def test_01(self):
        print("正在执行test1")
        x = "this"
        assert 'h' in x

    def test_add(self):
        print("正在执行test_add()")
































