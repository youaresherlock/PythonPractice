#!usr/bin/python
# -*- coding:utf8 -*-
"""
实现一个MyQueue类，该类用两个栈来实现一个队列。

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

和此题一样: [address](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof)
[address](https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci)
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1, self.stack2 = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1]
        if self.stack1:
            return self.stack1[0]

        return -1

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1 + self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

































