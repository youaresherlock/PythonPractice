#!usr/bin/python
# -*- coding:utf8 -*-
"""
插入排序是一种简单直观的排序算法。它
的工作原理是通过构建有序序列，对于未排序数据，
在已排序序列中从后向前扫描，找到相应位置并插入
平均时间复杂度: O(n^2)
最好情况: O(n)
最坏情况: O(n^2)
空间复杂度: O(1)
稳定性: 稳定
"""
import random


def insert_sort(array):
    for i in range(1, len(array)):
        key = array[i]

        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


if __name__ == '__main__':
    array = [random.randint(0, 100) for _ in range(10)]
    print(insert_sort(array))































