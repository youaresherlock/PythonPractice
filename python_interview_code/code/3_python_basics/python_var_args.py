#!usr/bin/python
# -*- coding:utf8 -*-

def print_multiple_args(*args):
    print(type(args), args)
    for idx, val in enumerate(args):
        print(idx, val)

print_multiple_args('a', 'b', 'c')
print_multiple_args(*['a', 'b', 'c'])

def print_kwargs(**kwargs):
    print(type(kwargs), kwargs)
    # for k, v in kwargs.items(): # dict.items()以列表返回可遍历的(键，值）元祖数组
    for k, v in enumerate(kwargs):
        # 不设置指定位置， 按默认顺序
        print('{}: {}'.format(k, v))

print_kwargs(a=1, b=2)
print_kwargs(**dict(a=1, b=2))
print_kwargs(**{'a': 1, 'b': 2})

def print_all(a, *args, **kwargs):
    print(a)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

print_all('hello', 'world', name='muke')