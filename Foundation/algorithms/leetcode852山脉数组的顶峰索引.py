#!usr/bin/python
# -*- coding:utf8 -*-
"""
我们把符合下列属性的数组 A 称作山脉：
A.length >= 3
存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] >
A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] <
A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。


输入：[0,2,1,0]
输出：1

[address](https://leetcode-cn.com/problems/peak-index-in-a-mountain-array)
"""
from typing import List


def peak_index_in_mountain_array(arr: List[int]) -> int:
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] > arr[m - 1]:
            l = m
        else:
            r = m - 1

    return l


if __name__ == '__main__':
    arr = [0, 2, 4, 7, 3, 2, 0]
    print(peak_index_in_mountain_array(arr))




















