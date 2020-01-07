# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2020-01-07 18:02:10
# @Last Modified by:   Clarence
# @Last Modified time: 2020-01-07 18:03:07

# 递归函数计算列表元素数
def count(list):
	if list == []:
		return 0 
	return 1 + count(list[1:])