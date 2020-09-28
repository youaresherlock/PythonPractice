#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:x1430371727@127.0.0.1:3306/test_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# 构建模型类
class Goods(db.Model):
    __tablename__ = 't_good'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    count = db.Column(db.Integer)


@app.route('/')
def purchase():
    goods = Goods(name='方便面', count=20)
    db.session.add(goods)
    # 主动执行flush操作,立即执行SQL操作(数据库同步)
    db.session.flush()
    # 提交会话会自动执行flush操作
    db.session.commit()

    return "index"


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    app.run(debug=True)