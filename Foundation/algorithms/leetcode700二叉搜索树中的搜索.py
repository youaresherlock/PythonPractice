#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点
值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存
在，则返回 NULL。


[address](https://leetcode-cn.com/problems/search-in-a-binary-search-tree/)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def search_bst(root: TreeNode, val: int) -> TreeNode:
    """
    二叉搜索树: 是一颗二叉树,每个节点大于左子树上任意一个节点,
    小于右子树上任意一个节点的值
    """
    # 1. 递归
    # 节点为空或者节点的值等于val返回此节点
    # val > root.val, 对当前节点的右子树查找,否则左子树查找
    # if not root:
    #     return root
    #
    # if root.val == val:
    #     return root
    #
    # return search_bst(root.left, val) if val < root.val \
    #     else search_bst(root.right, val)

    # 2. 迭代
    while root is not None and root.val != val:
        root = root.left if val < root.val else root.right

    return root












