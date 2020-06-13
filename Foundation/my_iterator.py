#!usr/bin/python
# -*- coding:utf8 -*-
"""
迭代器协议:
把一个类作为一个迭代器使用需要在类中实现两个方法__iter__()与__next__()
__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__()
方法并通过 StopIteration 异常标识迭代的完成。
"""


class MyNumbers(object):
    def __iter__(self):
        self.a = 1
        print("__iter__被调用了")
        return self

    def __getitem__(self, item):
        print("__getitem__被调用了")
        if item <= 20:
            return item
        else:
            raise StopIteration

    def __next__(self):
        print("__next__被调用了")
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_class = MyNumbers()
for x in my_class:
    print(x)
# my_iter = iter(my_class)
# for x in my_iter:
#     print(x)



































