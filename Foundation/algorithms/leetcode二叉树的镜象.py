#!usr/bin/python
# -*- coding:utf8 -*-
"""
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

[address](https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mirror_tree(root: TreeNode) -> TreeNode:
    """
    根据二叉树镜像的定义，考虑递归遍历（dfs）二叉树，交换每个节点的左 / 右子节点，
    即可生成二叉树的镜像。
    """
    # 递归法1.
    # if not root:
    #     return
    # root.left, root.right = root.right, root.left
    # mirror_tree(root.left)
    # mirror_tree(root.right)
    #
    # return root

    # 递归法2.
    # if not root:
    #     return
    # tmp = root.left
    # root.left = mirror_tree(root.right)
    # root.right = mirror_tree(tmp)
    #
    # return root

    """
    利用栈（或队列）遍历树的所有节点 nodenode ，并交换每个 nodenode 的左 / 右子节点。
    """
    # 辅助栈(或队列)
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        node.left, node.right = node.right, node.left

    return root













