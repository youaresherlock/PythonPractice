#!usr/bin/python
# -*- coding:utf8 -*-
"""
序列化: marshal函数
步骤:
    定义序列化规则
    序列化规则字典 = {字段名: 序列化类型}
    marshal函数按照序列化规则将模型对象转为字典
"""
from flask import Flask
from flask_restful import Resource, Api, marshal, fields


app = Flask(__name__)
api = Api(app)


# 定义模型类
class User(object):
    def __init__(self):
        self.name = 'clarence'
        self.age = 18
        self.height = 1.75
        self.scores = [80, 90]
        self.info = {
            'gender': True,
            'level': 8
        }


# 序列化规则
fields = {
    'username': fields.String(attribute='name'),
    'age': fields.Integer(default=20),
    'height': fields.Float(),
    # 列表类型属性,要求列表中元素类型唯一
    'scores': fields.List(fields.Integer),
    'info': fields.Nested({'gender': fields.Boolean,
                           'level': fields.Integer})
}


class DemoResource(Resource):
    def get(self):
        user = User()

        return marshal(user, fields, envelope='data')


api.add_resource(DemoResource, '/')


if __name__ == '__main__':
    app.run(debug=True)

















