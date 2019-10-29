#!usr/bin/python
# -*- coding:utf8 -*-

def binary_search(array, target):  # 二分查找
    if not array:
        return -1
    beg, end = 0, len(array)
    while beg < end:
        mid = beg + (end - beg) // 2  # py3
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid
        else:
            beg = mid + 1
    return -1

# 递归方式实现二分
def binary_search_recursive(sorted_array, beg, end, val):
    if beg >= end:
        return -1
    mid = int((beg+end) / 2)
    if sorted_array[mid] == val:
        return mid
    elif sorted_array[mid] > val:
        return binary_search_recursive(sorted_array, beg, mid, val)
    else:
        return binary_search_recursive(sorted_array, mid+1, end, val)

def test():
    """
    如何设计测试用例：(等价类划分)
    - 正常值功能测试
    - 边界值（比如最大最小，最左最右值）
    - 异常值（比如 None，空值，非法值）
    """
    # 正常值，包含有和无两种结果
    assert binary_search_recursive([0, 1, 2, 3, 4, 5], 0, 6, 1) == 1
    assert binary_search([0, 1, 2, 3, 4, 5], 1) == 1
    assert binary_search([0, 1, 2, 3, 4, 5], 6) == -1
    assert binary_search([0, 1, 2, 3, 4, 5], -1) == -1
    # 边界值
    assert binary_search([0, 1, 2, 3, 4, 5], 0) == 0
    assert binary_search([0, 1, 2, 3, 4, 5], 5) == 5
    assert binary_search([0], 0) == 0

    # 异常值
    assert binary_search([], 1) == -1
