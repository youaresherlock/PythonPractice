#!usr/bin/python
# -*- coding:utf8 -*-
"""
flask-restful也实现了类似的功能:
反序列化:
    参数解析RequestParser
序列化: marshal函数

RequestParser负责请求解析工作,基本步骤如下:
创建请求解析器
    请求解析器 = RequestParser()
添加参数规则
    请求解析器.add_argument(参数名,参数规则...)
执行解析
    参数对象 = 请求解析器.parse_args()
获取参数
    参数对象.参数名
"""
from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser


app = Flask(__name__)
api = Api(app)


class DemoResource(Resource):
    def get(self):
        parser = RequestParser()

        parser.add_argument('name')
        parser.add_argument('age')

        # 执行解析, 默认会从查询字符串/post-form/post-json数据 进行参数提取
        args = parser.parse_args()

        print(args.name)
        print(args.age)

        return {'foo': 'get'}


api.add_resource(DemoResource, '/')


if __name__ == '__main__':
    app.run(debug=True)





















