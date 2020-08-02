#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一个非递减整数数组, 和一个target,要求你找到数组中最小的一个数x, 可以满足
x*x > target,一旦不存在,则返回-1
"""


def solve(arr, target):
    begin, end = 0, len(arr) - 1
    ret = -1
    while begin <= end:
        m = (begin + end) // 2
        if arr[m] * arr[m] > target:
            ret = m
            end = m - 1
        else:
            begin = m + 1

    return ret if ret == -1 else arr[ret]


print(solve([1, 2, 3, 4, 5, 6], 8))
print(solve([1, 2, 3, 4, 5, 6], 9))
print(solve([1, 2, 3, 4, 5, 6], 0))
print(solve([1, 2, 3, 4, 5, 6], 40))













