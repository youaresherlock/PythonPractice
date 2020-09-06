#!usr/bin/python
# -*- coding:utf8 -*-
"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组
char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1)
的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

[address](https://leetcode-cn.com/problems/reverse-string)
"""
from typing import List


def reverse_string(s: List[str]) -> None:
    # 1. 列表反转方法
    # s.reverse()

    # 2. 双指针
    # start, end = 0, len(s) - 1
    # while start < end:
    #     s[start], s[end] = s[end], s[start]
    #     start, end = start + 1, end - 1

    # 3. 递归
    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

    helper(0, len(s) - 1)


if __name__ == '__main__':
    s = ['a', 'b', 'c', 'd']
    reverse_string(s)
    print(s)






















