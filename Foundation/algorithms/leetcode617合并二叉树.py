#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

[address](https://leetcode-cn.com/problems/merge-two-binary-trees)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def merge_trees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not all([t1, t2]):
        return t1 or t2

    t1.val += t2.val
    t1.left = merge_trees(t1.left, t2.left)
    t1.right = merge_trees(t1.right, t2.right)

    return t1


















