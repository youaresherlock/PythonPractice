#!usr/bin/python
# -*- coding:utf8 -*-
"""
solo和koko分积木
koko要求两人分配的积木重量相等,koko计算重量时会将两个数
转换成二进制加法,而且总会忘记进位(每个进位都会忘记)

solo来分配积木,想要使自己得到的积木总重量最大,怎么分配
3
3 5 6 
"""
from functools import reduce


def compute(message):
    message.sort()
    for i in range(len(message)):
        result = reduce(lambda x, y: x ^ y, message[:i] + message[i+1:])
        if message[i] == result:
            return sum(message) - message[i]


if __name__ == '__main__':
    count = input()
    message = list(map(int, input().split()))
    print(compute(message))

















