#!usr/bin/python
# -*- coding:utf8 -*-

# python和java中的变量本质不一样 python的变量实质上是一个指针
a = 1
# 1. a贴在1上面
# 2. 先生

a = [1, 2, 3]
b = a
print(a is b)
b.append(4)
print(a)

"""
intern机制 小整数池和小段字符串
a = 1 
b = 1 
print(id(a), id(b))
print(a is b)
"""































