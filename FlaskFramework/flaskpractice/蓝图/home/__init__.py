#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Blueprint

# 1. 创建蓝图对象
# 细节1: 可以通过url_prefix参数给蓝图定义的路由添加统一的URL资源段前缀
home_blu = Blueprint("home_b", __name__, url_prefix='/home')


# 细节3: 蓝图也可以设置请求钩子, 只有访问该蓝图定义的路由时才会触发 局部监听
@home_blu.before_request
def home_prepare():
    print('home_prepare')


# 4. 让视图文件和主程序建立关联
# 遇到ImportError, 需要查看和调整代码的执行顺序
from . import views