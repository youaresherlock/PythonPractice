#!usr/bin/python
# -*- coding:utf8 -*-

from collections import namedtuple

# 创建了一个User类
User = namedtuple("User", ["name", "age", "height", "edu"])
# user = User(name="bobby", age=29, height=175)
user_tuple = ("bobby", 29, 175)
user = User(*user_tuple, "master")
"""
user_dict = {
    "name": "bobby", 
    "age": 29, 
    "height": 175
}
user = User(**user_dict, edu="master")
"""
print(user.age, user.name, user.height)

# 函数参数
def ask(*args, **kwargs):
    pass

ask("bobby", 29)



















