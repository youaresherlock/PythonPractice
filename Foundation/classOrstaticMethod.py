#!usr/bin/python
# -*- coding:utf8 -*-

"""
python类语法中有三种方法:实例方法/静态方法/类方法
python中实现静态方法和类方法都是依赖于python的修饰器来实现的
实例方法需要将类实例化后调用，如果使用类直接调用实例方法，需要显示地将实例作为参数传入 ClassName.func(instances)
类方法传入的第一个参数为cls,是类本身，类方法可以通过类直接调用，或通过实例直接调用
静态方法是指类中无需实例参与即可调用的方法
"""
class Foo(object):
    # 实例方法
    def instance_method(self):
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))

    # 类方法，使用@classmethod装饰器修饰
    @classmethod
    def class_method(cls):
        print("是类方法")

    # 静态方法，参数没有要求
    @staticmethod
    def static_method():
        print("是静态方法")

foo = Foo()
# 实例方法只能被实例调用。
foo.instance_method()
Foo.instance_method(foo)

print('----------')

# 类方法可以被类或者实例调用。
Foo.class_method()
foo.class_method()

print('----------')

# 静态方法可以被类或者实例调用。
Foo.static_method()
foo.static_method()

































