#!usr/bin/python
# -*- coding:utf8 -*-
"""
python2的语法
___metaclass__属性自定义元类
可以在定义一个类的时候为其添加__metaclass__属性.Python会在类的定义中寻找__metaclass__
属性,如果找到了,Python就会用它来创建类,如果没有找到,就会用内键的type来创建这个类
"""


class StudentMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['school'] = 'stanford'
        attrs['job'] = 'student'
        print("helo")
        return super().__new__(cls, name, bases, attrs)


class Student(metaclass=StudentMetaClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age

"""
python2的语法
class Student(object):
    __metaclass__ = StudentMetaclass
"""


s = Student("clarence", 18)
print(Student.__dict__)
print(s.__dict__)  # {'name': 'clarence', 'age': 18}
print(Student.school, Student.job)

























