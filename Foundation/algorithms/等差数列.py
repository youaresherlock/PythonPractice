#!usr/bin/python
# -*- coding:utf8 -*-
"""
功能:等差数列 2，5，8，11，14。。。。

输入:正整数N >0

输出:求等差数列前N项和

返回:转换成功返回 0 ,非法输入与异常返回-1

本题为多组输入，请使用while(cin>>)等形式读取数据

输入一个正整数。
输出一个相加后的整数。
n = na1 + n(n-1)*d/2
"""

while True:
    try:
        num = input()
        if num.isdigit():
            num = int(num)
            print(num * 2 + num * (num - 1) * 3 // 2)
        else:
            print(-1)
    except Exception as e:
        break














