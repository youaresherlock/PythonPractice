#!usr/bin/python
# -*- coding:utf8 -*-

# re.match(pattern, string, flags = 0)
# pattern 匹配的正则表达式 string 要匹配的字符串 flags 标志位
import re

line = "Cats are smarter than dogs"
# re.M Multi-line regular expression  re.I ignore Case忽略大小写
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print("matchObj.group(): ", matchObj.group())
    print(f"matchObj.group(1): {matchObj.group(1)}, matchObj.group(2): {matchObj.group(2)}")
else:
    print("No match!")

# re.search(pattern, string, flags = 0)扫描整个字符串并返回第一个成功的匹配 返回一个匹配的对象，否则返回None
print(re.search("www", "www.runoob.com").span()) # 在起始位置匹配

"""
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，
则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配
"""

"""
检索和替换
Python的re模块提供了re.sub用于替换字符串中的匹配项
re.sub(pattern, repl, string, count = 0, flags = 0)
pattern: 正则中的模式字符串
repl: 替换的字符串，也可以为一个函数
string: 要被查找替换的原始字符串
count: 模式匹配后替换的最大次数,默认0表示替换所有匹配
flags: 编译时用的匹配模式，数字形式
"""
phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', '', phone)
print("电话号码: ", num)

# 移除非数字内容
num = re.sub(r'\D', "", phone)
print("电话号码: ", num)

def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = "A23G4HFD567"
print(re.sub('(?P<value>\d+)', double, s))

# findall(string[,pos[,endpos]])
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
# match和search是匹配一次findall匹配所有
pattern = re.compile(r'\d+')
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1, result2)

it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group())

# re.split(pattern, string[, maxsplit = 0, flags = 0)
# 按照能够匹配的子串将字符串分割后返回列表,它的使用形式如下:
print(re.split("\W+", 'runoob, runoob, runoob.'))


import os
print(os.environ)
















