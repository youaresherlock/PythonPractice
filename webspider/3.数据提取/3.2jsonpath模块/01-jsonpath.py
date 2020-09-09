#!usr/bin/python
# -*- coding:utf8 -*-
"""
pip3 install jsonpath
"""
from jsonpath import jsonpath


my_dict = {'key1': {'key2': {'key3': {'key4': {'key5': {'key6': '张三'}}}}}}

# res = my_dict['key1']['key2']['key3']['key4']['key5']['key6']
#
# print(res)

# jsonpath(my_dict, jsonpath语法规则字符串)
res = jsonpath(my_dict, '$..key6')[0]
print(res)

















