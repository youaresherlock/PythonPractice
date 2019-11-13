#!usr/bin/python
# -*- coding:utf8 -*-

"""
python3中父类默认继承object, 可以不写.
1. 初始化父类一般使用的是子类直接调用父类的__init__方法
        父类类名.__init__(self, args)
父类的初始化顺序和继承顺序相同(实际上是子类的调用父类的初始化顺序)

如下所示
class first(object):
    def __init__(self, value):
        self.value = value

class son_of_first(first):
    def __init__(self):
        first.__init__(self, 9)

class first(object):
    def __init__(self, value):
        self.value = value

class son_of_first(first):
    def __init__(self):
        first.__init__(self, 9)

child = son_of_first()
print(child.value) // 9

菱形继承体系: 菱形继承就是子类继承自两个不同的超类，这两个超类
有一个公共的基类，形成一个类似竖着的菱形的继承样式，所以叫做菱形继承体系.
在顶部顶点的基类会执行多个初始化方法(__init__)

示例:
class first(object):
    def __init__(self, value):
        self.value = value

class second(first):
    def __init__(self,value):
        first.__init__(self,value)
        self.value += 8

class third(first):
    def __init__(self,value):
        first.__init__(self,value)
        self.value *= 7

class four(second,third):
    def __init__(self,value):
        second.__init__(self,value)
        third.__init__(self,value)

child = four(5)
# 调用第二个超类的时候，再度调用了first 这与four的__init__中父类初始化的顺序有关
print(child.value) # 35

2. super()函数是用于调用父类的一个方法
super()用来解决多重继承问题,直接用类名调用父类方法在使用单继承的时候没问题，但如果使用多继承,
会涉及到查找顺序(MRO 类的方法解析顺序表,即继承父类方法时的顺序表)，重复调用(钻石继承)等种种问题.

python3可以直接使用super().__init__(value)代替python2中的super(Class, self).__init__(value)
在python3中可以使用__class__准确拿到当前类
super(__class__, self).__init__(value)
"""

class A():
    def __init__(self):
        print('enter A')
        print('leave A')


class B(A):
    def __init__(self):
        print('enter B')
        super().__init__()
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')


class D(B, C):
    def __init__(self):
        print('enter D')
        # super().__init__()
        super(__class__, self).__init__()
        print('leave D')

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro()) # D继承顺序表
d = D()