#!usr/bin/python
# -*- coding:utf8 -*-


"""
LRU
Least Recent used 最近最少使用算法，主要用于缓存淘汰.
主要目的就是把最近最少使用的数据移除内存，以加载其他数据
原理:

有新数据(意味着数据之前没有被缓存过)时,加入到列表头
缓存达到最大容量时, 需要淘汰数据多出来的数据,此时淘汰列表尾部的数据
当缓存中有数据被命中, 则将数据移动到列表头部(相当于新加入缓存)

从前面的文章中我们可以知道，缓存简化下来就两个功能，一个是往里装数据（缓存数据），
一个是往外吐数据（命中缓存），所以我们的缓存对外只需要put和get两个接口就可以了。
按照前面的示意图，缓存内部我们只需要有一个列表（list）就可以实现LRU逻辑，不过用列表虽然能实现逻辑，
但是在判断是否命中缓存时，速度可能非常慢（列表需要遍历才能知道数据有没有在里面）。在Python中，
我们可以用基于hash的结构，比如字典（dict）或集合（set），来快速判断数据是否存在，
解决列表实现的性能问题。但是字典(python3.6后有序)和集合又是没有顺序的，如果能有一种既能排序，
又是基于hash存储的数据结构，就好了。

在Python的collections包中，已经内置了这种实用的结构OrderedDict，OrderedDict是dict的子类，
但是存储在内部的元素是有序的（列表的特点）。
"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = OrderedDict()

    def get(self, key):
        # 要找的数据不再缓存中返回-1
        if key not in self.queue:
            return -1
        # 将命中缓存的数据移除
        value = self.queue.pop(key)
        # 假定字典最后一个元素是头
        # 将命中缓存的数据重新添加到头部
        self.queue[key] = value
        return self.queue[key]

    def put(self, key, value):
        # 如果已经在缓存中, 则先移除老的数据
        if key in self.queue:
            self.queue.pop(key)
        # 如果不在缓存中并且达到最大容量, 则把最后的数据淘汰
        elif len(self.queue.items()) == self.capacity:
            # 将字典开始的元素淘汰
            self.queue.popitem(last=False)
        # 将新数据添加到头部
        self.queue[key] = value




































































