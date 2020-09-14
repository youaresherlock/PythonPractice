#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false

输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。

[address](https://leetcode-cn.com/problems/unique-number-of-occurrences)
"""
from typing import List
import collections


def unique_occurrences(arr: List[int]) -> bool:
    # 1.
    # mapping = collections.defaultdict(int)
    # for number in arr:
    #     mapping[number] += 1
    #
    # return len(mapping) == len(set(mapping.values()))

    # 2.
    mapping = collections.Counter(arr)
    print(mapping)
    return len(mapping) == len(set(mapping.values()))


if __name__ == '__main__':
    arr = [1, 2, 2, 1, 1, 3]
    print(unique_occurrences(arr))












