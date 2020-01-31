# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2020-01-31 14:28:43
# @Last Modified by:   Clarence
# @Last Modified time: 2020-01-31 14:32:06
from collections import deque 

def person_is_seller(name):
	return name[-1] == 'm'

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
	search_deque = deque() 
	search_deque += graph[name]
	searched = [] 
	while search_deque:
		person = search_deque.popleft() 
		if person not in searched:
			if person_is_seller(person):
				print(person + " is a mongo seller!")
				return True 
			else:
				search_deque += graph[person]
				searched.append(person)
	return False 

search("you")