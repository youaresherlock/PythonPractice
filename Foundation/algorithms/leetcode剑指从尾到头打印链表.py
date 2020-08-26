#!usr/bin/python
# -*- coding:utf8 -*-
"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

输入：head = [1,3,2]
输出：[2,3,1]

[address](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_print(head: ListNode) -> List[int]:
    # 1. 辅助栈
    # result = []
    # while head:
    #     result.insert(0, head.val)
    #     head = head.next
    #
    # return result

    # 2. 递归
    if not head:
        return []

    return reverse_print(head.next) + [head.val]




















