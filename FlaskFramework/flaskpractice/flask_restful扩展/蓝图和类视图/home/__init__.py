#!usr/bin/python
# -*- coding:utf8 -*-
# user/__init__.py
from flask import Blueprint
from flask_restful import Api
from home.views import DemoResource

# 1.创建蓝图对象
home_blu = Blueprint('user', __name__, url_prefix='/user')

# 2.创建蓝图对应的api对象
user_api = Api(home_blu)

# 3.添加类视图
user_api.add_resource(DemoResource, '/')