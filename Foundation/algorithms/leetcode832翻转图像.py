#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 
的结果是 [0, 1, 1]。
反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。
例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。

输入: [[1,1,0],[1,0,1],[0,0,0]]
输出: [[1,0,0],[0,1,0],[1,1,1]]
解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
     然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]

[address](https://leetcode-cn.com/problems/flipping-an-image)
"""
from typing import List


def flip_and_invert_image(A: List[List[int]]) -> List[List[int]]:
    for row in A:
        for i in range((len(row) + 1) // 2):
            """
            In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
            helps us find the i-th value of the row, counting from the right.
            """
            row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
    return A



















