#!usr/bin/python
# -*- coding:utf8 -*-
"""完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。

它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。

例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。

给定函数count(int n),用于计算n以内(含n)完全数的个数。计算范围, 0 < n <= 500000

返回n以内完全数的个数。 异常情况返回-1
Input: 输入一个数字
Output: 输出完全数的个数

"""
import math 


def is_perfect_number(number):
    if number <= 2:
        return False
    approximate = [1]
    for i in range(2, math.ceil(number / 2) + 1):
        if number % i == 0:
            approximate.append(i)
    if sum(approximate) == number:
        return True
    else:
        return False


while True:
    try:
        number = int(input())
        print(len(list(filter(is_perfect_number, range(1, number + 1)))))
    except:
        break



























