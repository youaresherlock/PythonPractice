#!usr/bin/python
# -*- coding:utf8 -*-
import sys
import traceback


try:
    x = int(input("请输入一个被除数："))
    print("30除以", x, "等于", 30/x)
except Exception:
    # 返回一个元祖,第一个是发生的异常类,第二个是异常类的实例,第三个为一个traceback对象
    # print(sys.exc_info())
    traceback.print_tb(sys.exc_info()[2])
    print("其他异常...")