#!usr/bin/python
# -*- coding:utf8 -*-
"""
学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。

请你返回能让所有学生以 非递减 高度排列的最小必要移动人数。

注意，当一组学生被选中时，他们之间可以以任何可能的方式重新排序，而未被选中的学生应该保持不动。


输入：heights = [1,1,4,2,1,3]
输出：3
解释：
当前数组：[1,1,4,2,1,3]
目标数组：[1,1,1,2,3,4]

[address](https://leetcode-cn.com/problems/height-checker)
"""
from typing import List


def height_checker(heights: List[int]) -> int:
    sorted_heights = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if sorted_heights[i] != heights[i]:
            count += 1

    return count










