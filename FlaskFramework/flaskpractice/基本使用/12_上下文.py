#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask, request, current_app, g

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
