#!usr/bin/python
# -*- coding:utf8 -*-

# 类也是对象，  type创建类的类

# 如何动态创建一个类
def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"
        return Company

# type 动态创建类
# User = type("User", (), {"name": "user"})

def say(self):
    return "i am user"
    # return self.name

class BaseClass:
    def answer(self):
        return "i am baseclass"

class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
# 什么是元类， 元类是创建类的类 对象<-class(对象)<-type
# type是元类
class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "user"

# python中类的实例化过程， 会首先寻找metaclass属性，通过metaclass去创建user类对象
# type去创建类对象， 实例

if __name__ == "__main__":
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(my_obj)

    User = type("User", (BaseClass,), {"name": "user", "say": say})
    my_obj = User()
    print(my_obj.say())
    print(my_obj.answer())


































































