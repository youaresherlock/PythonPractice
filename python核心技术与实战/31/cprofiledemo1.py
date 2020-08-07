#!usr/bin/python
# -*- coding:utf8 -*-
from functools import wraps


def cache(func):  # 装饰器
    store = {}  # 外部变量

    @wraps(func)
    # 按照习惯，有时候单个独立下划线是用作一个名字，来表示某个变量是临时的或无关紧要的
    def _(n):  # 闭包函数
        # if n not in store:
        #     store[n] = func(n)
        # return store[n]
        if n in store:
            return store[n]
        else:
            res = func(n)
            store[n] = res
            return res
    return _


@cache
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n-1))
    res.append(fib(n))
    return res


# fib_seq(30)

import cProfile
cProfile.run('fib_seq(30)')
"""
想要测试一下这段代码总的效率以及各个部分的效率
1.
import cProfile
# def fib(n)
# def fib_seq(n):
cProfile.run('fib_seq(30)')
2. 运行脚本的命令中加入-m cProfile

python3 -m cProfile xxx.py


result:
         7049218 function calls (96 primitive calls) in 8.450 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    8.450    8.450 <string>:1(<module>)
     31/1    0.000    0.000    8.450    8.450 cprofiledemo1.py:14(fib_seq)
7049123/31    8.450    0.000    8.450    0.273 cprofiledemo1.py:5(fib)
        1    0.000    0.000    8.450    8.450 {built-in method builtins.exec}
       31    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       30    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
"""














