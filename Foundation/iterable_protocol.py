#!usr/bin/python
# -*- coding:utf8 -*-
"""
可迭代协议:
可以被for循环的就是可迭代的，目前有字符串，列表，元组，字典，集合
可以被迭代要满足的要求就叫做可迭代协议。可迭代协议的定义非常简单，就是内部实现了__iter__方法。
"""
from collections import Iterable, Sequence

string = "hello"
l = [1, 2, 3, 4]
t = tuple(l)
d = {1: 2, 3: 4}
s = set(l)

for each in [string, l, t, d, s]:
    print(isinstance(each, Iterable))
    # python中的序列类型有字符串,列表,元组
    print(isinstance(each, Sequence))














