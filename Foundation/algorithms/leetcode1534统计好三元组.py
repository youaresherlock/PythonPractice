#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个整数数组 arr ，以及 a、b 、c 三个整数。请你统计其中好三元组的数量。
如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
其中 |x| 表示 x 的绝对值。

返回 好三元组的数量 。

输入：arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
输出：4
解释：一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)] 。

[address](https://leetcode-cn.com/problems/count-good-triplets)

3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000
"""
from typing import List


def count_good_triplets(arr: List[int], a: int, b: int, c: int) -> int:
    # 枚举
    # 用O(n^3)的循环一次枚举所有的(i, j, k), 对于每组(i, j, k),
    # 判断arr[i], arr[j], arr[k]是否满足条件
    # n = len(arr)
    # cnt = 0
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         for k in range(j + 1, n):
    #             if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
    #                 cnt += 1
    #
    # return cnt
    # 优化枚举
    ans = 0
    n = len(arr)
    total = [0] * 1001
    for j in range(n):
        for k in range(j + 1, n):
            if abs(arr[j] - arr[k]) <= b:
                lj, rj = arr[j] - a, arr[j] + a
                lk, rk = arr[k] - c, arr[k] + c
                l = max(0, lj, lk)
                r = min(1000, rj, rk)
                if l <= r:
                    ans += total[r] if l == 0 else total[r] - total[l - 1]
        for k in range(arr[j], 1001):
            total[k] += 1

    return ans


if __name__ == '__main__':
    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3
    print(count_good_triplets(arr, a, b, c))
























