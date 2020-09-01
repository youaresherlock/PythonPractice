#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一棵二叉搜索树，请找出其中第k大的节点。

[address](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        """
          二叉搜索树的中序遍历倒序为递减序列
          求二叉搜索树第k大的节点此树的中序遍历倒序的第k个节点
        """
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res



















