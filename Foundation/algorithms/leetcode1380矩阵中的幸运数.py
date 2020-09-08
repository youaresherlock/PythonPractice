#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返
回矩阵中的所有幸运数。
幸运数是指矩阵中满足同时下列两个条件的元素：
在同一行的所有元素中最小
在同一列的所有元素中最大

输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
输出：[15]
解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

提示: 元素不唯一

[address](https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix)
"""
from typing import List


def lucky_numbers(matrix: List[List[int]]) -> List[int]:
    # 1. 元素不唯一的情况下也可以
    # m, n = len(matrix), len(matrix[0])
    # results = []
    # for i in range(m):
    #     min_index = 0
    #     for j in range(1, n):
    #         if matrix[i][min_index] > matrix[i][j]:
    #             min_index = j
    #
    #     max_index = 0
    #     for k in range(1, m):
    #         if matrix[max_index][min_index] < matrix[k][min_index]:
    #             max_index = k
    #
    #     if max_index == i:
    #         results.append(matrix[i][min_index])
    #
    # return results

    # 2. 如果元素唯一 求出含有最小元素和最大元素的集合交集
    mins = {min(rows) for rows in matrix}
    print(list(zip(*matrix)))
    """
    >>>a = [1,2,3]
    >>> b = [4,5,6]
    >>> zipped = zip(a,b)     # 打包为元组的列表
    [(1, 4), (2, 5), (3, 6)]
    >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
    [(1, 2, 3), (4, 5, 6)]
    """
    maxes = {max(columns) for columns in zip(*matrix)}

    return list(mins & maxes)


if __name__ == '__main__':
    matrix = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
    print(lucky_numbers(matrix))













