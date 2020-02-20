#!usr/bin/python
# -*- coding:utf8 -*-

# __getattr__, __getattribute__
# __getattr__就是在查找不到属性的时候调用

from datetime import date
class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __getattr__(self, item):
        print("not find attr")
        return item.upper()

    def __getattribute__(self, item):
        return "bobby"


if __name__ == "__main__":
    user = User("bobby", date(year=1987, month=1, day=1))
    print(user.age)



