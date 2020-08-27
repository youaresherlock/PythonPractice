#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个数字数组 arr 。
如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。
如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。


输入：arr = [3,5,1]
输出：true
解释：对数组重新排序得到 [1,3,5] 或者 [5,3,1] ，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。

[address](https://leetcode-cn.com/problems/can-make-arithmetic-progression-from-sequence)
"""
from typing import List


def can_make_arithmetic_progression(arr: List[int]) -> bool:
    # 1. 按照等差数列的格式检验
    # array = sorted(arr)
    # gep = array[1] - array[0]
    # for i in range(0, len(array) - 1):
    #     if array[i] + gep != array[i+1]:
    #         return False
    #
    # return True
    # 2. 另一种方式检验
    arr.sort()
    for i in range(1, len(arr) - 1):
        if arr[i] * 2 != arr[i - 1] + arr[i + 1]:
            return False

    return True




















