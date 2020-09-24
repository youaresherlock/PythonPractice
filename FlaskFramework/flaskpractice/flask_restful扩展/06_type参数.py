#!usr/bin/python
# -*- coding:utf8 -*-
"""
type: 设置参数的转换类型(类型转换 & 格式校验) 可以传递函数引用、int等内置类型
"""
from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
from flask_restful.inputs import *


app = Flask(__name__)
api = Api(app)


# 自定义函数进行参数校验和转换
def func(value):
    if re.match(r'^user:', value):
        return value[5:]
    else:
        raise ValueError('age参数格式错误')


class DemoResource(Resource):
    def get(self):
        parser = RequestParser()

        parser.add_argument('name')
        # parser.add_argument('age', type=int)
        # parser.add_argument('age', type=date)
        parser.add_argument('age', type=func)

        args = parser.parse_args()

        print(args.name)
        print(args.age)

        return {'foo': 'get'}


api.add_resource(DemoResource, '/')


if __name__ == '__main__':
    app.run(debug=True)





















