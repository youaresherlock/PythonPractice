#!usr/bin/python
# -*- coding:utf8 -*-

class Sample():
    def __enter__(self):
        print("in __enter__")
        return 'Foo'

    def __exit__(self, exc_type, exc_val, exc_tbl):
        # exc_type: 错误的类型
        # exc_val: 错误类型对应的值
        # exc_tbl: 代码中错误发生的位置
        print("in __exit__")

def get_sample():
    return Sample()

# 紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值
# 给as后面的变量。当with后面的代码块全部被执行完之后， 将调用前面返回对象的exit()方法
with get_sample() as sample:
    print("sample:", sample)
