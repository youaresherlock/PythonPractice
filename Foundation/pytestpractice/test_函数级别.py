#!usr/bin/python
# -*- coding:utf8 -*-
"""
setup_function和teardown_function每个测试用例都会执行,不能在类中使用,否则无效
setup_method和teardown_method每个测试用例都会执行,但是是只在类里面的方法,否则无效
"""
import pytest


def setup_function():
    print("setup_function(): 每个方法之前执行")


def teardown_function():
    print("teardown_function(): 每个方法之后执行")


def test_01():
    print('正在执行test1')
    x = 'this'
    assert 'h' in x

@pytest.mark.skip()
def test_02():
    print('正在执行test2')
    x = 'hello'
    assert hasattr(x, 'hello')


def add(a, b):
    return a+b


def test_add():
    print("正在执行test_add()")
    assert add(3, 4) == 7


if __name__ == '__main__':
    pytest.main(['-s', "test_simple.py"])





































