#!usr/bin/python
# -*- coding:utf8 -*-
from typing import List


def max_point(points: List, k: int) -> int:
    max_index, max_sum = k, 0
    for i in range(max_index + 1):
        another_index = max_index - i
        left_list = points[:i]
        right_list = list(reversed(points))[:another_index]
        print(left_list, right_list, i)
        sum_points = sum(left_list + right_list)
        if max_sum < sum_points:
            max_sum = sum_points

    return max_sum


if __name__ == '__main__':
    points = [1, 2, 3, 4, 5, 6, 1]
    print(max_point(points, 3))