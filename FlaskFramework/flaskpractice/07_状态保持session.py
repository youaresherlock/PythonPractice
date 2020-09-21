#!usr/bin/python
# -*- coding:utf8 -*-
from datetime import timedelta
from flask import Flask, session

app = Flask(__name__)
# 设置应用秘钥   会被用于session签名
app.secret_key = 'test'
# 设置session过期时间   默认31天
app.permanent_session_lifetime = timedelta(days=7)


@app.route('/')
def index():
    # session是一个类字典对象, 对其取值/赋值 就可以实现session数据的读写

    # 记录session数据
    session['username'] = 'zs'

    # 设置session支持过期时间
    session.permanent = True

    # 删除session数据
    # session.pop('username')

    return "index"


@app.route('/demo1')
def demo1():

    # 获取session数据
    name = session.get('username')
    print(name)
    return 'demo1'


if __name__ == '__main__':
    app.run(debug=True)