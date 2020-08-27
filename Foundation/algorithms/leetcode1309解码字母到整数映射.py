#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希
望按下述规则将 s 映射为一些小写英文字符：s
字符（'a' - 'i'）分别用（'1' - '9'）表示。
字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 
返回映射之后形成的新字符串。
题目数据保证映射始终唯一。

输入：s = "10#11#12"
输出："jkab"
解释："j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

[address](https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping)
"""


def freq_alphabets(s: str) -> str:
    """
    对字符串s进行顺序遍历, 当遍历到位置i时,我们首先检查s[i+2]存在且为
    #,那么i, i+1和i+2表示一个'j'到'z'之间的字符,否则位置i表示一个'a'到
    'i'的字符
    """
    def get(st):
        return chr(int(st) + 96)

    i, ans = 0, ''
    while i < len(s):
        if i + 2 < len(s) and s[i + 2] == '#':
            ans += get(s[i: i+2])
            i += 2
        else:
            ans += get(s[i])
        i += 1

    return ans



















