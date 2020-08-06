#!usr/bin/python
# -*- coding:utf8 -*-
"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"
和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

输入: s = "abcdefg", k = 2
输出: "cdefgab" 7

https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
"""


def reverse_left_words(s: str, k: int) -> str:
    # solution 1:
    # return s[k:] + s[:k]
    # solution 2:
    # n = len(s)
    # s = s + s
    # return s[k: n + k]
    # solution 3:
    n = len(s)
    res = ''
    for i in range(k, k+n):
        res += s[i % n]

    return res


if __name__ == '__main__':
    s = "hello kitty"
    k = 2
    print(reverse_left_words(s, k))




















