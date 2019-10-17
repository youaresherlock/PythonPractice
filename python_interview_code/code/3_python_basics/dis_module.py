#!usr/bin/python
# -*- coding:utf8 -*-

"""
The dis module supports the analysis of CPython bytecode by disassembling it.
The CPython bytecode which this module takes as an input is defined in the
file Include/opcode.h and used by the compiler and the interpreter.
"""

import dis

def update_list(l):
    l[0] = 1 # 原子操作，不用担心线程安全问题

dis.dis(update_list)

def incr_list(l):
    l[0] += 1 # 不是原子操作

dis.dis(incr_list)

"""
 13           0 LOAD_CONST               1 (1)
              2 LOAD_FAST                0 (l)
              4 LOAD_CONST               2 (0)
              6 STORE_SUBSCR
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
 18           0 LOAD_FAST                0 (l)
              2 LOAD_CONST               1 (0)
              4 DUP_TOP_TWO
              6 BINARY_SUBSCR
              8 LOAD_CONST               2 (1)
             10 INPLACE_ADD
             12 ROT_THREE
             14 STORE_SUBSCR
             16 LOAD_CONST               0 (None)
             18 RETURN_VALUE
"""