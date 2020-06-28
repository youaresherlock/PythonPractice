#!usr/bin/python
# -*- coding:utf8 -*-
"""
首先输入数字n，表示要输入多少个字符串。连续输入字符串
(输出次数为N,字符串长度小于100)。
按长度为8拆分每个字符串后输出到新的字符串数组，
长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
5
wx
x54on1s73ubb9c
f29iiqb28l72k
y
y5vor
--------
wx000000
x54on1s7
3ubb9c00
f29iiqb2
8l72k000
y0000000
y5vor000
"""

n = int(input())

for i in range(0, n):
    x = input()
    if len(x) < 8:
        print(x + '0' * (8 - len(x)))
    else:
        while len(x) > 8:
            print(x[:8])
            x = x[8:]
        print(x + '0' * (8 - len(x)))







