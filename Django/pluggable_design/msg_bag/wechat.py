#!usr/bin/python
# -*- coding:utf8 -*-


# 微信 消息
class Wechat:
    # 对象实例化的时候触发
    def __init__(self, name):
        self.name = name

    # 鸭子类型的方法，对象的绑定方法
    def send_msg(self, content):
        print('Wechat今天是10月的最后一天，请好好{}'.format(content))