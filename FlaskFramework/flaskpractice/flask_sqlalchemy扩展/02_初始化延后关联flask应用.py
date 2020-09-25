#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_dict


# 方式2: 初始化组件对象, 延后关联Flask应用
db = SQLAlchemy()


def create_app(config_type):
    """工厂函数"""

    # 创建应用
    flask_app = Flask(__name__)
    # 加载配置
    config_class = config_dict[config_type]
    flask_app.config.from_object(config_class)

    # 关联flask应用
    db.init_app(flask_app)

    return flask_app
