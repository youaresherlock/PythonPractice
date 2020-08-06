#!usr/bin/python
# -*- coding:utf8 -*-
"""
 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 
S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有
多少是宝石。
J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，
因此"a"和"A"是不同类型的石头。

输入: J = "aA", S = "aAAbbbb"
输出: 3

链接：https://leetcode-cn.com/problems/jewels-and-stones
"""


def num_jewel_is_in_stones(J: str, S: str) -> int:
    # result = 0
    # for j in J:
    #     result += S.count(j)
    #
    # return result
    return sum(map(lambda x: x in J, S))


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    print(num_jewel_is_in_stones(J, S))















