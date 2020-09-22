#!usr/bin/python
# -*- coding:utf8 -*-
from home import home_blu
from flask import url_for


# 2. 使用蓝图对象来定义路由
@home_blu.route('/')
def index():

    return "index"


@home_blu.route('/demo')
def demo():
    # 细节2: 蓝图定义的路由,其函数标记为蓝图名.函数名
    url = url_for('home_b.demo')  # /home/demo
    print(url)
    return 'demo'
