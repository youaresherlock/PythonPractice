#!usr/bin/python
# -*- coding:utf8 -*-
"""
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。

例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。

对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。

那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
input:
    输入仅一行，包含多个单词，之间用逗号分隔
output:
    输出一个整数，表示对给定单词列表进行编码的最小字符串长度
"""

# 单词的压缩编码
num_list = input().split(',')
n_set = set(num_list)  # {}
for word in num_list:
    for i in range(1, len(word)):
        # 移除指定的集合元素
        n_set.discard(word[i:])
result = sum(len(i) + 1 for i in n_set)
print(result)

























