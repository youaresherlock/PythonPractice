#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个 n 行 m 列的矩阵，最开始的时候，每个单元格中的值都是 0。

另有一个索引数组 indices，indices[i] = [ri, ci] 中的 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。

你需要将每对 [ri, ci] 指定的行和列上的所有单元格的值加 1。

请你在执行完所有 indices 指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。


输入：n = 2, m = 3, indices = [[0,1],[1,1]]
输出：6
解释：最开始的矩阵是 [[0,0,0],[0,0,0]]。
第一次增量操作后得到 [[1,2,1],[0,1,0]]。
最后的矩阵是 [[1,3,1],[1,3,1]]，里面有 6 个奇数。

[address](https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix)
"""
from typing import List


def odd_cells(n: int, m: int, indices: List[List[int]]) -> int:
    # 1. 暴力法
    # res = 0
    # arr = [[0] * m for _ in range(n)]
    # for row, col in indices:
    #     for j in range(m):
    #         arr[row][j] += 1
    #     for i in range(n):
    #         arr[i][col] += 1
    #
    # for row in arr:
    #     for i in row:
    #         if i % 2 == 1:
    #             res += 1
    #
    # return res

    # 2. 改进
    rows = [0] * n
    cols = [0] * m
    for x, y in indices:
        rows[x] += 1
        cols[y] += 1

    odd_rows = sum(x % 2 == 1 for x in rows)
    odd_cols = sum(y % 2 == 1 for y in cols)
    return odd_rows * (m - odd_cols) + (n - odd_rows) * odd_cols


if __name__ == '__main__':
    n = 2
    m = 3
    indices = [[0, 1], [1, 1]]
    print(odd_cells(n, m, indices))

















