#!usr/bin/python
# -*- coding:utf8 -*-
"""
计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
用来计数的数组C的长度取决于待排序数组中数据的范围(等于待排序数组的最大值与
最小值的差加上1), 因此使得计数排序对于数据范围很大的数组,需要大量时间和内存.
算法的步骤如下:
(1) 找出待排序的数组中的最大和最小的元素
(2) 统计数组中每个值为i的元素出现的次数,存入数组C的第i项
(3) 对所有的计数累加(从C中的第一个元素开始,每一项和前一项相加)
(4) 反向填充目标数组: 将每个元素i放在新数组的第C(i)项, 每放一个元素就将C(i)减去1
平均时间复杂度: O(n+k)
最好情况: O(n+k)
最坏情况: O(n+k)
空间复杂度: O(k)
稳定性: 稳定
"""
import random


def counting_sort(array, max_value):
    bucket_length = max_value + 1
    bucket = [0] * bucket_length
    array_length = len(array)
    sorted_index = 0
    for i in range(array_length):
        bucket[array[i]] += 1
    print(bucket)
    for j in range(bucket_length):
        while bucket[j] > 0:
            array[sorted_index] = j
            bucket[j] -= 1
            sorted_index += 1
    return array


if __name__ == '__main__':
    arr = [random.randint(0, 10) for _ in range(10)]
    print(arr)
    print(counting_sort(arr, 10))















































