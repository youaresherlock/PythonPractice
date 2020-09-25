#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:x1430371727@127.0.0.1:3306/test_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# 创建组件对象
db = SQLAlchemy(app)


# 构建模型类
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('username', db.String(20), unique=True)
    age = db.Column(db.Integer, index=True)


@app.route('/')
def index():
    """增加数据"""

    # 1.创建模型对象
    user1 = User(name='zs', age=20)
    # user1.name = 'zs'
    # user1.age = 20

    # 2.将模型对象添加到会话中
    db.session.add(user1)
    # 添加多条记录
    # db.session.add_all([user1, user2, user3])

    # 3.提交会话 (会提交事务)
    # sqlalchemy会自动创建隐式事务
    # 事务失败会自动回滚
    db.session.commit()

    return "index"


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)