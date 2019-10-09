#!usr/bin/python
# -*- coding:utf8 -*-

# Chained exceptions
import shutil

def mycopy(source, desc):
    try:
        shutil.copy2(source, desc)
    except OSError: # python2里 raise 会丢失原来的traceback信息
        # raise from 保留之前异常栈信息
        raise NotImplementedError("automatic sudo injection") from OSError

mycopy('old', 'new')
