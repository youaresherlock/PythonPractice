#!usr/bin/python
# -*- coding:utf8 -*-
"""
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

输入: s = "leetcode"
输出: false

[address](https://leetcode-cn.com/problems/is-unique-lcci/)
"""


def is_unique(astr: str) -> bool:
    # 1. 利用集合去重
    # return len(astr) == len(set(astr))

    # 2. 遍历一遍字符串,如果重复则返回False
    buckets = [0] * 26
    for char in astr:
        buckets[ord(char) - 97] += 1
        if buckets[ord(char) - 97] > 1:
            return False

    return True













