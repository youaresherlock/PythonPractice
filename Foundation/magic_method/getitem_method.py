#!usr/bin/python
# -*- coding:utf8 -*-
"""
getattribute: 无论访问的属性存在或者不存在,都会调用, 同时存在也会调用getattribute方法
重载__getattr__方法对类及其实例未定义的属性有效。
也就属性是说，如果访问的属性存在，就不会调用__getattr__方法。
这个属性的存在，包括类属性和实例属性
(1)__setattr__(self, item, value):
会拦截所有属性的的赋值语句，如果定义了这个方法，在给属性变量赋值时会调用__setattr__(self, item, value)方法，执行self.__dict__[key] = value。当在__setattr__(self, item, value)方法内对属性进行赋值时，不可使用self.name = value,因为他会再次调用__setattr__(self, item, value)方法形成无限循环，最后导致堆栈溢出异常。应该通过对属性字典做索引运算来赋值任何实例属性，也就是使用self.__dict__[‘name’] = value.
(2)__setitem__(self, key, value):
同setattr方法类似，会拦截所有属性的赋值语句，区别在于如果将对象当作字典操作，设置键值对时会触发该方法，同样在__setitem__(self, key, value)方法内对属性进行赋值时，也不能使用self.name = value，而应该使用self.__dict__[‘name’] = value.
__getitem__,__setitem__,__delitem__: 取值、赋值、删除数据
"""


class Foo:

    def __getitem__(self, key):

        print('__getitem__',key)

    def __setitem__(self, key, value):

        print('__setitem__',key,value)

    def __delitem__(self, key):

        print('__delitem__',key)

    def __getattr__(self, item):
        print('getattr', item)

    def __getattribute__(self, item):
        print("getattribute", item)


obj = Foo()

# result = obj['k1']      # 自动触发执行 __getitem__
#
# obj['k2'] = 'jack'      # 自动触发执行 __setitem__
#
# del obj['k1']     # 自动触发执行 __delitem__
obj.name


# class Person(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age  = age
#
#     # 在访问一个存在的属性时,新增提示功能
#     def __getattribute__(self, name):
#         print("你正在访问一个存在属性")
#
#         # return getattr(self, name)       # 递归错误，默认1000次
#         # return self.__dict__[name]       # 递归错误，默认1000次
#         return super(Person, self).__getattribute__(name)
#
#     # 找不到attribute的时候，会调用getattr，返回一个值或AttributeError异常
#     def __getattr__(self, name, value):
#         # setattr(self, name, value)
#         self.__dict__[name] = value
#
#
# if __name__ == '__main__':
#     p = Person('jaon', 25)
#     print(p.name)

