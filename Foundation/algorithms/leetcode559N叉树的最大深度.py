#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

[address](https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/)

对于二叉树来说,是这个题[address](https://blog.csdn.net/qq_32252957/article/details/108268370)
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # 1. 递归 深度优先搜索
        # 每个节点遍历一次, 时间复杂度为O(N)
        # if root is None:
        #     return 0
        # elif not root.children:
        #     return 1
        # else:
        #     height = [self.maxDepth(c) for c in root.children]
        #
        #     return max(height) + 1

        # 2. 迭代
        # 使用深度优先搜索策略访问每个节点,同时更新每次访问时的最大深度
        # 可以从包含根节点的、对应深度为1的栈开始. 然后继续迭代,从栈中
        # 弹出当前节点并将子节点压入栈中,每次都更新对应深度
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                for c in root.children:
                    stack.append((current_depth + 1, c))

        return depth














