#!usr/bin/python
# -*- coding:utf8 -*-
"""
数据关联步骤:
从表模型类中定义外键字段
从表模型对象的外键字段记录主表主键
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# 创建组件对象
db = SQLAlchemy(app)


# 用户表 一个用户可以有多个地址
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


# 地址表 从表
class Address(db.Model):
    __tablename__ = 't_adr'
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(20))
    user_id = db.Column(db.Integer)


@app.route('/')
def index():
    """添加并关联数据"""
    user = User(name='张三')
    db.session.add(user)
    # 需要手动执行flush操作,让主表生成主键,否则外键关联失败
    db.session.flush()
    # 有些场景下,为了保证数据操作的原子性不能分成多个事务进行操作
    # db.session.commit()

    adr1 = Address(detail='中关村3号', user_id=user.id)
    adr2 = Address(detail='华强北5号', user_id=user.id)
    db.session.add_all([adr1, adr2])
    db.session.commit()

    return 'index'


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    app.run(debug=True)










































