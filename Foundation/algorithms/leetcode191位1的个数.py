#!usr/bin/python
# -*- coding:utf8 -*-
"""
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’
的个数（也被称为汉明重量）。
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')
        xor = n
        distance = 0
        while xor:
            distance += 1
            xor = xor & (xor - 1)

        return distance

