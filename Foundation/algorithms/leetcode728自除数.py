#!usr/bin/python
# -*- coding:utf8 -*-
"""
自除数 是指可以被它包含的每一位数除尽的数。
例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
还有，自除数不允许包含 0 。
给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

输入：
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

每个输入参数的边界满足 1 <= left <= right <= 10000。

[address](https://leetcode-cn.com/problems/self-dividing-numbers/)
"""
from typing import List


def self_dividing_numberes(left: int, right: int) -> List[int]:
    def is_dividing_number(number):
        bit = number
        while bit != 0:
            bit_number = bit % 10
            bit = bit // 10
            if not bit_number or number % bit_number != 0:
                return False

        return True

    return list(filter(is_dividing_number, range(left, right + 1)))


if __name__ == '__main__':
    left = 1
    right = 22
    print(self_dividing_numberes(left, right))



























