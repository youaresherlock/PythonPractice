#!usr/bin/python
# -*- coding:utf8 -*-
"""
assert:
Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
assert expression [, arguments]
等价于:
if __debug__:
    if not expression:
        raise AssertionError(arguments)
这里的__debug__是一个常数。如果 Python 程序执行时附带了-O这个选项，
比如Python test.py -O，那么程序中所有的 assert 语句都会失效，
常数__debug__便为 False；反之__debug__则为 True。

不过，需要注意的是，直接对常数__debug__赋值是非法的，
因为它的值在解释器开始运行时就已经决定了，中途无法改变。
"""
import sys
assert 'linux' in sys.platform, "该代码只能在 Linux 下执行"

