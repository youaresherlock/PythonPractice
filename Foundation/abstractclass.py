#!usr/bin/python
# -*- coding:utf8 -*-

"""
    如果说类是从一堆对象中抽取相同的内容而来的, 那么抽象类就是从一堆类中抽取
相同的内容而来的, 内容包括数据属性和函数属性
    从实现角度来看,抽象类与普通类的不同之处在于: 抽象类中有抽象方法, 该类不能被实例化,
只能被继承,且子类必须实现抽象方法.
"""
import abc  # 利用abc模块实现抽象类


class AllFile(metaclass=abc.ABCMeta):
    all_type = 'file'

    @abc.abstractmethod
    def read(self):
        """子类必须定义读功能"""
        pass

    @abc.abstractmethod
    def write(self):
        """子类必须定义写功能"""
        pass


class Txt(AllFile):  # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')


class Sata(AllFile):  # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')


class Process(AllFile):  # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')


txt = Txt()

sata = Sata()

process_file = Process()

# 这样大家都是被归一化了,也就是一切皆文件的思想
txt.read()
sata.write()
process_file.read()

print(txt.all_type)
print(sata.all_type)
print(process_file.all_type)







































