#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你两个整数，n 和 start 。
数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。
请返回 nums 中所有元素按位异或（XOR）后得到的结果。

[address](https://leetcode-cn.com/problems/xor-operation-in-an-array/)
"""
from functools import reduce


def xor_operation(n: int, start: int) -> int:
    return reduce(lambda x, y: x ^ y, [start + 2 * i for i in range(n)])


if __name__ == '__main__':
    n = 3
    start = 0
    print(xor_operation(n, start))
















