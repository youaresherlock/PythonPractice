#!usr/bin/python
# -*- coding:utf8 -*-
my_list = []
my_list.append(1)
my_list.append("a")

# 容器相关的抽象基类
from collections import abc

a = [1, 2]
# a = list()
# c为新的list + 符号两边都为list才能相加 否则抛出异常
c = a + [3, 4]
# print(c)

# +=  就地加 将a本身作一个变化 += 任意的序列类型，通过一个魔法函数来实现__iadd__ 调用了extend方法
a += (3, 4)

# extend(Iterable) 直接在a修改，没有返回值
a.extend(range(3))
# 直接整体放入list
a.append([1,2])
# 放入tuple 
a.append((1, 2))
print(a)


































