#!usr/bin/python
# -*- coding:utf8 -*-
import inspect
# 生成器是可以暂停的函数
def gen_func():
    yield 1
    return "bobby"

if __name__ == "__main__":
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
         pass
    print(inspect.getgeneratorstate(gen))

























