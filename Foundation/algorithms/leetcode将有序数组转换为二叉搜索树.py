#!usr/bin/python
# -*- coding:utf8 -*-
"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的
绝对值不超过 1。

给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

[address](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree)
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sorted_array_to_bst(nums: List[int]) -> TreeNode:
    def helper(left, right):
        if left > right:
            return None

        # 总是选择中间位置左边的数字作为根节点
        mid = (left + right) // 2

        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)

        return root

    return helper(0, len(nums) - 1)












