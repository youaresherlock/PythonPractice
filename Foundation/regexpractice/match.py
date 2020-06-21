"""
re.compile可以将正则表达式进行预编译, 用来提升性能
模块函数会对已编译的对象进行缓存, 但使用re.compile可以减少查询缓存的时间
"""
import re


# 从字符串的起始部分对模式进行匹配,返回匹配对象
match_object = re.match("foo", "food on the table")
if match_object is not None:
    print(match_object.group(), match_object.groups())


























9