#!usr/bin/python
# -*- coding:utf8 -*-
"""
功能: 求一个byte数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1

输入: 一个byte型的数字

输出: 无

返回: 对应的二进制数字中1的最大连续数
Input: 3
Output: 2
"""
num = int(input())


def count(num):
    buf = ""
    while num != 0:
        remainder = num % 2
        buf += str(remainder)
        num = num // 2
    buf = buf[::-1]
    l = buf.split('0')
    return max(len(i) for i in l)


print(count(num))


















