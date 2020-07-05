#!usr/bin/python
# -*- coding:utf8 -*-
"""
当我们使用class定义类的时候，Python解释器仅仅是扫描一下定义的语法，
然后调用type()函数创建class类。
class A(object):
    # 类属性
    role = 'student'

    # 实例方法
    def __init__(self, name):
        # 实例属性
        self.name = name

    # 类方法
    @classmethod
    def study(cls):
        pass

    # 静态方法
    @staticmethod
    def cal_student_num():
        pass
"""


# 使用type()函数定义类
# 实例方法
def __init__(self, name):
    # 实例属性
    self.name = name


# 类方法
@classmethod
def study(cls):
    pass


# 静态方法
def cal_student_num():
    pass


# 元类最大的作用不在于创建一个新的类
# class type(name, bases, dict)
A = type(
    'A',
    (object, ),
    {
        'role': 'student',
        '__init__': __init__,
        'study': study,
        'cal_student_num': cal_student_num
    }
)

a = A('小王')
print(a.role, a.name)  # student 小王

"""
小结:
使用type()函数时，如果只传入一个参数object，那么将返回该object的类型；
如果分别传入name，bases，dict这三个参数，那么type()函数将会创建一个对象；
使用class定义对象的时候，Python解释器调用type()函数来动态创建对象。
"""





























