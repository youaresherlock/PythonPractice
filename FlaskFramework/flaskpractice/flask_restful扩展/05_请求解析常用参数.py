#!usr/bin/python
# -*- coding:utf8 -*-
"""
parser.add_argument()常用参数:
default: 不传递该参数则使用默认值
required: 默认为False. 如果设置为True,不传递会返回400
location: 设置参数提取的位置(args查询字符串/form表单/json请求体/files文件对象
    /headers请求头/cookies
type: 设置参数的转换类型(类型转换 & 格式校验) 可以传递函数引用、int等内置类型
"""
from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser


app = Flask(__name__)
api = Api(app)


class DemoResource(Resource):
    def get(self):
        parser = RequestParser()

        parser.add_argument('name', required=True, location='args')
        parser.add_argument('age', default=10)

        args = parser.parse_args()

        print(args.name)
        print(args.age)

        return {'foo': 'get'}


api.add_resource(DemoResource, '/')


if __name__ == '__main__':
    app.run(debug=True)





















