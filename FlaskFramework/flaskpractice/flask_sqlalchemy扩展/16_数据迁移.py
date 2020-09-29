#!usr/bin/python
# -*- coding:utf8 -*-
"""
pip3 install flask_migrate
flask_migrate提供了数据迁移功能(增加字段、修改字段类型等)

执行迁移命令:
export FLASK_APP=xxx.py
flask db init # 生成迁移文件夹
flask db migrate # 生成迁移版本, 保存到迁移文件夹中
flask db upgrade # 执行迁移
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test32'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# SQlalchemy组件初始化
db = SQLAlchemy(app)

# 迁移组件初始化
Migrate(app, db)


# 构建模型类
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('username', db.String(20), unique=True)
    age= db.Column(db.Integer, default=10, index=True)


@app.route('/')
def index():

    return "index"


if __name__ == '__main__':
    app.run(debug=True)