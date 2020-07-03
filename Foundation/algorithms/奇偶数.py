#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一个长度为n的数组，请将数组中元素按照奇偶性重新划分，所有奇数靠左边，
所有偶数靠右边，然后分别对奇数、偶数部分进行排序
请尽可能实现通过一次遍历并且原地操作（即不得借助其他数组）进行奇偶划分。
Input
输入有两行，第一行输入一个数字n表示数组的长度，

第二行依次输入n个数字，表示数组的元素值。
Output
打印按照奇偶排列并各自排序后的新数组，元素之间用空格隔开

[类似leetcode原题](https://leetcode-cn.com/problems/sort-array-by-parity/)

思路: 先进行奇偶划分然后再排序
双指针遍历,一个从数组头部进行,一个从尾部运行;
对于两个指针指的数字进行判断,将会有四种情况:
1. 左偶右奇 不作处理,两个指针分别移动一个单位
2. 左奇右偶 进行交换,两个指针分别移动一个单位
3. 都是奇数 将尾部指针移动一个单位,再进行上述判断
4. 都是偶数 将头部指针移动一个单位,再进行上述判断

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        while i < j:
            # 左偶右奇
            if A[i] % 2 == 0 and A[j] % 2 != 0:
                i += 1
                j -= 1
            # 左奇右偶
            elif A[i] % 2 != 0 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            # 都是奇数
            elif A[i] % 2 != 0 and A[j] % 2 != 0:
                j -= 1
            # 都是偶数
            else:
                i += 1
        return A
"""
import sys


def split_even_odd():
    length = int(sys.stdin.readline())
    l = sys.stdin.readline().strip().split(' ')
    i = 0
    j = len(l) - 1
    index = 0
    while i < j:
        # 左偶右奇
        if int(l[i]) % 2 == 0 and int(l[j]) % 2 != 0:
            l[i], l[j] = l[j], l[i]
            index = i
            i += 1
            j -= 1
        # 左奇右偶
        elif int(l[i]) % 2 != 0 and int(l[j]) % 2 == 0:
            index = i
            i += 1
            j -= 1
        # 都是奇数
        elif int(l[i]) % 2 != 0 and int(l[j]) % 2 != 0:
            i += 1
        # 都是偶数
        else:
            j -= 1
    print(' '.join(sorted(l[:index+1], key=lambda x: int(x)) + sorted(l[index+1:], key=lambda x: int(x))))


split_even_odd()

"""
length = int(input())
l = input().strip().split(' ')
print(' '.join(sorted([i for i in l if int(i) % 2 != 0], key=lambda x: int(x)) + sorted([i for i in l if int(i) % 2 == 0], key=lambda x: int(x))))
"""








