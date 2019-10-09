#!usr/bin/python
# -*- coding:utf8 -*-

'''
python3可以直接使用super().__init__(value)代替python2中的super(Class, self).__init__(value)
在python3中可以使用__class__准确拿到当前类
super(__class__, self).__init__(value)
'''

class Base(object):
    def hello(self):
        print('hello')

class C(Base):
    def hello(self):
        # py2
        return super(C, self).hello()

c = C()
c.hello()


class C2(Base):
    def hello(self):
        # py3
        print(__class__ == C2)
        return super().hello()
c2 = C2()
c2.hello()

"""
hello
True
hello
"""