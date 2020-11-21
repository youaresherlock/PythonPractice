#!usr/bin/python
# -*- coding:utf8 -*-
from typing import List


def max_point(points: List[int], k: int) -> int:
    max_index, max_sum = k, 0
    for i in range(max_index + 1):
        another_index = max_index - i
        left_list = points[:i]
        right_list = points[-another_index:] if another_index > 0 else []
        sum_points = sum(left_list + right_list)
        if max_sum < sum_points:
            max_sum = sum_points

    return max_sum


if __name__ == '__main__':
    message = [1, 2, 3, 4, 5, 6, 1]
    print(max_point(message, 3))