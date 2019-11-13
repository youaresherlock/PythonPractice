#!usr/bin/python
# -*- coding:utf8 -*-

"""
python类中的__init__、__new__、__call__方法
__init__方法负责对象的初始化，系统执行该方法前，其实该对象已经存在了
__new__方法的返回值就是类的实例对象，这个实例对象会传递给__init__方法中定义的
self参数，以便实例对象可以被正确地初始化

__call__方法
可调用对象(callable),我们平时自定义的函数、内置函数和类都属于可调用对象，但
凡是可以把一对括号()应用到某个对象身上都可称之为可调用对象,判断对象是否为可调用
对象可以用函数callable
利用这种特性可以实现基于类的装饰器，在类里面记录状态
"""

# class A(object): python2 必须显示的继承object
class A:
    def __init__(self):
        print("__init__")
        # super().__init__()
        print(self)
        super(A, self).__init__()

    def __new__(cls):
        print("__new__")
        self = super(A, cls).__new__(cls)
        print(self)
        return self

    def __call__(self): # 可以定义任何参数
        print("__call__")

a = A()
a()

"""
__new__
<__main__.A object at 0x0000020AF937F550>
__init__
<__main__.A object at 0x0000020AF937F550>
"""



















