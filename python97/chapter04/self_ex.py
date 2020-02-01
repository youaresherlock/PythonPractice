#!usr/bin/python
# -*- coding:utf8 -*-

# 自省是通过一定的机制查询到对象的内部结构
class Person:
    """
    人
    """
    name = "user"

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

if __name__ == "__main__":
    user = Student("慕课网")

    # 通过__dict__查询属性
    print(user.__dict__)
    user.__dict__["school_addr"] = "北京市"
    print(user.school_addr)
    print(user.__dict__)
    print(Person.__dict__)
    print(user.name)
    # dir比__dict__更加强大，只有属性名称，没有属性的值
    print(dir(user))




























