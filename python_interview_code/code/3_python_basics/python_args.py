#!usr/bin/python
# -*- coding:utf8 -*-

# python进行对象引用传递，而不是通过值传递和引用传递

# 可变类型作为参数
def flist(l):
    l.append(0)
    print(id(l))
    print(l)

ll = []
print(id(ll))
flist(ll)
flist(ll)

print('+++++++++++++++++')

# 不可变类型作为参数
def fstr(s):
    print("fstr start")
    print(s, id(s))
    s += 'a'
    print(s, id(s))
    print("fstr end")

ss = 'clarence'
print(ss, id(ss))
fstr(ss)
fstr(ss)
ss += 'a'
print(ss, id(ss))
print(id('clarencea'))

