#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一个 N 叉树，返回其节点值的后序遍历。

[address](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def post_order(root: Node) -> List[int]:
    # 1. 递归
    # result = []
    #
    # def post_helper(root):
    #     if not root:
    #         return None
    #     children = root.children
    #     for child in children:
    #         post_helper(child)
    #     result.append(root.val)
    #
    # post_helper(root)
    #
    # return result

    # 2. 迭代
    if root is None:
        return []

    stack, output = [root, ], []
    while stack:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
        for c in root.children:
            stack.append(c)

    return output[::-1]













