#!usr/bin/python
# -*- coding:utf8 -*-

class people:
    # 定义基本属性
    job = "gopher"
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        # 注意__xx是私有变量，self._weight外部是可以直接访问到的
        self.__weight = weight  # 私有变量，翻译成了self._A__name = "python"
    def speak(self):
        print("%s 说: 我 %d 岁. " %(self.name, self.age))


class student(people):
    grade = '99'
    def __init__(self, name, age, weight, grade):
        # 调用父类的构造函数 子类中需要父类的构造方法就需要显示地调用父类的构造方法，或者不重写父类的构造方法
        people.__init__(self, name, age, weight)
        self.grade = grade
    # override
    def speak(self):
        print("{}说: 我{}岁了.我在读{}年级".format(self.name, self.age, self.grade))
        # 加上下面报错 AttributeError: 'student' object has no attribute '_student__weight'
        # print(self.__weight)

s = student("clarece", "25", "140", "9")
s.speak()
# 当实例属性和类属性重名时，实例属性优先级高，将会屏蔽对类属性的访问
print(student.grade, s.grade) # 分别是类变量和实例的成员变量
print(s._people__weight)  #通过这种方式，在外面也能够访问“私有”变量；这一点在调试中是比较有用的
print(student.job)























