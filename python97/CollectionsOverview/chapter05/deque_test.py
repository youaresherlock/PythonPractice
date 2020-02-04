#!usr/bin/python
# -*- coding:utf8 -*-

# deque是线程安全的,list不是线程安全的 
from collections import deque
# user_list = ["bobby", "bobby2"]
# user_name = user_list.pop()
# print(user_name, user_list)

# 参数是iterable,字典也是可迭代对象, 将字典key值作为列表元素
# user_list = deque({
#     "bobby1": 28,
#     "bobby2": 29
# })b
# print(user_list)

user_deque = deque(["bobby1", "bobby2", "bobby3"])
user_deque2 = deque(["bobby11", "bobby21", "bobby31"])
user_deque.extend(user_deque2)
# user_deque.appendleft("bobby8")
print(user_deque)































