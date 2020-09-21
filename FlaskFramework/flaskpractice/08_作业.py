#!usr/bin/python
# -*- coding:utf8 -*-
"""
客户端发起POST请求，传递JSON数据, /login接受用户的请求
{
    "username": "clarence",
    "password": 123456,
    "remember": True
}
如果用户名和密码成功,表示登录成功，重定向到/userinfo在此页面显示:
欢迎回来: clarence. 如果用户名或密码错误,登录失败

登录成功,判断remember是否为True,如果为True实现状态保持,设置过期时间为3天,
否则保持到会话结束
"""
from datetime import timedelta
from flask import Flask, session, request, jsonify, make_response, redirect


app = Flask(__name__)
app.secret_key = 'you are sherlock'
app.permanent_session_lifetime = timedelta(days=3)


@app.route('/userinfo')
def user_info():
    username = request.cookies.get('username')

    return '欢迎回来: {}'.format(username)


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    remember = request.json.get('remember')

    if not all([username, password]):
        return jsonify({'errmsg': '缺少必传参数'})

    if not isinstance(remember, bool):
        return jsonify({'errmsg': 'remember类型为布尔值'})

    if username == 'clarence' and password == 123456:
        response = make_response(redirect('/userinfo'))
        if remember:
            session.permanent = True
            response.set_cookie('username', 'clarence', max_age=3 * 24 * 3600)
        else:
            response.set_cookie('username', 'clarence')
        session['username'] = 'clarence'

        return response
    else:
        return '登录失败', 400, {}


if __name__ == '__main__':
    app.run(debug=True)












