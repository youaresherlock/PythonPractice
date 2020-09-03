#!usr/bin/python
# -*- coding:utf8 -*-
"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail
和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功
能。(若队列中没有元素，deleteHead 操作返回 -1 )

[address](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof)
"""


class CQueue:
    """
    stack1负责插入元素
    stack2弹出元素,如果stack2为空,stack1也为空则返回-1
    如果stack2为空,stack1不为空,则将stack1弹出到stack2中,
    最后从stack2弹出元素
    """

    def __init__(self):
        self.stack1, self.stack2 = [], []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        # while self.stack1:
        #     self.stack2.append(self.stack1.pop())
        self.stack2.extend(self.stack1[::-1])
        self.stack1 = []
        return self.stack2.pop()




















# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()