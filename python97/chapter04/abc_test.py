#!usr/bin/python
# -*- coding:utf8 -*-

# 检查某个类是否有某种方法
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

com = Company(["bobby1", "bobby2"])
print(len(com))
print(hasattr(com, "__len__")) # 对象是否有这个属性
print(isinstance(com, Company))
# 我们在某些情况之下希望判定某个对象的类型
from collections.abc import Sized
print(isinstance(com, Sized)) # True Sized类型


# 我们需要强制某个子类必须实现某些方法
# 实现了一个web框架，集成cache(redis, cache, memorycache)
# 需要设计一个抽象积基类， 指定子类必须实现某些方法



























