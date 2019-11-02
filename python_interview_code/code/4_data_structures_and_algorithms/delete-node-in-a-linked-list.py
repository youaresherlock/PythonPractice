#!usr/bin/python
# -*- coding:utf8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextnode = node.next
        after_next_node = nextnode.next
        node.val = nextnode.val
        node.next = after_next_node

