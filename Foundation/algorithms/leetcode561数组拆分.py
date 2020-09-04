#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1),
(a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。


输入: [1,4,3,2]
输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).

提示:
n 是正整数,范围在 [1, 10000].
数组中的元素范围在 [-10000, 10000].

[address](https://leetcode-cn.com/problems/array-partition-i)
"""
from typing import List


def array_pair_sum(nums: List[int]) -> int:
    """
    可以对给定数组的元素进行排序,并直接按排序顺序形成元素的配对.这将导致
    元素的配对,他们之间的差异最小,从而导致所需总和的最大化
    """
    nums.sort()
    res = 0
    # for i in range(0, len(nums), 2):
    #     res += nums[i]
    for i in range(len(nums)):
        if i % 2 == 0:
            res += nums[i]

    return res










































