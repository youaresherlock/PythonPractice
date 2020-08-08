#!usr/bin/python
# -*- coding:utf8 -*-
"""
平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi]。请你计算访问所有这些点需要的
最小时间（以秒为单位）。你可以按照下面的规则在平面上移动：
每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各
移动一个单位长度）。必须按照数组中出现的顺序来访问这些点。

[address](https://leetcode-cn.com/problems/minimum-time-visiting-all-points)

思路：
对于平面上两个点x=(x0, x1)和y=(y0, y1),设横坐标距离之差为dx,纵坐标距离之差为dy.
有三种情况来计算从x到y的最小次数
1. dx < dy 沿对角线移动dx次,竖直移动dy-dx次,一共dy次
2. dx = dy 沿对角线移动dx次
3. dx > dy 沿对角线移动dy次,水平移动dx-dy次,一共dy次
可以发现，对于任意一种情况，从 x 移动到 y 的最少次数为 dx 和 dy 中的较大值
max(dx, dy)，这也被称作 x 和 y 之间的 切比雪夫距离。

由于题目要求，需要按照数组中出现的顺序来访问这些点。因此我们遍历整个数组，
对于数组中的相邻两个点，计算出它们的切比雪夫距离，所有的距离之和即为答案。
"""
from typing import List


def min_time_to_visit_all_points(points: List[List[int]]) -> int:
    x0, x1 = points[0]
    ans = 0
    for i in range(1, len(points)):
        y0, y1 = points[i]
        ans += max(abs(x0 - y0), abs((x1 - y1)))
        x0, x1 = points[i]

    return ans


if __name__ == '__main__':
    points = [[1, 1], [3, 4], [-1, 0]]
    print(min_time_to_visit_all_points(points))


















