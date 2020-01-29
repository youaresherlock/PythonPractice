#!usr/bin/python
# -*- coding:utf8 -*-
# @Author: Clarence
# @Date:   2020-01-20 18:41:46
# @Last Modified by:   Clarence
# @Last Modified time: 2020-01-21 09:44:19


def mybin(num): # 10进制->2进制 
	if num == 0:
		return 0 
	res = [] 
	while num:
		num, rem = divmod(num, 2) # 2 -> 62
		res.append(str(rem))
	return ''.join(reversed(res))

print(mybin(10))

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def encode(num):
	if num == 0:
		return CHARS[0]
	res = [] 
	while num:
		num, rem = divmod(num, len(CHARS)) # 62
		res.append(CHARS[rem])
	return ''.join(reversed(res))

print(encode(0))