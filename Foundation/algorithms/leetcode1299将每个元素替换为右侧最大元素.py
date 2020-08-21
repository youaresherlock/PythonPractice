#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个数组 arr,请你将每个元素用它右边最大的元素替换，如果是最后一个元素，
用 -1 替换。完成所有替换操作后，请你返回这个数组。

输入：arr = [17,18,5,4,6,1]
输出：[18,6,6,6,1,-1]

提示：
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5

[address](https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side/)
"""
from typing import List


def replace_elements(arr: List[int]) -> List[int]:
    n = len(arr)
    ans = [0] * (n - 1) + [-1]
    for i in range(n - 2, -1, -1):
        print(ans, ans[i+1], arr[i+1])
        ans[i] = max(ans[i + 1], arr[i + 1])
    return ans


if __name__ == '__main__':
    arr = [17, 18, 5, 4, 6, 1]
    print(replace_elements(arr))


















