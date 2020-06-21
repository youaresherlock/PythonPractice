#!usr/bin/python
# -*- coding:utf8 -*-
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
输入: 121 true
输出: 10 false
"""

# 方法1:
# num = input()
# print("true" if num == num[::-1] and int(num) >= 0 else "false")


# 方法2:
# num = input()
#
#
# def check(num):
#     if int(num) < 0:
#         return "false"
#     beg, end = 0, len(num) - 1
#     while beg < end:
#         if num[beg] == num[end]:
#             beg += 1
#             end -= 1
#         else:
#             return "false"
#     return "true"
#
#
# print(check(num))


# 方法3:
num = int(input())


def check(num):
    if num < 0:
        return "false"
    elif num == 0:
        return "true"
    l = []
    while num != 0:
        l.append(num % 10)
        num = num // 10
    return "true" if l == list(reversed(l)) else "false"


print(check(num))