#!usr/bin/python
# -*- coding:utf8 -*-
"""
https://leetcode-cn.com/problems/number-of-good-pairs/

给你一个整数数组 nums 。
如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，
就可以认为这是一组 好数对 。返回好数对的数目。

输入：nums = [1,2,3,1,1,3]
输出：4
解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始

提示:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""


def pair_count(array):
    bucket = [0] * 101
    for i in array:
        bucket[i] += 1
    result = 0
    for i in bucket:
        if i > 0:
            result += i * (i - 1) // 2

    return result


if __name__ == '__main__':
    # nums = [1, 2, 3, 1, 1, 3]
    nums = [1, 1, 1, 1]
    print(pair_count(nums))















