# -*- coding: utf-8 -*-
# 列表元素之和-递归写法 
def sum(list):
	if list == []:
		return 0 
	return list[0] + sum(list[1:])
