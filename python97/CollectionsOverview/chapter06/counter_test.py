#!usr/bin/python
# -*- coding:utf8 -*-

from collections import Counter

users = ["bobby1", "bobby2", "bobby3", "bobby1", "bobby2", "bobby2"]
# 除了可以统计tuple,list还可以统计字符串
# user_counter = Counter(users)
user_counter = Counter("afafalfejlajf")
user_counter2 = Counter("afjajflk")
# update 传入可迭代对象,counter继承了dict
user_counter.update(user_counter2)
# top n 的问题 用堆实现
print(user_counter.most_common(2))
print(user_counter)
