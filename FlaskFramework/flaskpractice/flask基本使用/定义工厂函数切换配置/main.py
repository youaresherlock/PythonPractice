#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask, current_app, Config
from config import config_dict


# 工厂函数: 根据参数需求, 内部封装对象的创建过程
def create_app(config_type):
    """封装应用的创建过程"""

    # 创建应用
    flask_app = Flask(__name__)

    # 根据配置类型取出对应的配置子类
    config_class = config_dict[config_type]

    # 加载普通配置
    flask_app.config.from_object(config_class)

    return flask_app


# 创建应用对象
app = create_app('dev')


"""
Basically this example::

            @app.route('/')
            def index():
                pass

        Is equivalent to the following::

            def index():
                pass
            app.add_url_rule('/', 'index', index)
"""


@app.route("/")
def index():
    print(app.config.get('SQL_URL'))
    return "index"


if __name__ == '__main__':
    app.run()