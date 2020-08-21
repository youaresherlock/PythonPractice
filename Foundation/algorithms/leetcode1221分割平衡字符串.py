#!usr/bin/python
# -*- coding:utf8 -*-
"""
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
返回可以通过分割得到的平衡字符串的最大数量。

输入：s = "RLLLLRRRLR"
输出：3
解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。

[address](https://leetcode-cn.com/problems/split-a-string-in-balanced-strings)
"""


# 可遍历字符串,遇到L加一,R减一,当为0时表示经过一个平衡字符串
def balanced_string_split(s: str) -> int:
    # 方法1. 贪心算法
    # balance = 0
    # res = 0
    # for char in s:
    #     if char == 'L':
    #         balance += 1
    #     elif char == 'R':
    #         balance -= 1
    #     if balance == 0:
    #         res += 1
    #
    # return res
    # 方法2. 栈操作
    # 1. 栈为空则入栈
    # 2. 栈不为空则判断当前元素是否与栈顶数据一致,一致入栈,不一致出栈
    # 3. 判断栈是否为0, 为0则说明成功匹配一个平衡字符串, 数量加一
    res = 0
    stack = []
    for char in s:
        if len(stack) > 0:
            stack.append(char) if stack[0] == char else stack.pop()
            if len(stack) == 0:
                res += 1
        else:
            stack.append(char)

    return res






