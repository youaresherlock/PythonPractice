#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask, request, current_app, g
"""
current_app: 会自动引用创建的flask对象,需要在项目的其他文件中使用flask
对象时,应该通过current_app来获取,减少循环导入的问题
"""

# 上下文变量: 有使用范围  [请求开始, 请求结束]
# 请求上下文: 记录一些和请求有关的数据 request session
# 应用上下文: 记录一些和应用有关的数据  current_app  g

app = Flask(__name__)


@app.route('/')
def index():
    # print(request.url)
    g.name = 'zs'

    return "index"


@app.route('/demo1')
def demo1():
    # print(g.name)  # 会报错
    return 'demo1'


if __name__ == '__main__':
    with app.app_context():
        print(current_app, g)
    # print(request.url)  # 使用范围外, 会报错
    # app.run(debug=True)
