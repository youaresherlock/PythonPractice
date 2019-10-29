#!usr/bin/python
# -*- coding:utf8 -*-

# 归并排序， 合并两个有序数组
def merge_sorted_list(sorted_a, sorted_b):
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_seq = []

    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1

    # 将剩余的元素合并到有序数组里
    # while a < length_a:
    #     new_sorted_seq.append(sorted_a[a])
    #     a += 1
    # while b < length_b:
    #     new_sorted_seq.append(sorted_b[b])
    #     b += 1
    if a < length_a:
        new_sorted_seq.extend(sorted_a[a:])
    else:
        new_sorted_seq.extend(sorted_b[b:])
    return new_sorted_seq

def test_merge_sorted_list():
    a = [1, 2, 5]
    b = [0, 3, 4, 8]
    print(merge_sorted_list(a, b))

# test_merge_sorted_list()

# 分治法三步走。注意递归出口

def mergesort(array):
    # 递归出口
    if len(array) <= 1:
        return array
    else:
        # mid = len(array) // 2
        mid = int(len(array) / 2)
        left_half = mergesort(array[:mid])
        right_half = mergesort(array[mid:])
        return merge_sorted_list(left_half, right_half)

def test_mergesort():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    print(ll)
    assert mergesort(ll) == sorted(ll)

test_mergesort()