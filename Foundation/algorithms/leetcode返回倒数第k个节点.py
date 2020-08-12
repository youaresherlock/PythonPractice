#!usr/bin/python
# -*- coding:utf8 -*-
"""
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

注意：本题相对原题稍作改动

示例：

输入： 1->2->3->4->5 和 k = 2
输出： 4

[address](https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        """
        思路: 先确定快慢指针的位置，慢指针比快指针落后k位。当快指针走完全程,慢指针就是
        所需要的的节点
        """
        a = head
        b = head
        for i in range(k):
            b = b.next
        while b:
            a = a.next
            b = b.next

        return a.val

















