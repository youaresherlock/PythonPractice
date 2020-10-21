#!usr/bin/python
# # -*- coding:utf8 -*-

class Base:
    pass

class Child(Base):
    pass

# 等价定义， 注意Base后面要加上逗号否则就不是tuple了
SameChild = type('Child', (Base,), {})

# 加上方法
class ChildWithMethod(Base):
    bar = True

    def hello(self):
        print('hello')

def hello(self):
    print('hello')

# 等价定义
ChildWithMethod = type(
    'ChildWithMethod', (Base,), {'bar': True, 'hello': hello}
)

# 元类继承自type
class LowercaseMeta(type):
    """ 修改类的属性名称为小写的元类 """
    def __new__(mcs, name, bases, attrs):
        lower_attrs = {}
        for k, v in attrs.items():
            if not k.startswith('__'): # 排除magic method
                lower_attrs[k.lower()] = v
            else:
                lower_attrs[k] = v
        return type.__new__(mcs, name, bases, lower_attrs)

class LowercaseClass(metaclass=LowercaseMeta): # python3
    BAR = True

    def HELLO(self):
        print('hello')

print(dir(LowercaseClass)) # 'BAR'和'HELLO'都变成了小写
# 用一个类的实例调用hello方法，我们修改了类定义时候的属性名!!!
LowercaseClass().hello()





























