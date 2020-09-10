#!usr/bin/python
# -*- coding:utf8 -*-
"""
反转一个单链表。
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

[address](https://leetcode-cn.com/problems/reverse-linked-list/)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head: ListNode) -> ListNode:
    # 1. 双指针
    # pre, cur = None, head
    # while cur:
    #     cur.next, pre, cur = pre, cur, cur.next
    #
    # return pre

    # 2. 递归
    # def helper(pre, cur):
    #     if cur is None:
    #         return pre
    # 
    #     cur_next = cur.next
    #     cur.next = pre
    #     return helper(cur, cur_next)
    # 
    # return helper(None, head)

    # new_head始终指向最后一个节点,即新的头结点
    if not head or not head.next:
        return head
    new_head = reverse_list(head.next)
    # 从头结点开始将引用反转
    head.next.next = head
    # 为了让头结点指向None,这里的代码实际上只发挥一次作用
    head.next = None

    return new_head










