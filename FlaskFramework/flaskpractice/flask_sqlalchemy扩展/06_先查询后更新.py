#!usr/bin/python
# -*- coding:utf8 -*-
"""
对应的SQL中的先select, 再update
执行查询语句,获取目标模型对象
对模型对象的属性进行赋值(更新数据)
提交会话

缺点:
查询和更新分两条语句,效率低
如果并发更新，可能出现更新丢失问题
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test31'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# 创建组件对象
db = SQLAlchemy(app)


# 构建模型类  商品表
class Goods(db.Model):
    __tablename__ = 't_good'  # 设置表名
    id = db.Column(db.Integer, primary_key=True)  # 设置主键
    name = db.Column(db.String(20), unique=True)  # 商品名称
    count = db.Column(db.Integer)  # 剩余数量


@app.route('/')
def purchase():
    """购买商品"""

    # 更新方式1: 先查询后更新
    # 缺点: 并发情况下, 容易出现更新丢失问题 (Lost Update)
    good = Goods.query.filter(Goods.name == '方便面').first()
    good.count = good.count - 1
    db.session.commit()

    return "index"


if __name__ == '__main__':
    # 删除所有继承自db.Model的表
    db.drop_all()
    # 创建所有继承自db.Model的表
    db.create_all()

    # 添加一条测试数据
    goods = Goods(name='方便面', count=1)
    db.session.add(goods)
    db.session.commit()
    app.run(debug=True)