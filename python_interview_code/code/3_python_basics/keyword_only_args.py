#!usr/bin/python
# -*- coding:utf8 -*-

# Feature: Keyword only arguments

# 限定关键字参数需要指定参数名传入
def add(a, b, *, c):
    return a + b + c

print(add(1, 2, c=3))