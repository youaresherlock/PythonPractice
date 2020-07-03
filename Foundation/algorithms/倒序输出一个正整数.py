#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一个正整数n，请尽可能利用递归实现倒序输出
Input: 输入一个正整数n
Output: 倒序输出正整数
"""
number = input().rstrip('0')


def output(number):
    if len(number) < 1:
        return number
    return output(number[1:]) + number[:1]


print(int(output(number)))