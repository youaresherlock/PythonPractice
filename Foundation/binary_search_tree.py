#!usr/bin/python
# -*- coding:utf8 -*-

"""
二叉查找树
二叉排序树或者是一颗空树，或者是具有下列性质的二叉树:
1. 若左子树不为空，则左子树上所有节点的值均小于它的根节点的值
2. 若右子树不为空，则右子树上所有节点的值均大于或等于它的根节点的值
3. 左、右子树也分别为二叉排序树
4. 没有键值相等的节点
"""
class node(object):
    '''
    bst的节点
    '''
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None

class bst(object):
    '''
    BST
    '''
    def __init__(self):
        self.root = None

    def inorder_tree_walk(self, p):
        '''
        中序遍历的结果必然是从小到大的排序
        :param p:
        :return:
        '''
        if p != None:
            self.inorder_tree_walk(p.left)
            print(p.val)
            self.inorder_tree_walk(p.right)

    def preorder_tree_walk(self, p):
        if p != None:
            print(p.val)
            self.preorder_tree_walk(p.left)
            self.preorder_tree_walk(p.right)

    def postorder_tree_walk(self, p):
        if p != None:
            self.postorder_tree_walk(p.left)
            self.postorder_tree_walk(p.right)

    def search(self, root, val):
        '''
        给定一个关键字，查找包含关键字的节点
        :param val:
        :return:
        '''
        p = root
        if p == None:
            return -1
        elif p.val == val:
            return p
        elif p.val > val:
            self.search(p.left, val)
        else:
            self.search(p.right, val)

    def find_max(self):
        '''
        从根节点沿着右子树的方向一直找下去，直到叶子节点，则
        必然找到最大值
        :return:
        '''
        p = self.root
        while p.right != None:
            p = p.right
        return p

    def find_min(self):
        p = self.root
        while p.left != None:
            p = p.left
        return p

    def find_preprocessor(self, val):
        '''
        查找给定值的节点的前驱
        '''
        n = self.search(self.root, val)
        if n == None:
            return None
        # 如果存在左子树，就查找左子树里面最大值
        if n.left != None:
            return self.find_max(n.left)
        else:
            # 如果没有左子树，就往上找第一个有右子树且左子树里没有x节点的祖先
            p = n.parent
            while p.next != None and p.right != n:
                n = p
                p = p.parent
            return p

    def find_successor(self, val):
        '''
        查找给定值的节点的前驱
        '''
        n = self.search(self.root, val)

        if n == None:
            return None
        # 如果存在有，就查找右子树里面最小值
        if n.right != None:
            return self.find_min(n.right)
        else:
            # 如果没有右子树，就往上找第一个有右子树且左子树里没有x节点的祖先
            p = n.parent
            while p.next != None and p.left != n:
                n = p
                p = p.parent
            return p

    def insert(self, val):
        '''
        insert
        '''
        y = None
        x = self.root
        while x != None:
            y = x
            if x.val > val:
                x = x.left
            else:
                x = x.right
        n = node(val)
        n.parent = y
        if y == None:
            self.root = n
        else:
            if val < y.val:
                y.left = n
            else:
                y.right = n

    def delete(self, val):
        '''
        删除
        '''
        z = self.search(self.root, val)
        # 没找到
        if z == None:
            return None

        if z.left == None and z.right == None:
            # 如果是个叶子节点
            if z.parent.left == z:
                z.parent.left = None
            else:
                z.parent.right = None

        elif z.left != None and z.right != None:
            # 如果有两个后继
            # 1.先删掉他的后驱节点
            y = self.find_successor(val)
            # print y.val
            self.delete(y.val)
            # 2.然后将后驱节点的值替换z节点
            z.val = y.val

        # 如果只有一个后继节点，就让父节点成为该后继节点的父节点
        elif z.left != None:
            if z.parent.left == z:
                z.parent.left = z.left
            else:
                z.parent.right = z.left
        else:
            if z.parent.left == z:
                z.parent.left = z.right
            else:
                z.parent.right = z.right




































































