#!/usr/bin/python
# -*- coding:utf-8 -*-
from typing import List


def change_ranking(base_scores: List[int], ranks: List[List[int]]) -> int:

    def compute_honor_list(current_taps):
        numbers = []
        max_number = max(current_taps)
        for index, number in enumerate(current_taps):
            if number == max_number:
                numbers.append(index)

        return numbers

    count = 0
    current_taps = base_scores
    honor_list = compute_honor_list(current_taps)

    ranks_mapping = dict()
    for item in ranks:
        if item[0] not in ranks_mapping:
            ranks_mapping[item[0]] = []

        ranks_mapping[item[0]].append([item[1], item[2]])

    max_week = 0
    for rank in ranks:
        if max_week < rank[0]:
            max_week = rank[0]

    for week in range(1, max_week + 1):
        if week in ranks_mapping:
            for item in ranks_mapping[week]:
                current_taps[item[0]] += item[1]
        honor = compute_honor_list(current_taps)
        if honor != honor_list:
            count += 1

    return count


if __name__ == '__main__':
    base_scores = [6, 7, 6, 5, 9]
    ranks = [[1, 4, -1], [3, 2, 3], [3, 3, -2], [1, 1, 1], [4, 0, 1]]
    print(change_ranking(base_scores, ranks))