#!usr/bin/python
# -*- coding:utf8 -*-
"""
db.session.query(主表模型字段1, 主表模型字段2, 从表模型字段1, xx.. ).join(从表模型类,
主表模型类.主键 == 从表模型类.外键)
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


# 用户表  一
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
    """查询多表数据  需求: 查询姓名为"张三"的用户id和地址信息"""

    # sqlalchemy的join查询
    data = db.session.query(User.id, Address.detail).join(Address, User.id == Address.user_id).filter(User.name == '张三').all()
    # 使用join语句优化关联查询
    # adrs = Address.query.join(User, Address.user_id == User.id).filter(User.name == '张三').all()
    for item in data:
        print(item.detail, item.id)

    return "demo"


@app.route('/')
def index():
    """添加数据"""
    user1 = User(name='张三')
    db.session.add(user1)
    db.session.flush()
    adr1 = Address(detail='中关村3号', user_id=user1.id)
    adr2 = Address(detail='华强北5号', user_id=user1.id)
    db.session.add_all([adr1, adr2, user1])
    db.session.commit()

    return 'index'


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    app.run(debug=True)