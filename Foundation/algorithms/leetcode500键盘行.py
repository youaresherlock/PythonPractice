#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]


注意：
你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。

[address](https://leetcode-cn.com/problems/keyboard-row/)
"""
from typing import List


def find_words(words: List[str]) -> List[str]:
    line1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    line2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    line3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    mapping = dict(list(zip(line1, len(line1) * ['q'])) +
                   list(zip(line2, len(line2) * ['a'])) +
                   list(zip(line3, len(line3) * ['z'])))

    results = []
    for word in words:
        result = set()
        for char in word:
            result.add(mapping.get(char.lower()))
        if len(result) == 1:
            results.append(word)

    return results


if __name__ == '__main__':
    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(find_words(words))














