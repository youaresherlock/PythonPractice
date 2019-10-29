#!usr/bin/python
# -*- coding:utf8 -*-

# 借助内置的数据结构实现一个栈
from collections import deque

class Stack(object):
    def __init__(self):
        self.deque = deque()

    def push(self, value):
        self.deque.append(value)

    def pop(self):
        return self.deque.pop()