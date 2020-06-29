#!usr/bin/python
# -*- coding:utf8 -*-
"""
入门
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
Input: 5 输入一个整数（int类型）输入一个整数（int类型）
Output: 2 这个数转换成2进制后，输出1的个数
"""


"""
方法1:
num = int(input())
print(bin(num).count('1'))
"""
num = int(input())

l = list()
while num != 0:
    remainder = num % 2
    l.append(str(remainder))
    num = num // 2
l.reverse()
print(''.join(l).count('1'))