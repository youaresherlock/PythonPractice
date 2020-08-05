#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个数组 nums 。数组「动态和」的计算公式为：
runningSum[i] = sum(nums[0]…nums[i]) 。
请返回 nums 的动态和。

输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
"""
from typing import List


def yield_num(nums):
    sum = 0
    for i in range(len(nums)):
        yield sum + nums[i]
        sum += nums[i]


def running_sum(nums: List[int]) -> List[int]:
    return [i for i in yield_num(nums)]
    # return [sum(nums[:index + 1]) for index, _ in enumerate(nums)]


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(running_sum(nums))
























