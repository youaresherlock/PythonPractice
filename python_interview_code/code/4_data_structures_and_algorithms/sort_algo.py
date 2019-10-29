#!usr/bin/python
# -*- coding:utf8 -*-

def quicksort(array):
    # 递归出口，空数组或者只有一个元素的数组都是有序的
    if len(array) < 2:
        print('return {}'.format(array))
        return array
    else:
        pivot_index = 0 # 第一个元素作为privot
        pivot = array[pivot_index]
        less_part = [
            i for i in array[pivot_index+1:] if i <= pivot
        ]
        great_part = [
            i for i in array[pivot_index+1:] if i > pivot
        ]
        print('less_part: {} + pivot: {} + quicksort: {}'.format(less_part, pivot, great_part))
        return quicksort(less_part) + [pivot] + quicksort(great_part)

def test_quicksort():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    # ll = [5,4,3,2,1] 最差时间复杂度，递归是一条链子O(n^2)
    print(ll)
    # print(quicksort(ll))
    assert(quicksort(ll) == sorted(ll))
test_quicksort()