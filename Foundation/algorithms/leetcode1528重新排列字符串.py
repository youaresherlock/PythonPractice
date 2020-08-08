#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个字符串 s 和一个 长度相同 的整数数组 indices 。
请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。
返回重新排列后的字符串。

输入：s = "codeleet", indices = [4,5,6,7,0,2,1,3]
输出："leetcode"
解释：如图所示，"codeleet" 重新排列后变为 "leetcode" 。

[address](https://leetcode-cn.com/problems/shuffle-string)
"""
from typing import List


def restore_string(s: str, indices: List[int]) -> str:
    # result = []
    # zipped = sorted(list(enumerate(indices)), key=lambda x: x[1])
    # for index, _ in zipped:
    #     result.append(s[index])
    #
    # return ''.join(result)
    target = list(s)
    for i, si in enumerate(indices):
        target[si] = s[i]

    return ''.join(target)


if __name__ == '__main__':
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    print(restore_string(s, indices))
















