# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2020-01-19 11:41:26
# @Last Modified by:   Clarence
# @Last Modified time: 2020-01-19 11:44:26
voted = {} 
def check_voter(name):
	if voted.get(name):
		print("kick them out!")
	else:
		voted[name] = True 
		print("let them vote!")

check_voter("tom")
check_voter("mike")
check_voter("mike")
