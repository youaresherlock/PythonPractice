#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask


app = Flask(__name__)


# 定义路由
@app.route('/')
def index():
    return 'hello flask'


if __name__ == '__main__':
    # 运行应用(启动一个测试服务器,接受请求并调用对应的视图函数)
    # host: 绑定的ip地址 0.0.0.0
    # port: 监听的端口
    app.run()





































