#!usr/bin/python
# -*- coding:utf8 -*-

import functools

def user_login_data(f):
    # @functools.wraps(f) 不加上输出的函数名改变，加上不改变
    # 增加@functools.wraps(f), 可以保持当前装饰器去装饰的函数name的值不变
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper

@user_login_data
def num1():
    print("aaa")

@user_login_data
def num2():
    print("bbb")

if __name__ == '__main__':
    # 由此函数使用装饰器时，函数的函数名即__name__已经被装饰器改变
    print(num1.__name__) # wrapper
    print(num2.__name__) # wrapper
