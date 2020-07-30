#!usr/bin/python
# -*- coding:utf8 -*-
"""
快速排序原理是：先从数据序列中选一个元素，
并将序列中所有比该元素小的元素都放到它的右边或左边，
再对左右两边分别用同样的方法处之直到每一个待处理的序列的长度为1，
处理结束。
平均时间复杂度: O(nlogn)
最好情况: O(nlogn)
最坏情况: O(n^2)
空间复杂度: O(logn)
稳定性: 不稳定
"""


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot_index = 0
        pivot = array[pivot_index]
        less_part = [i for i in array[pivot_index + 1:] if i <= pivot]
        great_part = [i for i in array[pivot_index + 1:] if i > pivot]
    return quick_sort(less_part) + [pivot] + quick_sort(great_part)


if __name__ == '__main__':
    array = [1, 10, 4, 4, 9, 2, 0]
    print(quick_sort(array))


