#!usr/bin/python
# -*- coding:utf8 -*-
"""
内存管理机制:
    1. 小整数对象池 范围[-5, 256]
    2. 大整数池 默认创建出来,池内为空的，创建一个就会往池中存储一个
    3. 字符串intern机制(字符串驻留机制) 每个单词(字符串), 不夹杂空格或者其他符号,
    默认开启intern机制, 共享内存, 靠引用计数决定是否销毁

python中的内存管理机制:
    garbage collection:
    1. 引用计数为主
    python里外物皆对象, 它们的核心就是一个结构体: PyObject
    typedef stuct_object{
        int ob_refcnt;
        struct_typeobject *ob_type;
    } PyObject;
    PyObject是每个对象必有的内容, 其中ob_refcnt就是作为引用计数, 当一个对象有新的引用时,
    它ob_refcnt就会增加,当引用它的对象被删除, 它的ob_refcnt就会减少. 当引用计数为0时, 该对象
    生命就结束了.
    优点:
        1. 简单
        2. 实时性: 一旦没有引用,内存就直接释放了, 不用像其它机制等到特定时机.
    缺点:
        1.维护引用计数消耗资源
        2. 循环引用的问题无法解决
        sys.getrefcount(obj)获取对象的引用计数
gc.enable(): 开启自动垃圾回收机制
gc.disable(): 关闭自动垃圾回收机制
gc.isenabled(): 如果垃圾回收是开启的返回True
gc.collect(generation=2): 手动垃圾回收
gc.set_threshold(threshold0[, threshold1[, threshold2]]):
    et the garbage collection thresholds (the collection frequency).
    Setting threshold0 to zero disables collection.
    The GC classifies objects into three generations depending on how many
    collection sweeps they have survived. New objects are placed in the youngest
    generation (generation 0). If an object survives a collection it is moved
    into the next older generation. Since generation 2 is the oldest
    generation, objects in that generation remain there after a collection
    2. 标记清除和分代回收为辅
"""


import gc
import sys


class Student(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("__del__")


s1 = Student('clarence')
print(sys.getrefcount(s1))

























