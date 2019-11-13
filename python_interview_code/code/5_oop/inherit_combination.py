#!usr/bin/python
# -*- coding:utf8 -*-

# 代理模式
from collections import deque

class Stack(object): # 使用组合的例子
    def __init__(self):
        self._deque = deque() # has a deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def empty(self):
        return len(self._deque) == 0

    def __iter__(self):
        res = []
        for i in self._deque:
            res.append(i)
        for i in reversed(res):
            yield i

s = Stack()
s.push(1)
s.push(2)
for i in s :
    print(i)
