#!usr/bin/python
# -*- coding:utf8 -*-
"""
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

[address](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof)
"""


def hamming_weight(self, n: int) -> int:
    """
    此题与leetcode461题目类似,可以转换成n与0之间的汉明距离
    n^0异或还是n
    """
    # return bin(n).count('1')
    xor = n
    distance = 0
    while xor:
        distance += 1
        xor = xor & (xor - 1)

    return distance
