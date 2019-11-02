#!usr/bin/python
# -*- coding:utf8 -*-

"""
https://leetcode.com/problems/merge-k-sorted-lists/submissions/
合并k个有序链表
方法1: 两两合并
方法2:
    读取所有链表值
    构造一个最小堆heapq实现
    根据最小堆构造一个链表
"""
from heapq import heapify, heappop
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 可能出现Lists是[[]]的情况，这是True
        # if not lists:
        #     return None
        # 读取所有节点值
        h = [] # 最小堆
        for node in lists:
            while node:
                h.append(node.val)
                node = node.next
        # 构造一个最小堆
        if not h:
            return None
        heapify(h) # 转换成最小堆

        # 构造链表
        root = ListNode(heappop(h))
        curnode = root
        while h:
            nextnode = ListNode(heappop(h))
            curnode.next = nextnode
            curnode = nextnode

        return root