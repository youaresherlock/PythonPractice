#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一个仅由数字 6 和 9 组成的正整数 num。
你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。
请返回你可以得到的最大数字。

输入：num = 9669
输出：9969
解释：
改变第一位数字可以得到 6669 。
改变第二位数字可以得到 9969 。
改变第三位数字可以得到 9699 。
改变第四位数字可以得到 9666 。
其中最大的数字是 9969 。

[address](https://leetcode-cn.com/problems/maximum-69-number)
"""


def maximum_69_number(num: int) -> int:
    # num_string = list(str(num))
    # for i in range(len(num_string)):
    #     if num_string[i] == '6':
    #         num_string[i] = '9'
    #         break
    #
    # return int(''.join(num_string))

    # 只需要找到第一位是6的数字,然后替换成9, 找不到不翻转
    # str.replace(old, new[,count])会从头开始寻找old,然后用new替换count次
    return int(str(num).replace('6', '9', 1))


if __name__ == '__main__':
    num = 9669
    print(maximum_69_number(num))












