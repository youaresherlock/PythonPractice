#!usr/bin/python
# -*- coding:utf8 -*-

# Python中垃圾回收的算法是采用引用计数法为主 标记清除和分代回收为辅

a = object()
b = a
del a
print(b)
# print(a)

class A:
    def __del__(self):
        pass 