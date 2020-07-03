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
# def find_top(message_list):
#     pivot = length // 2
#     if 1 < pivot < length - 1 and message_list[pivot] > message_list[pivot-1] and \
#             message_list[pivot] > message_list[pivot+1]:
#         print(pivot)
#         return 1
#
#     return find_top(message_list[:pivot+1]) or find_top(message_list[pivot+1:])
#
#
# find_top(message_list)

