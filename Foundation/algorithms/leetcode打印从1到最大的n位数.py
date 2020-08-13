#!usr/bin/python
# -*- coding:utf8 -*-
"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3
一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]

[address](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof)
"""
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        # return [i for i in range(1, 10 ** n)]
        return list(range(1, 10 ** n))
