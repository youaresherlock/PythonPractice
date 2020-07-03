#!usr/bin/python
# -*- coding:utf8 -*-
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。
Input:
输入一个正整数n(n<39)
Output:
输出青蛙有多少种跳法
"""
number = int(input())


# def choices(number):
#     if number <= 3 :
#         return number
#     else:
#         return choices(number-1) + choices(number-2)

def choices(number):
    if number <= 2:
        return number
    a, b, index = 1, 2, number - 2
    while index:
        a, b = b, a + b
        index -= 1
    return b


print(choices(number))