#!usr/bin/python
# -*- coding:utf8 -*-
"""
有一只兔子，从出生后第3个月起每个月都生一只兔子，
小兔子长到第三个月后每个月又生一只兔子，
假如兔子都不死，问每个月的兔子总数为多少？
Input: 9
Output: 34
"""


while True:
    try:
        month = int(input())
        if month < 3:
            print(1)
        else:
            a, b = 1, 1
            for i in range(3, month + 1):
                a, b = b, a + b
            print(b)
    except:
        break



















