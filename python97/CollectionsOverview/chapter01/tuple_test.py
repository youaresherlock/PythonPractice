#!usr/bin/python
# -*- coding:utf8 -*-
# 可迭代对象iterable  实现__iter__或__getitem__方法
name_list = ("bobby1", "bobby2")
# for循环拿到对象的迭代器或者调用__getitem__方法
for name in name_list:
    print(name)

# 元祖拆包
# user_tuple = ("bobby", 29, 175)
# name, age, height = user_tuple
# print(name, age, height)
user_tuple = ("bobby", 29, 175, "beijing")
name, *other = user_tuple
# print(name, *other)
print(name, other)

# tuple不可变不是绝对的
name_tuple = ("bobby", [29, 175])
name_tuple[1].append(22)
print(name_tuple)

# hashable 可以作为dict的key
user_info_dict = {}
user_info_dict[user_tuple] = "bobby"
print(user_info_dict)