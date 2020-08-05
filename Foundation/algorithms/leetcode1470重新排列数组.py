#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn]
的格式排列。请你将数组按 [x1,y1,x2,y2,...,xn,yn]格式重新排列，返回重排
后的数组。
输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7]
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，
所以答案为 [2,3,5,4,1,7]

tips:
1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3

https://leetcode-cn.com/problems/shuffle-the-array
"""
from typing import List


# 一种比较巧妙的方法,数组原地交换
def shuffle(nums: List[int], n: int) -> List[int]:
    desire_id = lambda i: i * 2 if i < n else (i - n) * 2 + 1
    for i in range(2*n):
        j = i
        while nums[i] >= 0:
            j = desire_id(j)
            nums[i], nums[j] = nums[j], -nums[i]
    for i in range(2*n):
        nums[i] = -nums[i]

    return nums


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(shuffle(nums, n))





