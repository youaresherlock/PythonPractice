#!usr/bin/python
# -*- coding:utf8 -*-
"""
桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，
拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。

https://leetcode-cn.com/problems/na-ying-bi/
"""
import math
from typing import List


def min_count(coins: List[int]) -> int:
    # result = 0
    # for i in coins:
    #     result += math.ceil(i/2)
    #
    # return result
    return sum([(x + 1) // 2 for x in coins])


if __name__ == '__main__':
    coins = [2, 3, 10]
    print(min_count(coins))



































