#!usr/bin/python
# -*- coding:utf8 -*-

"""
翻转字符数组 https://leetcode.com/problems/reverse-string/
s是一个字符串列表
1. s.reverse
"""


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        beg = 0
        end = len(s) - 1
        while beg < end:
            s[beg], s[end] = s[end], s[beg]
            beg += 1
            end -= 1

