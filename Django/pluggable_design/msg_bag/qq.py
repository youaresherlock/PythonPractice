#!usr/bin/python
# -*- coding:utf8 -*-
# 1.我们先用面向对象来写着三个发消息的共功能
# 面向对象的鸭子类型
# 只要长得像，就是鸭子类型
# 就是有很多个类，但是这些个类都具有同样的方法名，但是呢？它的方法名实现的功能不一样，就是鸭子类型


# QQ 消息
class QQ:
    # 实例化类的时候触发
    def __init__(self, name):
        self.name = name

    # 对象的绑定方法
    # 也是鸭子类型的方法
    def send_msg(self, content):
        print('QQ今天是10月的最后一天，请好好{}'.format(content))