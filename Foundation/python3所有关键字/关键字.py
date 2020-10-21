#!usr/bin/python
# -*- coding:utf8 -*-
"""
python保留字
保留字即关键字,我们不能把它们用作任何标识符名称.
Python的标准库提供了一个keyword模块,可以输出当前版本的所有关键字
keyword.iskeyword(s) 如果s是一个Python关键字则返回True
keyword.kwlist 包含解释器定义的所有关键字的序列

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
'except', 'finally', 'for', 'from', 'global', 'if', 'import',
'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
"""
import keyword


print(keyword.kwlist)






















