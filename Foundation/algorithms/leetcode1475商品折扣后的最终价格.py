#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。
商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j]
相等的折扣，其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，
如果没有满足条件的 j ，你将没有任何折扣。
请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。


输入：prices = [8,4,6,2,3]
输出：[4,2,4,2,3]
解释：
商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
商品 3 和 4 都没有折扣。

[address](https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop)
"""

"""
题目中的信息告诉我们，如果想要获得折扣，则必须获取后方一个小于等于该元素的值，因此可以使用单调栈。
如何维护一个单调栈，笔者用[8,4,6,2,3]这一例子配合代码来说明：
设：空栈stack，prices副本result【也是结果存储空间】，开始遍历prices

(1)第一次循环因为stack为空所以必定入栈，此时stack:[0]，result:[8,4,6,2,3]；
(2)第二次循环prices[1]==4 <= prices[stack[-1]]==8，因此触发折扣条件，减去折扣并弹出栈顶元素，然后将i==1入栈，此时stack:[1]，result:[4,4,6,2,3];
(3)第三次循环无法触发折扣条件，于是i==2入栈，此时stack:[1,2]，result:[4,4,6,2,3];
(4)第四次循环prices[3]==2 <= prices[stack[-1]]==6，触发折扣条件，减去折扣并弹出栈顶元素，循环判断是否触发折扣条件，将i==3入栈，此时stack:[3]，result:[4,2,4,2,3];
(5)第五次循环无法触发折扣条件，于是i==4入栈，此时stack:[3,4]，result:[4,2,4,2,3]；
(6)循环结束，返回结果result
注意：折扣条件是指stack非空且符合价格条件
"""
from typing import List


def final_price(prices: List[int]) -> List[int]:
    stack, result = [], [i for i in prices]
    for i in range(len(prices)):
        # 当stack非空且stack栈顶元素在prices对应的值大于prices[i]时触发while循环
        while stack and prices[stack[-1]] >= prices[i]:
            result[stack[-1]] -= prices[i]  # 将stack中所有对应在prices的满足价格条件的值都减去prices[i]
            stack.pop()  # 弹出栈顶元素
        stack.append(i)  # 储存索引
    return result

