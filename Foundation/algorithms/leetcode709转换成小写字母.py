#!usr/bin/python
# -*- coding:utf8 -*-
"""
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串
中的大写字母转换成小写字母，之后返回新的字符串。

输入: "Hello"
输出: "hello"

[address](https://leetcode-cn.com/problems/to-lower-case/)
"""


def to_lower_case(string: str) -> str:
    # return string.lower()
    # 1. 利用ascii码转换, 'A'-'Z'对应65-90, 'a'-'z'对应97-122
    # res = []
    # for char in string:
    #     if 65 <= ord(char) <= 90:
    #         res.append(chr(ord(char) + 32))
    #     else:
    #         res.append(char)
    #
    # return ''.join(res)

    # 2. 字典,效率最高
    dic = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f',
           'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l',
           'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r',
           'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x',
           'Y': 'y', 'Z': 'z'}

    res = []
    for char in string:
        if dic.get(char):
            res.append(dic[char])
        else:
            res.append(char)

    return ''.join(res)


if __name__ == '__main__':
    string = "HellO"
    print(to_lower_case(string))


























