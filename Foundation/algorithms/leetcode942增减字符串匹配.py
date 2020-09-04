#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

如果 S[i] == "I"，那么 A[i] < A[i+1]
如果 S[i] == "D"，那么 A[i] > A[i+1]

输入："IDID"
输出：[0,4,1,3,2]

[address](https://leetcode-cn.com/problems/di-string-match)
"""
from typing import List


def di_string_match(S: str) -> List[int]:
    """
    S[0] = 'I', 只要令A[0] = 0,
    s[0] = 'D', 只要令A[0] = N,
    同理对剩下的N-1个字母,如果 S[1] == 'I'，我们就令 A[1] 为剩下数中最小的
    那个数；如果 S[1] == 'D'，我们就令 A[1] 为剩下数中最大的那个数
    很容易发现规律:
    每次会把可以使用的数的集合中的最小值或最大值取出,并放到当前的位置,
    可以满足条件
    """
    lo, hi = 0, len(S)
    ans = []
    for x in S:
        if x == 'I':
            ans.append(lo)
            lo += 1
        else:
            ans.append(hi)
            hi -= 1

    return ans + [lo]


if __name__ == '__main__':
    S = 'IDID'
    print(di_string_match(S))















