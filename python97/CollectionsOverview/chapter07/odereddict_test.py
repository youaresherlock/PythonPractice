#!usr/bin/python
# -*- coding:utf8 -*-
from collections import OrderedDict

# user_dict = dict() python3字典默认是有序的 python2是无序的
user_dict = OrderedDict()
user_dict["b"] = "bobby2"
user_dict["a"] = "bobby1"
user_dict["c"] = "bobby3"
user_dict.move_to_end('b')
print(user_dict)
# 保存添加顺序
print(user_dict.popitem()) # 返回(key, value) 元组
# 传递key值
print(user_dict.pop('a'))
print(user_dict)


































