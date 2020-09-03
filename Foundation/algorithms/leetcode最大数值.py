#!usr/bin/python
# -*- coding:utf8 -*-
"""
编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。

输入： a = 1, b = 2
输出： 2

[address](https://leetcode-cn.com/problems/maximum-lcci/)
"""


def maximum(a: int, b:int) -> int:
    # max(a,b) = (|a-b|+a+b)/2
    return (abs(a - b) + a + b) // 2


if __name__ == '__main__':
    a = 2
    b = 5
    print(maximum(a, b))



















