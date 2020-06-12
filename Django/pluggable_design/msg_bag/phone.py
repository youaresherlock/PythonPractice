#!usr/bin/python
# -*- coding:utf8 -*-


# Phone 短信
class Phone:
    def __init__(self, name):
        self.name = name

    # 鸭子类型
    def send_msg(self, content):
        print('Phone今天是10月的最后一天，请好好{}'.format(content))
