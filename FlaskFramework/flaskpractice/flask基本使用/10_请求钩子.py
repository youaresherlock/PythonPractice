#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask, Response


# 请求钩子: 类比django中间件 ,请求钩子可以对请求的各阶段进行监听, 方便开发者针对请求完成一些统一的处理
app = Flask(__name__)


"""
# 另一种语法
def prepare():
    print('before_request')

app.before_request(prepare)
"""


# 每次执行视图函数之前调用, 对请求进行一些准备处理, 如参数解析, 黑名单过滤, 数据统计等
@app.before_request
def prepare():
    print('before_request')


# 每次执行视图函数之后(已经包装为响应对象)调用, 对响应进行一些加工处理, 如设置统一响应头, 设置数据的外层包装
@app.after_request
def process(response: Response):  # 必须定义形参接收响应对象
    print('after_request:')
    # print(response.headers)
    # print(response.data)
    # print(response.status_code)
    return response


# web应用被第一次请求前调用, 可以进行web应用初始化处理, 如数据库连接
@app.before_first_request
def initial():
    print('before_first_request')


# 每次执行视图函数之后调用, 无论是否出现异常都会执行, 一般用于请求收尾, 如资源回收, 异常统计
@app.teardown_request  # 测试时不要开启调试模式
def request_handle(error):  # 必须定义形参来接收具体错误信息, 如果没有错误, error=None
    print('teardown_request : %s' % error)


@app.route('/')
def index():
    print('执行视图')
    a = 1 / 0
    return "index"


if __name__ == '__main__':
    app.run()