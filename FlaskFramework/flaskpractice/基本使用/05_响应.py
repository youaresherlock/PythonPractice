#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask, redirect, url_for
from flask import make_response
from flask import Response
from flask import jsonify

app = Flask(__name__)


@app.route('/demo1')
def demo1():
    # 返回值:  响应体, 响应状态码, 响应头
    return 'demo1', 400, {'A': 40}


# 自定义响应对象
@app.route('/demo2')
def demo2():
    # 视图函数的返回值可以为str/bytes类型, 并且flask内部会将其包装为Response响应对象
    # return 'hello flask'

    # 创建响应对象     设置响应头时,需要手动创建响应对象
    response = make_response('hello flask')  # type: Response
    # 设置响应头
    response.headers['B'] = 10
    return response


# 返回json
@app.route('/demo3')
def demo3():

    dict1 = {'name': 'zs', 'age': 20}
    # 字典转json字符串
    # json.dumps序列化只支持int/str/list/tuple/dict类型
    # return json.dumps(dict1)

    # 可以将字典转json字符串, 并且设置响应头的content-type为application/json
    # return jsonify(dict1)
    return jsonify(name='zs', age=20)  # 也支持关键字实参的形式


# 重定向
@app.route('/demo4')
def demo4():
    # 重定向到指定网站
    # return redirect('http://www.baidu.com')
    # 重定向到自己的路由   只需要URL资源段
    return redirect('/demo3')


if __name__ == '__main__':
    app.run(debug=True)