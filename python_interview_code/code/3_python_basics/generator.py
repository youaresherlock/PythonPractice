#!usr/bin/python
# -*- coding:utf8 -*-

def simple_gen():
    yield 'hello'
    yield 'world'

gen = simple_gen()
print(type(gen)) # 'generator' object
# print(gen.__next__())
print(next(gen))
print(next(gen))
print(next(gen)) # StopIteration异常 迭代器没有更多的值