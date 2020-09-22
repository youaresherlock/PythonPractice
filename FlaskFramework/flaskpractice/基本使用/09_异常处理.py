#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask, abort
# flask对http错误进行了封装, 可以捕获http错误也可以主动抛出http错误

app = Flask(__name__)


# 捕获http错误
@app.errorhandler(404)
def error_404(error):  # 一旦进行捕获, 要求必须定义形参接收具体错误信息
    return "<h3>您访问的页面去浪迹天涯了</h3> %s" % error


# 还可以捕获系统内置错误
@app.errorhandler(ZeroDivisionError)
def error_zero(error):
    return '除数不能为0'


@app.route('/')
def index():
    # a = 1 / 0

    abort(500)  # 主动抛出异常 (只能抛出http错误)
    return "index"


if __name__ == '__main__':
    app.run(debug=True)