#!/usr/bin/python
# -*- coding:utf-8 -*-
from typing import List


def small_elements(nums: List[int]) ->  List[int]:
    result = list()
    points = [0] * 101
    for number in nums:
        points[number] += 1
    for number in nums:
        temp = sum(points[:number])
        result.append(temp)

    return result


if __name__ == '__main__':
    nums = [9, 2, 6, 6, 4]
    print(small_elements(nums))