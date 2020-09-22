#!usr/bin/python
# -*- coding:utf8 -*-
"""
请求钩子: 类比Django的中间件,对请求的各阶段进行监听, 用于
抽取视图中的公共代码,减少代码冗余
"""
from flask import Flask


app = Flask(__name__)


# 视图函数执行之前会调用,一般会用于请求的准备工作,如
# 参数解析,黑名单过滤,数据统计等
@app.before_request
def prepare():
    print('before_request')


# 没有出现错误的情况下,每次视图函数执行之后调用, 一般会用于响应的
# 加工工作, 如设置统一的响应头,设置数据的外层包装
@app.after_request
def process(resp):
    resp.headers['name'] = 'clarence'
    # 加工完响应对象,将响应对象再返回
    return resp


@app.before_first_request
def initial():
    print('before_first_request')


@app.teardown_request
def clear_request(error):
    print('error: {}'.format(error))


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
