#!usr/bin/python
# -*- coding:utf8 -*-

# 先序遍历
class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right

class BinTree(object):
    def __init__(self, root=None):
        self.root = root

    def preorder_trav(self, subtree):
        """ 先(根)序遍历 """
        if subtree is not None:
            print(subtree.data) # 递归函数里先处理根
            self.preorder_trav(subtree.left) # 递归处理左子树
            self.preorder_trav(subtree.right) # 递归处理右子树

    def inorder_trav(self, subtree):
        if subtree is not None:
            self.preorder_trav(subtree.left)
            print(subtree.data)
            self.preorder_trav(subtree.right)

    def postorder_trav(self, subtree):
        if subtree is not None:
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)
            print(subtree.data)




























