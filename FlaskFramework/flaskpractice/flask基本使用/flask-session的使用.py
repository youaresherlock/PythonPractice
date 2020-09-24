#!usr/bin/python
# -*- coding:utf8 -*-
"""
pip3 install flask-session
"""
from flask import Flask, session
from flask_session import Session
from redis import StrictRedis


app = Flask(__name__)

# 设置Session的配置
app.config['SESSION_TYPE'] = 'redis'
# 指定redis的客户端
app.config['SESSION_REDIS'] = StrictRedis(host='127.0.0.1', port=6379)
# 设置对Session的签名
app.config['SESSION_USE_SIGNER'] = True
# 设置SECRET_KEY
app.config['SECRET_KEY'] = 'you are sherlock'
# 初始化组件
Session(app)


@app.route('/')
def index():
    session['user_id'] = 1
    return 'index'


@app.route('/demo')
def demo():
    print(session.get('user_id'))
    return 'demo'


if __name__ == '__main__':
    app.run(debug=True)