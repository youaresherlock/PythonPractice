#!usr/bin/python
# -*- coding:utf8 -*-

from heapq import heappush, heappop

def heapsorte_use_heapq(iterable):
    items = []
    for value in iterable:
        heappush(items, value)
    return [heappop(items) for i in range(len(items))]