#!usr/bin/python
# -*- coding:utf8 -*-
"""
基数排序是一种非比较型整数排序算法, 其原理是将整数按位数切割成不同的数字,然后按
每个位数分别比较.
平均时间复杂度: O(nxk)
最好情况: O(nxk)
最坏情况: O(nxk)
空间复杂度: O(n+k)
稳定性: 稳定
算法步骤:
1. 取得数组中的最大数,并取得位数
2. 对数位较短的数前面补零
3. 分配,先从个位开始,根据位值(0-9)分别放到0-9号桶中
4. 收集, 再将放置在0-9号桶中的数据按顺序放到数组中
5. 重复3、4过程,直到最高位,即可完成排序

基数排序vs计数排序vs桶排序:
基数排序: 根据键值的每位数字来分配桶
计数排序: 每个桶只存储单一键值
桶排序: 每个桶存储一定范围的数值
1 9 8 12 32 48 19 99
0 1  2  3 4 5 6 7 8 9
  1 12,32        8,48  9,19,99
"""
from typing import List


def radix_sort(arr: List[int]):
    n = len(str(max(arr)))  # 记录最大值的位数
    for k in range(n):  # n轮排序
        # 每一轮生成10个元素的列表
        bucket_list = [[] for _ in range(10)]
        for i in arr:
            # 按第k位放入到桶中
            index = i // (10**k) % 10
            bucket_list[index].append(i)
        # 按当前桶的顺序重新排序列表
        arr = [j for i in bucket_list for j in i]
        print(bucket_list, arr, sep='\n')

    return arr


if __name__ == '__main__':
    arr = [1, 9, 8, 12, 32, 48, 19, 99]
    arr_new = radix_sort(arr)
    print(arr_new)








































