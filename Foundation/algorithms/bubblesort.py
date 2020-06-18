#!usr/bin/python
# -*- coding:utf8 -*-
"""
冒泡排序（Bubble Sort）也是一种简单直观的排序算法。
它重复地走访过要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，
也就是说该数列已经排序完成
"""


def bubble_sort(array):
    n = len(array)
    # 遍历n-1次
    for i in range(n-1):
        for j in range(0, n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(arr))











































