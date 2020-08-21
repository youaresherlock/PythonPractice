#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个整数数组 nums，请你选择数组的两个不同下标 i 和 j，
使 (nums[i]-1)*(nums[j]-1) 取得最大值。

请你计算并返回该式的最大值。
输入：nums = [3,4,5,2]
输出：12
解释：如果选择下标 i=1 和 j=2（下标从 0 开始），则可以获得最大值，(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12

[address](https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array)
"""
from typing import List


def max_product(nums: List[int]) -> int:
    sub_max, max_num = 1, 1
    for num in nums:
        if num > max_num:
            sub_max = max_num
            max_num = num
        elif num > sub_max:
            sub_max = num

    return (max_num - 1) * (sub_max - 1)
























