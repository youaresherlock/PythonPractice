#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次
。找出那个只出现了一次的元素。

输入: [2,2,1]
输出: 1

[address](https://leetcode-cn.com/problems/single-number)
"""
from typing import List


def single_number(nums: List[int]) -> int:
    # 1. 位运算 利用相同数字的异或为0,0和任意数异或为任意数
    # res = nums[0]
    # for i in range(1, len(nums)):
    #     res ^= nums[i]
    #
    # return res

    # 2. 数学公式
    return sum(set(nums)) * 2 - sum(nums)


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    print(single_number(nums))














