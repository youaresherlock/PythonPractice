#!usr/bin/python
# -*- coding:utf8 -*-
"""
变量作用域
Python的作用域一共有4种,分别是
L(Local) 局部作用域、 E(Enclosing) 闭包函数外的函数中、 G(Global)全局作用域、B(Built-in)内置作用域(内置函数所有模块的范围)
以L->E->G->B的规则查找
内置作用域是通过一个名为builtin的标准模块来实现的
"""
import builtins

for each in dir(builtins):
    print(each)

"""
当内部作用域想修改外部作用域的变量时，就要用到gobal和nonlocal关键字
"""
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)

def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()
































