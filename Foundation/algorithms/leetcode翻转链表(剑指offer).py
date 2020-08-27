#!usr/bin/python
# -*- coding:utf8 -*-
"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

[address](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head: ListNode) -> ListNode:
    # 1. 双指针
    if not head:
        return head
    pre = None
    cur = head
    while cur:
        cur.next, pre, cur = pre, cur, cur.next

    return pre























