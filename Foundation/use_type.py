#!usr/bin/python
# -*- coding:utf8 -*-
# class type(name, bases, dict)
import types

x = type('X', (object, ), dict(a=1, say=sum, __doc__="这是type创建的对象"))
print(x.say([1, 2, 3]))
# 除了可以通过type函数判断对象类型,还可以通过__class__属性获取
print(x.__class__)
print(x.__name__)
print(x.__bases__)
print(x.__dict__)
print(x.__doc__)












