#!usr/bin/python
# -*- coding:utf8 -*-
"""
计算两个字符串的最大公共字串的长度，字符不区分大小写
"""

while True:
    try:
        a = input().lower()
        b = input().lower()
        n = 0
        for i in range(len(a)):
            if a[i-n:i+1] in b:
                n += 1
        print(n)
    except:
        break