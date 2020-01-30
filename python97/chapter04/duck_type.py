#!usr/bin/python
# -*- coding:utf8 -*-

class Cat(object):
    def say(self):
        print("I am a cat")

class Dog(object):
    def say(self):
        print("I am a dog")

    def __getitem__(self, item):
        return "bobby"

class Duck(object):
    def say(self):
        print("I am a duck")

# animal = Cat
# animal().say()
animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


dog = Dog()
a = ["bobby1", "bobby2"]

b = ["bobby2", "bobby"]
name_tuple = ["bobby3", "bobby4"]
name_set = set()
name_set.add("bobby5")
name_set.add("bobby6")
a.extend(dog) # extend(self, iterable)
print(a)
