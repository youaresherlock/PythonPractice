#!usr/bin/python
# -*- coding:utf8 -*-
# class type(name, bases, dict)

X = type('X', (object, ), dict(a=1, say=sum, __doc__="这是type创建的对象"))
x = X()
print(X.say([1, 2, 3]))
# 除了可以通过type函数判断对象类型,还可以通过__class__属性获取
print(X.__class__) # 父类
print(X.__name__) # 类名
print(X.__bases__) # 基类元组
print(X.__dict__)
x.name = 'clarence'
x.password = '123'
print(x.__dict__) # self.xxx
print(X.__doc__) # 类的说明










