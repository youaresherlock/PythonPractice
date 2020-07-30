#!usr/bin/python
# -*- coding:utf8 -*-
"""
桶排序是计数排序的升级版。它利用了函数的映射关系，
高效与否的关键就在于这个映射函数的确定。为了使桶排序更加高效，我们需要做到这两点：
在额外空间充足的情况下，尽量增大桶的数量
使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中
同时，对于桶中元素的排序，选择何种比较排序算法对于性能的影响至关重要。
1. 什么时候最快
当输入的数据可以均匀的分配到每一个桶中
2. 什么时候最慢
当输入的数据被分配到了同一个桶中
桶排序只能排序大于零的整数
平均时间复杂度: O(n+k)
最好情况: O(n+k)
最坏情况: O(n^2)
空间复杂度: O(n+k)
稳定性: 稳定
算法步骤:
1. 找出序列中最大和最小值, 目的是为了确定所需桶的数量
2. 将数据放入相应的桶
3. 桶内数据进行排序,可以按照快排等算法进行排序
4. 桶内数据有序取出并合并成完整的有序序列
"""
# from quick_sort import quick_sort


def bucket_sort(alist, bucketsize):
    minValue = alist[0]
    maxValue = alist[1]

    for i in alist:
        if i < minValue:
            minValue = i
        elif i > maxValue:
            maxValue = i
    # 桶数量
    bucketcount = (maxValue - minValue + 1) // bucketsize
    # 对应的桶
    bucket_lists = list([] for _ in range(bucketcount))

    # 把数据放入相应的桶
    for i in alist:
        bucket_index = (i - minValue) // bucketsize
        bucket_lists[bucket_index].append(i)

    # 桶内快排
    for j in bucket_lists:
        quick_sort(j, 0, len(j) - 1)  # 这里采用的是快排，需要引入快排的包，因为篇幅原因，这里不放快排的代码

    # 合并数据
    result = []
    for j in bucket_lists:
        if len(j) != 0:
            result.extend(j)
    return result


















