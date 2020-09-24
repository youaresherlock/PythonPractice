#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask
from flask import request

app = Flask(__name__)


# 1.路由对应的URL必须以/开头
# 2.通过app的url_map属性获取所有的路由规则 (URL资源段 支持的请求方式 视图函数标记)
# 3.可以通过route方法的methods参数指定路由支持的请求方式
@app.route('/hello', methods=['post', 'get'])
def index():
    # / hello?name = hello & name = test
    print(request.args)  # 查询字符串参数
    print(request.args.get('name'))  # 获取列表中第一个元素
    print(request.args.getlist('name'))  # 获取一个列表
    return "index"


if __name__ == '__main__':
    print(app.url_map)

    # 获取路由信息
    # for rule in app.url_map.iter_rules():
    #     print(rule.rule, rule.methods, rule.endpoint)

    app.run(debug=True)

