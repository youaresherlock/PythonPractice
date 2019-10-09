#!usr/bin/python
# -*- coding:utf8 -*-

# 列表/字典推导式
a = ['a', 'b', 'c']

b = [1, 2, 3]

# d = {'a': 1, 'b': 2, 'c': 3}
d = {}
for i in range(len(a)):
    d[a[i]] = b[i]
print(d)

d = {k: v for k, v in zip(a, b)}
print(d)