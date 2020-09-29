#!usr/bin/python
# -*- coding:utf8 -*-
"""
Session的生命周期和请求相近:
请求中的首次数据操作会创建Session
整个请求过程中使用的Session为同一个,并且线程隔离
请求结束时会自动销毁Session
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/toutiao'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# 构建模型类
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('username', db.String(20), unique=True)
    age = db.Column(db.Integer, default=0, index=True)


@app.route('/')
def index():

    """事务1"""
    try:
        user1 = User(name='zs', age=20)
        db.session.add(user1)
        db.session.commit()
    except BaseException:
        # 手动回滚   同一个session中, 前一个事务如果失败, 必须手动回滚, 否则无法创建新的事务
        db.session.rollback()

    """事务2"""
    user1 = User(name='lisi', age=30)
    db.session.add(user1)
    db.session.commit()

    return "index"


if __name__ == '__main__':
    """为了进行测试, 首次运行 建表并添加一条测试数据后, 注释下方代码, 并重新运行测试"""

    # 重置所有继承自db.Model的表
    # db.drop_all()
    # db.create_all()

    # 添加一条测试数据
    # user1 = User(name='zs', age=20)
    # db.session.add(user1)
    # db.session.commit()

    app.run(debug=True)