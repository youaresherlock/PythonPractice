#!usr/bin/python
# -*- coding:utf8 -*-

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        # super(B, self).__init__() # python2用法
        super().__init__() # python3简化用法

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()

# 既然我们重写了B的构造函数，为什么还要调用super
# super到底执行顺序是什么样呢？

if __name__ == "__main__":
    print(D.__mro__)
    d = D()
























