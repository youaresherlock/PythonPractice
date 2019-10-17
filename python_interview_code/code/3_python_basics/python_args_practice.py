#!usr/bin/python
# -*- coding:utf8 -*-

# 小例题
def clear_list(l):
    print('clear_list_end', id(l))
    l = []
    print('clear_list_end', id(l))


ll = [1, 2, 3]
print(ll)
clear_list(ll)
print(ll)


# python可变参数作为默认参数
# 默认参数只计算一次
def flist(l=[1]):
    print('flist', l)
    l.append(l)
    print(l)
flist()
flist()

# '...' 省略 用来省略代码/循环数据结构，一个复合对象包含指向自身的引用
test = [1, [...]]
print(test)
print(Ellipsis)
print(bool(Ellipsis))
