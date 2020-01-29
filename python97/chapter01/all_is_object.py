#!usr/bin/python
# -*- coding:utf8 -*-

def ask(name="bobby"):
    print(name)

class Person:
     def __init__(self):
         print("bobby1")

# my_func = ask
# my_func("bobby")

def decorator_func():
    print("dec start")
    return ask
my_ask = decorator_func()
my_ask("tom")

# obj_list = []
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
#     print(item())

# my_class = Person
# my_class()