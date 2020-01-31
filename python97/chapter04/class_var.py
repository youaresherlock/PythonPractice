#!usr/bin/python
# -*- coding:utf8 -*-

class A:
    aa = 1 # 类变量
    def __init__(self, x, y):
        # 实例变量
        self.x = x
        self.y = y

a = A(2, 3)
A.aa = 11
a.aa = 100
print(a.x, a.y, a.aa)
print(A.aa)