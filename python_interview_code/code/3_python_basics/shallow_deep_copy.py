#!usr/bin/python
# # -*- coding:utf8 -*-

import copy

alist = [1, 2, 3, ['a', 'b']]

# 直接赋值 引用传递
ref = alist
# shallow copy
shallow = copy.copy(alist)
# deep copy
deep = copy.deepcopy(alist)

print(ref, shallow, deep, sep='\n')

alist.append(5)

print(ref, shallow, deep, sep='\n')

alist[3].append('ccc')

print(ref, shallow, deep, sep='\n')

