#!usr/bin/python
# -*- coding:utf8 -*-

class User:
    # 生成User对象之前加逻辑 先调用new 后调用init
    def __new__(cls, *args, **kwargs):
        print(" in new")
        return super().__new__(cls)
    def __init__(self, name):
        print(" in init")
        self.name = name

# new 是用来控制对象的生成过程 在对象生成之前
# init是用来完善对象的
# 如果new方法不返回对象，则不会调用init函数
if __name__ == "__main__":
    user = User("bobby")