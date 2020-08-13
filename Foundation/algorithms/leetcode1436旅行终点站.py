#!usr/bin/python
# -*- coding:utf8 -*-
"""
给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] =
[cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。请你找出这次
旅行的终点站，即没有任何可以通往其他城市的线路的城市。
题目数据保证线路图会形成一条不存在循环的线路，因此只会有一个旅行终点站。


输入：paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
输出："Sao Paulo"
解释：从 "London" 出发，最后抵达终点站 "Sao Paulo" 。本次旅行的路线是 "London" -> "New York" -> "Lima" -> "Sao Paulo"

[address](https://leetcode-cn.com/problems/destination-city)
"""
from typing import List


def dest_city(paths: List[List[str]]):
    # 遍历一次建立所有城市与出发城市的两个集合，两个集合做差即是终点城市
    # all_city = set()
    # begin_city = set()
    # for path in paths:
    #     all_city.add(path[0])
    #     all_city.add(path[1])
    #     begin_city.add(path[0])
    # return (all_city - begin_city).pop()

    # 如果目的地不是出发地,则返回该目的地
    possible_city = [i[1] for i in paths]
    impossible_city = [i[0] for i in paths]

    for city in possible_city:
        if city not in impossible_city:
            return city
    # return [path[1] for path in paths if path[1] not in [path[0] for path in paths]][0]


if __name__ == '__main__':
    paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    print(dest_city(paths))























