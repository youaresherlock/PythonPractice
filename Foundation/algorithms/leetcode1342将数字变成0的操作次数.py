#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。
如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。

输入：num = 14
输出：6
解释：
步骤 1) 14 是偶数，除以 2 得到 7 。
步骤 2） 7 是奇数，减 1 得到 6 。
步骤 3） 6 是偶数，除以 2 得到 3 。
步骤 4） 3 是奇数，减 1 得到 2 。
步骤 5） 2 是偶数，除以 2 得到 1 。
步骤 6） 1 是奇数，减 1 得到 0 。

[address](https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero)
"""


def number_of_steps(num: int) -> int:
    binary = bin(num)  # 0bxxx
    print(binary)
    # 有多少个1就减去多少1，二进制位长度减一的位数就是除2的次数
    # (举个例子比如14,2^3=8且最接近14,因此要除3次)
    return len(binary) + binary.count('1') - 3


if __name__ == '__main__':
    num = 14
    print(number_of_steps(num))























