#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
from typing import List


def get_similar_str(str_list: List[str], target: str) -> int:
    result = 0
    table = 'abcdefghijklmnopqrstuvwxyz'

    def get_model(strings):
        target_model = []
        mapping = dict.fromkeys(table)
        for index, number in enumerate(strings):
            if mapping[number] is None:
                mapping[number] = []
            mapping[number].append(index)

        for string in strings:
            if len(mapping[string]) != 0:
                target_model.append(mapping[string])

        return target_model

    model = get_model(target)
    for item in str_list:
        if model == get_model(item):
            result += 1

    return result


if __name__ == '__main__':
    strList =["bcde","jkuv","ijtt","kggt","efzy","mmmm","dhfa"]
    target = "dhfa"
    print(get_similar_str(strList, target))