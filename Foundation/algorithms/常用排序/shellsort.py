#!usr/bin/python
# -*- coding:utf8 -*-
"""
希尔排序也称递减增量排序算法, 是插入排序的一种更高效的改进版本,但希尔排序是非稳定排序算法.
希尔排序是基于插入排序的以下两点性质而提出改进方法的：
    1. 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率；
    2. 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位；
希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。这样可以显著减少数据交换
的次数,以达到加快排序速度的目的.

希尔排序每一轮按照事先决定的间隔进行插入排序, 间隔会依次缩小,最后一次一定要是1
平均时间复杂度: O(nlogn)
最好情况: O(nlog^2 n)
最坏情况: O(nlog^2 n)
空间复杂度: O(1)
稳定性: 不稳定
算法步骤:
"""
import math
import random


def shell_sort(array):
    gap = 1
    while gap < len(array) / 3:
        gap = gap * 3 + 1

    while gap > 0:
        for i in range(gap, len(array)):
            key = array[i]
            j = i - gap
            while j >= 0 and key < array[j]:
                array[j+gap] = array[j]
                j -= gap
            array[j+gap] = key
        gap = math.floor(gap/3)

    return array


if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    print(shell_sort(array))



















