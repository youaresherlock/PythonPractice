#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
以数组形式返回答案。

输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释：
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。
对于 nums[3]=2 存在一个比它小的数字：（1）。
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。

[address](https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number)
"""
from typing import List


def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    num = sorted(nums)
    ans = []
    for n in nums:
        ans.append(num.index(n))

    return ans


if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    print(smaller_numbers_than_current(nums))




















