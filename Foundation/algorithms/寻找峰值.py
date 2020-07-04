#!usr/bin/python
# -*- coding:utf8 -*-
"""
峰值元素是指其值大于左右相邻值的元素。
给定一个输入数组nums，其中nums[i] ≠ nums[i+1]，找到峰值元素并输出其索引值，
你可以假设nums[-1] = nums[n] = -∞。
注意：不用担心存在多个峰值，测试数据保证仅存在一个峰值
Input
输入一个整数n，表述数组的长度，接下来依次输入n个数字，表示数组元素的值
Output
输出该数组峰值对应的索引位置
sample input:
6
1 8 9 10 7 5
sample output:
3
"""
length = int(input())
message_list = list(map(int, input().strip().split(' ')))
for i in range(1, length - 1):
    if message_list[i] > message_list[i-1] and message_list[i] > message_list[i+1]:
        print(i)
        break


# 二分
# n = int(input())
# num = list(map(int, input().split(' ')))
# if len(num) < 3:
#     if len(num) == 1:
#         print(0)
#     else:
#         print(0 if num[0] > num[1] else 1)
#
# l = 0
# r = len(num) - 1
# while l < r:
#     m = (l + r + 1) // 2
#     if num[m] > num[m - 1]:
#         l = m
#     else:
#         r = m - 1
# print(l)