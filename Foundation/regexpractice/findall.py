#!usr/bin/python
# -*- coding:utf8 -*-
"""
findall: 查询字符串中某个正则表达式模式全部的非重复出现情况
返回包含所有成功的匹配部分的列表
"""
import re
result = re.findall("car", "carry the barcardi to the car")
print(result)
