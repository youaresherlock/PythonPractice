# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2020-01-07 18:03:36
# @Last Modified by:   Clarence
# @Last Modified time: 2020-01-07 18:05:24

# 递归计算列表中最大元素 
def max(list):
	if len(list) == 2:
		return list[0] if list[0] > list[1] else list[1]
	sub_max = max(list[1:])
	return list[0] if list[0] > sub_max else sub_max