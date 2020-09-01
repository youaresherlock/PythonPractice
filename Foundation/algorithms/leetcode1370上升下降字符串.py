#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个字符串 s ，请你根据下面的算法重新构造字符串：

从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
重复步骤 2 ，直到你没法从 s 中选择字符。
从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
重复步骤 5 ，直到你没法从 s 中选择字符。
重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

请你返回将 s 中字符重新排序后的 结果字符串 。

输入：s = "aaaabbbbcccc"
输出："abccbaabccba"
解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"

[address](https://leetcode-cn.com/problems/increasing-decreasing-string)
"""


def sort_string(s: str) -> str:
    """
    桶计数:
    开一个长度为26的数组表示26个桶,先线性扫描一遍字符串,统计每个
    字母出现的次数. 只要不停从小到大和从大到小扫描,每次发现一个桶
    当中计数值不为0的时候，就把这个桶对应的字母添加到结果字符串的
    最后方,然后对计数值减一
    """
    def append_char(ret, p):
        if h[p] > 0:
            h[p] -= 1
            ret.append(chr(p + 97))

    def have_char():
        # any(iterable) 只要有一个为True, 就返回True
        return any(h[i] > 0 for i in range(26))

    # 初始化26个英文字母桶
    h = [0] * 26
    for ch in s:
        h[ord(ch) - 97] += 1

    ret = list()
    # 不断重复扫描
    while True:
        # 判断源字符串是否为空，为空退出
        if not have_char():
            break
        # 从小到大扫描加入结果字符串
        for i in range(26):
            append_char(ret, i)
        # 从大到小扫描加入结果字符串
        for i in range(26):
            append_char(ret, 25 - i)

    return ''.join(ret)


if __name__ == '__main__':
    s = "aaaabbbbcccc"
    print(sort_string(s))



















