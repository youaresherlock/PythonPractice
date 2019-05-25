#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:x1430371727@localhost/net_news?charset=utf8"
db = SQLAlchemy(app)

class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    content = db.Column(db.String(2000), nullable = False)
    type = db.Column(db.String(10), nullable = False)
    image = db.Column(db.String(300))
    author = db.Column(db.String(20))
    view_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean)

    def __repr__(self):
        return '<User %r>' % self.title

# 下面初始化数据库，创建表news
# db.create_all()

# Flask配备了Jinja2模板引擎,可以使用render_template()方法来渲染模板，会在templates文件夹里
# 寻找模板
@app.route("/")
def index():
    ''' 新闻首页'''
    return render_template("index.html")

@app.route('/cat/<name>/')
def cat(name):
    ''' 新闻类别 '''
    # 查询类别为name的新闻数据
    return render_template('cat.html', name = name)

@app.route('/detail/<int:pk>/')
def detail(pk):
    ''' 新闻详情 '''
    return render_template('detail.html', pk = pk)

if __name__ == "__main__":
    app.run(debug = True)