#!usr/bin/python
# -*- coding:utf8 -*-
"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍
然是递增排序的。

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

[address](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    # 开辟新的节点
    # root = ListNode(0)
    # cur = root
    # while l1 and l2:
    #     cur.next = ListNode(0)
    #     if l1.val <= l2.val:
    #         cur.next.val = l1.val
    #         l1 = l1.next
    #     else:
    #         cur.next.val = l2.val
    #         l2 = l2.next
    #     cur = cur.next
    #
    # last = l1 or l2
    # while last:
    #     cur.next = ListNode(0)
    #     cur.next.val = last.val
    #     cur, last = cur.next, last.next
    #
    # return root.next

    # 不开辟新的节点,利用原有节点
    cur = dum = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return dum.next


if __name__ == '__main__':
    l1 = ListNode(0)
    l2 = ListNode(0)
    l1.val = -9
    l1.next = ListNode(0)
    l1.next.val = 3
    l2.val = 5
    l2.next = ListNode(0)
    l2.next.val = 7
    result = merge_two_lists(l1, l2)
    while result:
        print(result.val)
        result = result.next
