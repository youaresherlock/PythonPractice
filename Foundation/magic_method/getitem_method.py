#!usr/bin/python
# -*- coding:utf8 -*-
"""
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


obj = Foo()

result = obj['k1']      # 自动触发执行 __getitem__

obj['k2'] = 'jack'      # 自动触发执行 __setitem__

del obj['k1']     # 自动触发执行 __delitem__
