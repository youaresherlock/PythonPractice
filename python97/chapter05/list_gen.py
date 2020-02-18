#!usr/bin/python
# -*- coding:utf8 -*-

# 列表生成式(列表推导式)
# 1. 提取出1-20之间的奇数
# odd_list = []
# for i in range(21):
#     if i % 2 == 1:
#         odd_list.append(i)

# odd_list = [i for i in range(21) if i % 2 == 1]
# print(odd_list)

# 2. 逻辑复杂的情况 如果是奇数将结果平方
# 列表生成式性能高于列表操作
def handle_item(item):
    return item * item
odd_list = [handle_item(i) for i in range(21) if i % 2 == 1]
print(odd_list)

# 生成器表达式
odd_gen = (i for i in range(21) if i % 2 == 1)
print(type(odd_gen))
for item in odd_gen:
    print(item)

# 字典推导式
my_dict = {"bobby1": 22, "bobby2": 23, "imooc.com": 5}
reversed_dict = {value:key for key, value in my_dict.items()}
print(reversed_dict)

# 集合推导式
my_set = set(my_dict.keys())
my_set = {key for key, value in my_dict.items()}
print(type(my_set))













