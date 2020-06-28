#!usr/bin/python
# -*- coding:utf8 -*-
"""
第15课 Python对象比较、拷贝
==: 比较变量所指向的值是否相等 a==b相当于a.__eq__(b)
    比如列表会重载__eq__,会去遍历列表中的元素,比较它们的顺序和值是否相等
is: 是否是同一个对象,是否指向同一个内存地址
浅拷贝和深拷贝:
浅拷贝: 只有三种操作 切片操作、工厂函数、copy.copy 只拷贝原对象内第一层对象的引用
深拷贝: 只有一种形式,copy.deepcopy 深拷贝拷贝了对象的所有元素,包括多层嵌套的元素

对于元组,使用tuple()或者切片操作符':'不会创建一份浅拷贝,相反,它会返回一个指向
相同元组的引用

浅拷贝中的元素，是原对象中子对象的引用，因此，如果原对象中的元素是可变的，
改变其也会影响拷贝后的对象，存在一定的副作用。
深度拷贝则会递归地拷贝原对象中的每一个子对象，因此拷贝后的对象和原对象互不相关。另
外，深度拷贝中会维护一个字典，记录已经拷贝的对象及其 ID，来提高效率并防止无限递归的发生。
"""
import copy


if __name__ == '__main__':
    a = 2
    b = 2
    print(a == b)
    print(a is b)
    print("id(a) = {}".format(id(a)))
    print("id(b) = {}".format(id(b)))
    # 以上只对-5至256的值有效
    a = 10000000
    b = 10000000
    print(a == b)
    print(a is b)
    print("id(a) = {}".format(id(a)))
    print("id(b) = {}".format(id(b)))
    # 对于不可变变量
    t1 = (1, 2, [3, 4])
    t2 = (1, 2, [3, 4])
    print(t1 == t2)
    print(id(t1), id(t2))
    t1[-1].append(5)
    print(t1 == t2)
    print(id(t1), id(t2))
    # 浅拷贝
    l1 = [1, 2, 3]
    l2 = list(l1)
    print(l1 == l2)
    print(l1 is l2)
    s1 = set([1, 2, 3])
    s2 = set(s1)
    print(s1, s2)
    print(s1 == s2)
    print(s1 is s2)
    # 通过切片操作
    l1 = [1, 2, 3]
    l2 = l1[:]
    print(l1 == l2)
    print(l1 is l2)
    # 使用copy函数
    l2 = copy.copy(l1)
    print(l1 == l2)
    print(l1 is l2)  # false
    # 元组的不同，返回一个指向元组的引用
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    print(t1 == t2)
    print(t1 is t2)  # true
    # 浅拷贝的副作用
    l1 = [[1, 2], (30, 40)]
    l2 = list(l1)
    l1.append(100)
    l1[0].append(3)
    print(l1)
    print(l2)
    l1[1] += (50, 60)
    print(l1)
    print(l2)
    # 深拷贝
    l1 = [[1, 2], (30, 40)]
    l2 = copy.deepcopy(l1)
    l1.append(100)
    l1[0].append(3)
    print(l1, l2)
    # 陷入无限循环的深拷贝
    x = [1]
    x.append(x)
    print(x)  # x是一个无限嵌套的列表
    y = copy.deepcopy(x)
    print(y)
    # 思考题
    # print(x == y) #报错 达到最大递归深度
    print(x is y)  # RecursionError: maximum recursion depth exceeded in comparison






















































