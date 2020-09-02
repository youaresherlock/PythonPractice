#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一个 N 叉树，返回其节点值的前序遍历。

[address](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/)
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def pre_order(root: Node) -> List[int]:
    # 迭代法
    """
    使用一个栈来帮助我们得到前序遍历,需要保证栈顶的节点是我们当前遍历
    到的节点.我们首先入栈根节点,根节点是前序遍历中的第一个节点.随后每次
    我们从栈顶取出一个节点u,它是我们当前遍历到的节点,并把u的所有子节点逆序
    推入栈中.(例如u的子节点从左到右是v1,v2,v3,那么推入栈的顺序应当为v3,v2,v1,
    这样就保证了下一个遍历到的节点(即u的第一个子节点v1)出现在栈顶的位置.
    """
    # if root is None:
    #     return []
    #
    # stack, output = [root,], []
    # while stack:
    #     root = stack.pop()
    #     output.append(root.val)
    #     stack.extend(root.children[::-1])
    #
    # return output

    # N叉树简洁递归
    # if not root:
    #     return []
    # res = [root.val]
    # for node in root.children:
    #     res.extend(pre_order(node))
    #
    # return res

    # N叉树通用递归模板
    res = []

    def helper(root):
        if not root:
            return
        res.append(root.val)
        for child in root.children:
            helper(child)

    helper(root)

    return res













