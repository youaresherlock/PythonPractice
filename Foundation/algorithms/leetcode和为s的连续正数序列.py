#!usr/bin/python
# -*- coding:utf8 -*-
"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序
列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。


输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

[address](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof)
"""
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 利用等差数列求和公式
        if target <= 2: # 最小的target应该是3 -> [1, 2]
            return []
        res = []
        for n in range(2, target+1): # n -> 首尾间隔
            temp = target - n*(n-1)//2
            if temp <= 0:
                break
            if not temp % n: # 首项必为正整数
                start = temp // n
                res.append([start + i for i in range(n)])
        return res[::-1]








