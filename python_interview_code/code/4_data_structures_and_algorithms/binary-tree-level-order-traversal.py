#!usr/bin/python
# -*- coding:utf8 -*-

# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root: # NOTE: 注意root可能为空
            return []
        res = []
        cur_nodes = [root]
        next_nodes = []
        res.append([i.val for i in cur_nodes])
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            if next_nodes:
                res.append(
                    [i.val for i in next_nodes]
                )

            cur_nodes = next_nodes
            next_nodes = []
        return res




















