#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
二叉搜索树保证具有唯一的值。

输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
输出：32
    10
  5   15
3  7 null  18
找出7 <= x <= 15的所有节点值之和

[address](https://leetcode-cn.com/problems/range-sum-of-bst/solution/er-cha-sou-suo-shu-de-fan-wei-he-by-leetcode/)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def range_sum_bst(root: TreeNode, L: int, R: int) -> int:
    # 深度优先搜索
    # 三种情况:
    # 1. 对于当前节点node, node.val <= L, 则继续搜索右子树
    # 2. node.val >= R, 继续搜索左子树
    # 3. node.val 在 (L, R) 中,则需要搜索它的所有子树

    # 递归
    # 当前节点为null时返回0
    if not root:
        return 0
    # 当前节点X < L时返回右子树之和
    if root.val < L:
        return range_sum_bst(root.right, L, R)
    # 当前节点X > R时返回左子树之和
    if root.val > R:
        return range_sum_bst(root.left, L, R)
    # 当前节点L <= X <= R时则返回当前节点值 + 左右子树之和
    return root.val + range_sum_bst(root.left, L, R) + range_sum_bst(root.right, L, R)

    # 迭代
    # ans = 0
    # stack = [root]
    # while stack:
    #     node = stack.pop()
    #     if node:
    #         if L <= node.val <= R:
    #             ans += node.val
    #         if L < node.val:
    #             stack.append(node.left)
    #         if node.val < R:
    #             stack.append(node.right)
    # return ans
























