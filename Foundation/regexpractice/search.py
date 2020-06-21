"""
search: 在一个字符串中查找模式, 第一次出现匹配的情况
"""
import re


match_object = re.search("foo", "seafood")
if match_object is not None:
    print(match_object.group())

