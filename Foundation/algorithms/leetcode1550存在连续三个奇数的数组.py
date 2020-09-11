#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都
是奇数的情况：如果存在，请返回 true ；否则，返回 false 。

输入：arr = [2,6,4,1]
输出：false
解释：不存在连续三个元素都是奇数的情况。

[address](https://leetcode-cn.com/problems/three-consecutive-odds/)
"""
from typing import List


def three_consecutive_odds(arr: List[int]) -> bool:
    # 1. 计数法
    # count = 0
    # for number in arr:
    #     if number % 2 == 1:
    #         count += 1
    #         if count == 3:
    #             return True
    #     else:
    #         count = 0
    #
    # return False

    # 2. 枚举
    n = len(arr)
    return n >= 3 and any(arr[i] & 1 and arr[i + 1] & 1 and
                          arr[i + 2] & 1 for i in range(n - 2))


if __name__ == '__main__':
    arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    print(three_consecutive_odds(arr))