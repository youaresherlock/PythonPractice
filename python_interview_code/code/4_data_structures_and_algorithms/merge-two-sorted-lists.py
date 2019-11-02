#!usr/bin/python
# -*- coding:utf8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(None)
        cur = root
        while l1 and l2:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l1.val)
                l2 = l2.next
            cur.next = node
            cur = node
        # l1或者12可能还有剩余元素
        # if l1 is None:
        #     cur.next = l2
        # else:
        #     cur.next = l1
        cur.next = l1 or l2
        return root.next
