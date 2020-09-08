#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定两个数组，编写一个函数来计算它们的交集。

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

[address](https://leetcode-cn.com/problems/intersection-of-two-arrays/)
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return list(set(nums1) & set(nums2))
        results = set()
        for number in nums1:
            if number in nums2:
                results.add(number)

        return list(results)