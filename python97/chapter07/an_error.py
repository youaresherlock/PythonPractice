#!usr/bin/python
# -*- coding:utf8 -*-

class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        print(id(staffs))
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)

def add(a, b):
    a += b
    return a

if __name__ == "__main__":
    # a = 1
    # b = 2
    # c = add(a, b)
    # print(c)
    # print(a, b)

    # a = [1, 2]
    # b = [3, 4]
    # c = add(a, b)
    # print(c)
    # print(a, b)
    # [1, 2, 3, 4]
    # [1, 2, 3, 4][3, 4]

    # a = (1, 2)
    # b = (3, 4)
    # c = add(a, b)
    # print(c)
    # print(a, b)
    # (1, 2, 3, 4)
    # (1, 2)(3, 4)

    com1 = Company("com1", ["bobby1", "bobby2"])
    com1.add("bobby3")
    com1.remove("bobby1")
    print(com1.staffs)
    # ['bobby2', 'bobby3']

    com2 = Company("com2")
    com2.add("bobby")
    print(com2.staffs)
    # ['bobby']

    com3 = Company("com3")
    com3.add("bobby5")
    print(com2.staffs)
    print(com3.staffs)
    # ['bobby', 'bobby5']
    # ['bobby', 'bobby5']
    print(com2.staffs is com3.staffs) # True

























