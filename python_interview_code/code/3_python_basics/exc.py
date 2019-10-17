#!usr/bin/python
# -*- coding:utf8 -*-

class MyException(Exception):
    pass

try:
    raise MyException('my exception')
# exception MyException as e:
except Exception as e:
    print(e)