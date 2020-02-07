#!usr/bin/python
# -*- coding:utf8 -*-

from collections import ChainMap

user_dict1 = {"a": "bobby1", "b": "bobby2"}
user_dict2 = {"b": "bobby4", "d": "bobby3"}
# 遍历
for key, value in user_dict1.items():
    print(key, value)
for key, value in user_dict2.items():
    print(key, value)
new_dict = ChainMap(user_dict1, user_dict2)
# 将多个字典连接起来
for key, value in new_dict.items():
    print(key, value)
print(new_dict['b'])
print(new_dict.maps)
new_dict.maps[0]['a'] = "bobby"
print(user_dict1)



