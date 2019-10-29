#!usr/bin/python
# -*- coding:utf8 -*-

"""
用堆来完成topk问题，从海量数字中寻找最大的k个, 有限内存
"""

import heapq

class TopK:
    """获取大量元素 topk大个元素，固定内存
    思路:
    1. 先放入元素中前k个建立一个最小堆
    2. 迭代剩余元素:
        如果当前元素小于对顶元素，跳过该元素(肯定不是前k大)
        否则替换堆顶元素为当前元素,并重新调整
    """
    def __init__(self, iterable, k):
        self.minheap = []
        self.capacity = k
        self.iterable = iterable

    def push(self, val):
        if len(self.minheap) >= self.capacity:
            min_val = self.minheap[0]
            if val < min_val: # 当然你可以直接if val > min_val操作，这里我只是显示指出跳过这个元素
                pass
            else:
                heapq.heapreplace(self.minheap, val) # 返回并且pop堆顶最小值，推入新的val值并调整堆
        else:
            heapq.heappush(self.minheap, val) # 前面k个元素直接放入minheap

    def get_topk(self):
        for val in self.iterable:
            self.push(val)
        return self.minheap

def test():
    import random
    l = list(range(1000)) # 这里可以是一个可迭代对象，节省内存
    random.shuffle(l)
    _ = TopK(l, 10)
    print(_.get_topk())


























