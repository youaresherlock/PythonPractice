#!usr/bin/python
# -*- coding:utf8 -*-

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class User:
    def __init__(self):
        self.name = 'zs'
        self.age = 20
        self.height = 1.8
        self.scores = [80, 90]
        self.info = {
            'gender': True
        }

    def to_dict(self):  # 自定义模型转换方法
        return {
            'name': self.name,
            'age': self.age
        }


class DemoResource(Resource):
    def get(self):
        user1 = User()
        return user1.to_dict()


api.add_resource(DemoResource, '/')


if __name__ == '__main__':
    app.run(debug=True)