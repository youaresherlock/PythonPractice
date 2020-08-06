#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」
与「各位数字之和」的差。

输入：n = 234
输出：15
解释：
各位数之积 = 2 * 3 * 4 = 24
各位数之和 = 2 + 3 + 4 = 9
结果 = 24 - 9 = 15

https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
"""


def subtract_product_and_sum(n: int) -> int:
    add, mul = 0, 1
    while n > 0:
        digit = n % 10
        n = n // 10
        add += digit
        mul *= digit

    return mul - add


if __name__ == '__main__':
    n = 234
    print(subtract_product_and_sum(n))




















