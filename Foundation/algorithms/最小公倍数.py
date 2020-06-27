#!usr/bin/python
# -*- coding:utf8 -*-
"""
求最小公倍数
Input: 5 7
输出: 35
辗转相除法:
def func(a, b):
    c = a % b
    if c == 0:
        return b
    a, b = b, c
    return func(a, b)
"""

"""
方法1:
def common_multiple(x, y):
    # 获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1

    return lcm


x, y = input().split(' ')
print(common_multiple(int(x), int(y)))
"""


"""
最小公倍数 = 两个整数的乘积/最大公约数
最大公约数可以用辗转相除法求得
"""


def common_multiple(x, y):
    mul = x * y
    c = x % y
    while c != 0:
        x, y = y, c
        c = x % y

    print(mul // y)


common_multiple(3, 9)




