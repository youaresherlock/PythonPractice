#!usr/bin/python
# -*- coding:utf8 -*-

# __abs__
class Nums(object):
    def __init__(self, num):
        self.num = num

    def __abs__(self):
        return abs(self.num)

my_num = Nums(1)
print(abs(my_num))


# __add__ 数学运算
class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other_instance):
        re_vector = MyVector(self.x + other_instance.x, self.y + other_instance.y)
        return re_vector
    def __str__(self):
        return "x: {x}, y:{y}".format(x = self.x, y = self.y)

first_vec = MyVector(1, 2)
second_vec = MyVector(2, 3)
print(first_vec+second_vec)

"""
1
x: 3, y:5
"""