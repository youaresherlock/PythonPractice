#!usr/bin/python
# -*- coding:utf8 -*-
"""
查找输入一组数中的所有众数排序后的中位数
"""


def compute_middle_number(message):
    message.sort()
    message_dict = dict.fromkeys(message, 0)
    for item in message:
        message_dict[item] += 1
    max_value = max(message_dict.values())
    many_numbers = [key for key, value in message_dict.items() if value == max_value]
    length = len(many_numbers)
    if length % 2 == 1:
        pivot = (length - 1) // 2
        result = many_numbers[pivot]
    else:
        pivot = length // 2
        result = (many_numbers[pivot - 1] + many_numbers[pivot]) // 2

    return result


if __name__ == '__main__':
    message = list(map(int, input().split()))
    print(compute_middle_number(message))























