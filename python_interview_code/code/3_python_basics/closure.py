#!usr/bin/python
# # -*- coding:utf8 -*-

from functools import wraps

def cache(func): # 装饰器
    store = {} # 外部变量

    @wraps(func)
    # 按照习惯，有时候单个独立下划线是用作一个名字，来表示某个变量是临时的或无关紧要的
    def _(n):  # 闭包函数
        if n in store:
            print('取出缓存值{}:{}'.format(n, store[n]))
            return store[n]
        else:
            res = func(n)
            print('计算缓存值{}:{}'.format(n, res))
            store[n] = res
            return res
    return _

@cache
def f(n): # fabonacci
    if n <= 1:
        return 1
    return f(n-1) + f(n-2)

print(f(10))

'''
计算缓存值1:1
计算缓存值0:1
计算缓存值2:2
取出缓存值1:1
计算缓存值3:3
取出缓存值2:2
计算缓存值4:5
取出缓存值3:3
计算缓存值5:8
取出缓存值4:5
计算缓存值6:13
取出缓存值5:8
计算缓存值7:21
取出缓存值6:13
计算缓存值8:34
取出缓存值7:21
计算缓存值9:55
取出缓存值8:34
计算缓存值10:89
89
'''