#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是
树的根，并且每个结点没有左子结点，只有一个右子结点。


[address](https://leetcode-cn.com/problems/increasing-order-search-tree/)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def increasing_bst(self, root: TreeNode) -> TreeNode:
        # 1. 中序遍历+构造新的树
        # 我们在树上进行中序遍历,就可以从小到大得到树上的节点.我们把
        # 这些节点的对应的值存放在数组中,他们已经有序.接着构造树即可
        # def inorder(node):
        #     if node:
        #         yield from inorder(node.left)
        #         yield node.val
        #         yield from inorder(node.right)
        #
        # ans = cur = TreeNode(None)
        # for v in inorder(root):
        #     cur.right = TreeNode(v)
        #     cur = cur.right
        #
        # return ans.right

        # 2. 中序遍历+更改树的连接方式
        # 进行中序遍历,将树中的节点之间重新连接而不
        # 使用额外的空间
        # 当我们遍历到一个节点时,把它的左孩子设为空
        # 并将其本身作为上一个遍历到的节点的右孩子
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        self.cur = ans = TreeNode(None)
        inorder(root)

        return ans.right
















