#!usr/bin/python
# -*- coding:utf8 -*-
# 蓝图作用: 实现Flask程序的模块化
# main.py
from flask import Flask
from home import home_blu

app = Flask(__name__)
# 4.注册蓝图
app.register_blueprint(home_blu)


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, port=8000)
