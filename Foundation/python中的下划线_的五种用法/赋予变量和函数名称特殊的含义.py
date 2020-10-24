                                                                                                         #!usr/bin/python
# -*- coding:utf8 -*-
"""
下划线可能最常用于“命名”。PEP8是Python的约定准则，它介绍了以下4种命名情况：



_single_leading_underscore (首部单下划线)



此约定用于声明模块中的私有变量、函数、方法和类。在

from module import *中，任何具有此约定的内容都将被忽略。



然而，当然，Python不支持真正的私有，所以我们不能强制一些私有的东西，也可以直接从其他模块调用它。所以有时我们会说“弱内部使用指标”。



_internal_name = 'one_nodule' # private variable
_internal_version = '1.0' # private variable

class _Base: # private class
    _hidden_factor = 2 # private variable

    def __init__(self, price):
        self._price = price

    def _double_price(self): # private method
        return self._price * self._hidden_factor

    def get_double_price(self):
        return self._double_price()


single_trailing_underscore_ (尾部单下滑线)



此约定可用于避免与Python关键字或内置项发生冲突。你可能不经常使用它。



Tkinter.Toplevel(master, class_='ClassName') # Avoid conflict with 'class' keyword

list_ = List.objects.get(1) # Avoid conflict with 'list' built-in type


__double_leading_underscore (首部双下划线)



这是语法而不是约定的。双下划线将”矫正“类的属性名，以避免类之间的属性名冲突。(所谓的“矫正”是指编译器或解释器用一些规则修改变量或函数名，而不是按原样使用)




Python的矫正规则是在属性名前面加上双下划线声明“_ClassName”。也就是说，如果你在一个类中编写了一个名为“__method”的方法，那么这个名字将会在“_ClassName__method”的表单中被矫正。



class A:
    def _single_method(self):
        pass
    def __double_method(self): # for mangling
        pass
class B(A):
    def __double_method(self): # for mangling
        pass


因为用双下划线命名的属性会像上面那样矫正，所以我们不能用“ClassName.__method”访问它。有时，有些人使用它就像真正的私人使用这些功能，但它不是私人的，也不推荐这样做。



__double_leading_and_trailing_underscore__ (首尾部双下划线)



这个约定用于特殊的变量或方法(所谓的“魔法方法”)，如:__init__， __len__。这些方法提供了特殊的语法特征或做了特殊的事情。例如，__file__表示Python文件的位置，当a==b表达式被执行时，__eq__被执行。



class A:
    def __init__(self, a): # use special method '__init__' for initializing
        self.a = a

    def __custom__(self): # custom special method. you might almost do not use it
        pass
"""