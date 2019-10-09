#!usr/bin/python
# -*- coding:utf8 -*-

class Duck:
    def quack(self):
        print("gua gua")

class Person:
    def quack(self):
        print("我是人类，但我也会gua gua gua")

def in_the_forest(duck):
    duck.quack()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)
    print(type(donald))
    print(type(john))
    print(isinstance(donald, Duck))
    print(isinstance(john, Person))

game()