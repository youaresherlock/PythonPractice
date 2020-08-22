#!usr/bin/python
# -*- coding:utf8 -*-
"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

输入：s = "We are happy."
输出："We%20are%20happy."

[address](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)
"""


def replace_space(s: str) -> str:
    # 内置函数
    # return s.replace(' ', '%20')
    res = []
    for c in s:
        if c == ' ':
            res.append('%20')
        else:
            res.append(c)

    return ''.join(res)


if __name__ == '__main__':
    s = "We are happy."
    print(replace_space(s))















