#!usr/bin/python
# -*- coding:utf8 -*-
"""
在介绍 with as 语句时讲到，该语句操作的对象必须是上下文管理器。那么，到底什么是上下文管理器呢？

简单的理解，同时包含 __enter__() 和 __exit__() 方法的对象就是上下文管理器。也就是说，上下文管理器必须实现如下两个方法：
__enter__(self)：进入上下文管理器自动调用的方法，该方法会在 with as 代码块执行之前执行。如果 with 语句有 as子句，那么该方法的返回值会被赋值给 as 子句后的变量；该方法可以返回多个值，因此在 as 子句后面也可以指定多个变量（多个变量必须由“()”括起来组成元组）。
__exit__（self, exc_type, exc_value, exc_traceback）：退出上下文管理器自动调用的方法。该方法会在 with as 代码块执行之后执行。如果 with as 代码块成功执行结束，程序自动调用该方法，调用该方法的三个参数都为 None：如果 with as 代码块因为异常而中止，程序也自动调用该方法，使用 sys.exc_info 得到的异常信息将作为调用该方法的参数。

当 with as 操作上下文管理器时，就会在执行语句体之前，先执行上下文管理器的 __enter__() 方法，然后再执行语句体，最后执行 __exit__() 方法。
"""


# 基于类的上下文管理器
class FileManager:
    def __init__(self, name, mode):
        print('calling __init__ method')
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print('calling __enter__ method')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('calling __exit__ method')
        if self.file:
            self.file.close()


with FileManager('test.txt', 'w') as f:
    print('ready to write to file')
    f.write('hello world')


