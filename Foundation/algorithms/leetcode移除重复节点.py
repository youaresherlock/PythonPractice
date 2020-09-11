#!usr/bin/python
# -*- coding:utf8 -*-
"""
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

输入：[1, 2, 3, 3, 2, 1]
输出：[1, 2, 3]

[address](https://leetcode-cn.com/problems/remove-duplicate-node-lcci/)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        val_set = set()
        prev = ListNode(-1)
        prev.next = head

        while prev.next:
            if prev.next.val in val_set:
                prev.next = prev.next.next
            else:
                val_set.add(prev.next.val)
                prev = prev.next

        return head











