#!usr/bin/python
# -*- coding:utf8 -*-
"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

[address](https://leetcode-cn.com/problems/hamming-distance)
"""


def hamming_distance(x: int, y: int) -> int:
    # 计算x和y之间的汉明距离,可以先计算x XOR y, 然后统计结果中等于1的位数
    # 1. 内置位计数功能
    # return bin(x ^ y).count('1')
    # 2. 自己实现计数功能
    # xor = x ^ y
    # distance = 0
    # while xor:
    #     if xor & 1:
    #         distance += 1
    #     xor = xor >> 1
    #
    # return distance
    # 3. 布莱恩.克尼根计数算法 当number和number-1进行与运算,则
    # 原数字number的最右边等于1的比特会被移除
    xor = x ^ y
    distance = 0
    while xor:
        distance += 1
        xor = xor & (xor - 1)

    return distance


if __name__ == '__main__':
    x, y = 1, 4
    print(hamming_distance(x, y))
















