#!usr/bin/python
# -*- coding:utf8 -*-
"""
app.config 用于设置配置, 该属性继承自 dict,
可以以字典形式赋值取值
"""
from datetime import timedelta
from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'test'

# config属性用于设置配置
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route('/')
def index():
    # 设置session 用于测试配置是否生效
    session['name'] = 'zs'

    # 读取配置
    print(app.config.get('PERMANENT_SESSION_LIFETIME'))
    return "index"


if __name__ == '__main__':
    app.run(debug=True)