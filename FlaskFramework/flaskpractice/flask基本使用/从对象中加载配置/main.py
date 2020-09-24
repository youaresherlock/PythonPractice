#!usr/bin/python
# -*- coding:utf8 -*-
# main.py

from datetime import timedelta
from flask import Flask

app = Flask(__name__)

# 从对象中加载配置
# 优点: 面向对象的设计有利于 减少重复代码 以及 代码解耦合
from config import DevelopmentConfig
app.config.from_object(DevelopmentConfig)


@app.route('/')
def index():
    print(app.config.get('PERMANENT_SESSION_LIFETIME'))
    return "index"


if __name__ == '__main__':
    app.run(debug=True)