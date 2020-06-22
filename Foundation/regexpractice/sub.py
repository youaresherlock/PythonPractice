#!usr/bin/python
# -*- coding:utf8 -*-
"""
sub(regex, replace_str, string): 将某字符串中所有匹配正则表达式
的部分进行某种形式的替换, 返回替换后的字符串
"""
import re
print(re.sub("[ae]", "X", "abcdef"))  # XbcdXf
print(re.subn("[ae]", "X", "abcdef"))  # ('XbcdXf', 2)
print(re.sub(r"(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})", r"\2/\1/\3", "2/20/1991"))
data = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA',
)

for datum in data:
    print(re.split(r', |(?= (?:\d{5}|[A-Z]{2}))', datum))
