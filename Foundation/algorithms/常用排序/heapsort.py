#!usr/bin/python
# -*- coding:utf8 -*-
"""
堆排序(heapsort)是指利用堆这种数据结构所设计的一种排序算法.
大顶堆: 每个节点的值都大于或等于其子节点的值,在堆排序算法中用于升序排序
小顶堆: 每个节点的值都小于或等于其子节点的值,在堆排序算法中用于降序排序
平均时间复杂度: O(nlogn)
最好情况: O(nlogn)
最坏情况: O(nlogn)
空间复杂度: O(1)
稳定性: 不稳定
算法步骤:
1.构造初始堆。将给定无序序列构造成一个大顶堆（一般升序采用大顶堆，降序采用小顶堆)；
2.将堆顶元素与末尾元素进行交换，使末尾元素最大。然后继续调整堆，再将堆顶元素与末尾元素交换，得到第二大元素；
3.重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素；
4.如此反复进行交换、重建、交换，直到整个序列有序。
"""


def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr, i)


def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def heapSort(arr):
    global arrLen
    arrLen = len(array)
    buildMaxHeap(arr)
    print(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr


if __name__ == '__main__':
    import random
    array = [random.randint(0, 100) for _ in range(10)]
    print(heapSort(array))









