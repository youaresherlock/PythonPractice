#!usr/bin/python
# -*- coding:utf8 -*-
import sys

a = [1, 2, 3]

print("命令行参数如下:")
# 包含了一个Python解释器自动查找所需模块的路径的列表
print(sys.path)
# 一个包含命令行参数的列表
print(sys.argv)

# 当我们使用import语句的时候，Python解释器是怎样找到对应的文件?
# Python的搜索路径是由一系列目录名组成的，Python解释器就以此从这些目录中取寻找所引入的模块


print(sys.__name__) # sys

# dir()函数可以找到模块内定义的所有名称，以一个字符串列表的形式返回
# dir(sys)
# 没有给定参数，那么dir()函数会罗列出当前定义的所有名称
print(dir())


"""
模块导入注意的问题:
import item.subitem.subsubitem这种导入形式,除了最后一项，都必须是包，最后一项可以是模块或者是包，
但是不可以是类、函数或者变量的名字

在:file:sounds/effects/__init__.py中包含如下代码:
__all__ = ["echo", "surround", "reverse"]
这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块。
"""




