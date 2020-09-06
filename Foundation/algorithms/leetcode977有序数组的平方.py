#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数
组，要求也按非递减顺序排序。

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

[address](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)
"""
from typing import List


def sorted_squares(A: List[int]) -> List[int]:
    # return list(map(lambda x: x*x, sorted(A, key=lambda x: abs(x))))
    return sorted(x ** 2 for x in A)


if __name__ == '__main__':
    A = [-7, -3, 2, 3, 11]
    print(sorted_squares(A))














