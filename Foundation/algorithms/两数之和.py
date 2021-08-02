#!/usr/bin/python
# -*- coding:utf-8 -*-
from typing import List

# 方法1 暴力破解
# def two_sum(nums: List[int], target: int) -> List[int]:
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


"""
上面的方法的时间复杂度较高的原因是寻找target-x的时间
复杂度过高，因此我们可以使用哈希表
"""


def two_sum(nums: List[int], target: int) -> List[int]:
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
