"""
归并排序；
采用分治法
分割: 递归的把当前序列平均分割成两半
集成: 在保持元素顺序的同时将上一步得到的子序列集成到一起(归并)
"""
from typing import List


def merge(arr1: List[int], arr2: List[int]):
    result = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    if arr1:
        result += arr1
    if arr2:
        result += arr2
    return result


def merge_sort(arr: List[int]):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


if __name__ == '__main__':
    import random
    arr = [random.randint(0, 100) for _ in range(10)]
    print('原始数据:', arr)
    arr_new = merge_sort(arr)
    print('归并排序结果:', arr_new)


























































