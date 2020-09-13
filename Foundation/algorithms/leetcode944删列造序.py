#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定由 N 个小写字母字符串组成的数组 A，其中每个字符串长度相等。
你需要选出一组要删掉的列 D，对 A 执行删除操作，使 A 中剩余的每
一列都是 非降序 排列的，然后请你返回 D.length 的最小可能值。
删除 操作的定义是：选出一组要删掉的列，删去 A 中对应列中的所有字符
，形式上，第 n 列为 [A[0][n], A[1][n], ..., A[A.length-1][n]]）


输入：["cba", "daf", "ghi"]
输出：1
解释：
当选择 D = {1}，删除后 A 的列为：["c","d","g"] 和 ["a","f","i"]，均为非降序排列。
若选择 D = {}，那么 A 的列 ["b","a","h"] 就不是非降序排列了。

[address](https://leetcode-cn.com/problems/delete-columns-to-make-sorted)
"""
from typing import List


def min_deletion_size(A: List[str]) -> int:
    ans = 0
    for col in zip(*A):
        if any(col[i] > col[i + 1] for i in range(len(col) - 1)):
            ans += 1
    return ans


if __name__ == '__main__':
    A = ["cba", "daf", "ghi"]
    print(list(zip(*A)))














