#!/usr/bin/python
# -*- coding:utf-8 -*-
from typing import List


# 方法1: 这种方法时间复杂度太高，超时
# def breakfast_number(staple: List[int], drinks: List[int], x: int) -> int:
#     count = 0
#     for i in range(len(staple)):
#         for j in range(len(drinks)):
#             if staple[i] + drinks[j] <= x:
#                 count += 1
#
#     return count


"""
arr[i] 第i个元素表示食物里面价格小于等于i的个数

然后遍历饮料
lt = x - 当前饮料的价格
如果lt <= 0，则当前饮料的价格已经超过了上限
否则arr[lt]代表的是当前饮料可以和食物的组合数。
"""
def breakfast_number(staple: List[int], drinks: List[int], x: int) -> int:
    ans = 0
    arr = [0 for i in range(x + 1)]

    for sta in staple:
        if sta < x:
            arr[sta] += 1

    for i in range(2, x):
        arr[i] += arr[i - 1]

    for drink in drinks:
        lt = x - drink
        if lt <= 0:
            continue
        ans += arr[lt]

    return ans % (10 ** 9 + 7)


if __name__ == '__main__':
    staple = [2, 1, 1]
    drinks = [8, 9, 5, 1]
    print(breakfast_number(staple, drinks, 9))












































