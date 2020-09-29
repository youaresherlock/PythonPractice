#!usr/bin/python
# -*- coding:utf8 -*-
"""
关系属性的使用步骤:
定义关系属性 关系属性名 = db.relationship('关联数据所在的模型类')
外键字段设置外键参数 外键字段 = db.Column(字段类型, db.ForeginKey(主表名.主键名))
通过关系属性获取关联数据 模型对象.关联属性
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
    addresses = db.relationship('Address')


# 地址表   多
class Address(db.Model):
    __tablename__ = 't_adr'
    id = db.Column(db.Integer, primary_key=True)
    detail = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('t_user.id'))


@app.route('/')
def index():
    """添加数据"""
    user1 = User(name='张三')
    db.session.add(user1)
    db.session.flush()
    adr1 = Address(detail='中关村3号', user_id=user1.id)
    adr2 = Address(detail='华强北5号', user_id=user1.id)
    db.session.add_all([adr1, adr2])
    db.session.commit()

    """查询多表数据  需求: 查询姓名为"张三"的所有地址信息"""
    # 先根据姓名查找用户主键
    user1 = User.query.filter_by(name='张三').first()

    # 3.使用关系属性获取关系数据
    for address in user1.addresses:
        print(address.detail)

    return "index"


if __name__ == '__main__':
    # 重置所有继承自db.Model的表
    db.drop_all()
    db.create_all()

    app.run(debug=True)