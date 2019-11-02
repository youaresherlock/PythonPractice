#!usr/bin/python
# -*- coding:utf8 -*-

# 使用栈实现队列
"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
"""

from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, val):
        return self.items.append(val)

    def pop(self):
        return self.items.pop()

    def top(self): # 返回栈顶值
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1= Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s2.empty():
            return self.s2.pop()
        while not self.s1.empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.s2.empty():
            return self.s2.top()
        while not self.s1.empty():
            val = self.s1.pop()
            self.s2.push(val)
        return self.s2.top()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.s1.empty() and self.s2.empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

def test():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.pop())
    print(q.pop())

test()



