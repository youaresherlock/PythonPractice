#!usr/bin/python
# -*- coding:utf8 -*-
"""
选择排序（Selection sort）是一种简单直观的排序算法。
它的工作原理如下。首先在未排序序列中找到最小（大）元素，
存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，
然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
平均时间复杂度: O(n^2)
最好情况: O(n^2)
最坏情况: O(n^2)
空间复杂度: O(1)
稳定性: 不稳定
"""


def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]

    return array


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print(selection_sort(arr))





























































