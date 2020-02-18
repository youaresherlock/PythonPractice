#!usr/bin/python
# -*- coding:utf8 -*-

# 不建议继承list和dict
# class Mydict(dict):
#     # 某些情况下c语言实现的不会调用__setitem__魔法方法
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value*2)
#
# my_dict = Mydict(one=1) # 不生效
# my_dict["one"] = 1 # 生效
# print(my_dict)


# from collections import UserDict
# class Mydict(UserDict):
#     # 某些情况下c语言实现的不会调用__setitem__魔法方法
#     def __setitem__(self, key, value):
#         super().__setitem__(key, value*2)
#
# my_dict = Mydict(one=1)
# print(my_dict)

from collections import defaultdict
my_dict = defaultdict(dict)
my_value = my_dict["bobby"]
print(my_value)




























