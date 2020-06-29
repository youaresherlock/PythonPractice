#!usr/bin/python
# -*- coding:utf8 -*-
"""
输入一个String数据
输出string中大写字母的个数
"""
import re


while True:
    try:
        message = input()
        result = re.findall('[A-Z]', message)
        print(len(result))
    except Exception:
        break

"""
方法二:
while True:
    try:
        string = input()
        num = 0
        for s in string:
            if 'A' <= s <= 'Z':
                num += 1
        print(num)
    except:
        break
"""