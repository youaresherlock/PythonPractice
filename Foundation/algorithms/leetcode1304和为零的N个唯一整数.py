#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个整数 n，请你返回 任意 一个由 n 个 各不相同 的整数组成的数组，
并且这 n 个数相加和为 0 。

输入：n = 5
输出：[-7,-1,1,3,4]
解释：这些数组也是正确的 [-5,-1,1,2,3]，[-3,-1,2,-2,4]。

[address](https://leetcode-cn.com/problems/find-n-unique-integers-sum-up-to-zero/)
"""
from typing import List


def sum_zero(n: int) -> List[int]:
    ans = [x for x in range(1, n)]
    ans.append(-sum(ans))

    return ans


if __name__ == '__main__':
    n = 5
    print(sum_zero(n))
















