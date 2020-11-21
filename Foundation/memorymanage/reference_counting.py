#!usr/bin/python
# -*- coding:utf8 -*-
"""
内存管理机制:
    1. 小整数对象池 范围[-5, 256]
    2. 大整数池 默认创建出来,池内为空的，创建一个就会往池中存储一个
    3. 字符串intern机制(字符串驻留机制) 每个单词(字符串), 不夹杂空格或者其他符号,
    默认开启intern机制, 共享内存, 靠引用计数决定是否销毁,包含大小写英文字母和数字以及下划线

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
标记清除(Mark-Sweep):
    它分为两个阶段：第一阶段是标记阶段，GC会把所有的『活动对象』打上标记，
第二阶段是把那些没有标记的对象『非活动对象』进行回收。
那么GC又是如何判断哪些是活动对象哪些是非活动对象的呢？
对象之间通过引用（指针）连在一起，构成一个有向图，
对象构成这个有向图的节点，而引用关系构成这个有向图的边。
从根对象（root object）出发，沿着有向边遍历对象，可达的（reachable）对象标记为活动对象，不
可达的对象就是要被清除的非活动对象。根对象就是全局变量、调用栈、寄存器。
分代回收:
分代回收是一种以空间换时间的操作方式，Python将内存根据对象的存活时间划分为不同的集合，每
个集合称为一个代，Python将内存分为了3“代”，分别为年轻代（第0代）、中年代（第1代）、
老年代（第2代），他们对应的是3个链表，它们的垃圾收集频率与对象的存活时间的增大而减小。
新创建的对象都会分配在年轻代，年轻代链表的总数达到上限时，Python垃圾收集机制就会被触发，
把那些可以被回收的对象回收掉，而那些不会回收的对象就会被移到中年代去，依此类推，
老年代中的对象是存活时间最久的对象，甚至是存活于整个系统的生命周期内。同时，
分代回收是建立在标记清除技术基础之上。分代回收同样作为Python的辅助垃圾收集技术处理
那些容器对象
"""


import gc
import sys


class Student(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("__del__")


# gc.disable()  # 关闭自动垃圾回收
s1 = Student('clarence')
print(sys.getrefcount(s1))  # sys.getrefcount引用了一次,因此引用计数是2
print(gc.get_count())  # collections count
print(gc.get_threshold())  # 分代回收0、1、2代回收的阈值

























