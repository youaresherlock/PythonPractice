#!usr/bin/python
# -*- coding:utf8 -*-
"""
验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
例如：
1^3=1
2^3=3+5
3^3=7+9+11
4^3=13+15+17+19
输入: 输入一个int整数
输出: 输出分解后的string
Input: 6
Input: 31+33+35+37+39+41
"""
while True:
    try:
        number = int(input())
        multi = number ** 2
        result = [str(i) for i in range(multi - number + 1, multi + number, 2)]
        print('+'.join(result))
    except Exception:
        break






























