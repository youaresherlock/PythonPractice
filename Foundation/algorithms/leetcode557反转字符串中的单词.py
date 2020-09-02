#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格
和单词的初始顺序。

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

提示：
在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

[address](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/)
"""


def reverse_words(s: str) -> str:
    # messages = s.split()
    # for i in range(len(messages)):
    #     messages[i] = messages[i][::-1]
    #
    # return ' '.join(messages)

    # return ' '.join(word[::-1] for word in s.split(' '))
    return ' '.join(s.split(' ')[::-1])[::-1]
















