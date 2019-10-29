#!usr/bin/python
# -*- coding:utf8 -*-

# 实现队列。 使用deque
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def append(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.popleft()

    def empty(self):
        return len(self.items) == 0

def test_queue():
    q = Queue()
    q.append(0)
    q.append(1)
    q.append(2)
    print(q.pop())
    print(q.pop())
    print(q.pop())

test_queue()
