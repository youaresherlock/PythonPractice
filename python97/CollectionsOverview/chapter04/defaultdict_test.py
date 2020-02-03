#!usr/bin/python
# -*- coding:utf8 -*-

from collections import defaultdict

# 统计字符串出现的次数
users = ["bobby1", "bobby2", "bobby3", "bobby1", "bobby2", "bobby2"]
user_dict = {}
# 影响代码的可读性
# for user in users:
#     if user not in user_dict:
#         user_dict[user] = 1
#     else:
#         user_dict[user] += 1
# for user in users:
#     user_dict.setdefault(user, 0)
#     user_dict[user] += 1
# print(user_dict)

# defaultdict参数传递可调用对象名称
# default_dict = defaultdict(int)
# for user in users:
#     default_dict[user] += 1
# print(default_dict)

def gen_default():
    return {
        "name": "",
        "nums": 0
    }
# 生成dict嵌套dict结构
default_dict = defaultdict(gen_default)
print(default_dict["group1"]) # {'name': '', 'nums': 0}


