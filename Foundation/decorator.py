#!usr/bin/python
# -*- coding:utf8 -*-

"""
装饰器接受一个功能，添加一些功能并返回
"""

# 用参数装饰函数
def smart_divide(func):
    # 装饰器中嵌套的inner()函数的参数与其装饰的函数的参数是一样的
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)

    return inner

#相当于 divide = smart_divide(divide)
@smart_divide
def divide(a, b):
    return a/b

# print(divide(2, 5))


# 多个装饰器可以在python中链接 一个函数可以用不同或相同的装饰器多次装饰，只需将装饰器放置在所需函数之上
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

# 相当于printer = start(percent(printer)) 注意链装饰器的顺序
@star
@percent
def printer(msg):
    print(msg)


printer("Hello")



















