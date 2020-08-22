#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。

请你统计并返回 grid 中 负数 的数目。

输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。

[address](https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix)
"""
from typing import List


def count_negatives(grid: List[List[int]]) -> int:
    count = 0
    length = len(grid[0])
    for each in grid:
        for i in range(length):
            if each[i] < 0:
                count += length - i
                break

    return count


if __name__ == '__main__':
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(count_negatives(grid))

















