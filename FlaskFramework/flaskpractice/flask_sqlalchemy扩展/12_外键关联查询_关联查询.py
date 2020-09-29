#!usr/bin/python
# -*- coding:utf8 -*-
"""
关联查询步骤: (以主查从为例)
先查询主表数据
在通过外键字段查询关联的从表数据
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test31'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

# 创建组件对象
db = SQLAlchemy(app)


# 用户表  一   一个用户可以有多个地址
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


# 地址表   多
class Address(db.Model):
    __tablename__ = 't_adr'
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(20))
    user_id = db.Column(db.Integer)  # 定义外键


@app.route('/demo')
def demo():
    """查询多表数据  需求: 查询姓名为"张三"的所有地址信息"""

    user = User.query.filter_by(name='张三').first()
    adrs = Address.query.filter_by(user_id=user.id).all()
    for adr in adrs:
       print(adr.detail)

    return "demo"


@app.route('/')
def index():
    """添加并关联数据"""

    user1 = User(name='张三')
    db.session.add(user1)
    db.session.flush()
    adr1 = Address(detail='中关村3号', user_id=user1.id)
    adr2 = Address(detail='华强北5号', user_id=user1.id)
    db.session.add_all([adr1, adr2])
    db.session.commit()

    return "index"


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    app.run(debug=True)










































