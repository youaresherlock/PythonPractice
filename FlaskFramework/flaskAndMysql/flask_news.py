#!usr/bin/python
# -*- coding:utf8 -*-
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, abort, request
from flask_sqlalchemy import SQLAlchemy

from forms import NewsForm


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
    news_list = News.query.filter_by(is_valid = 1)
    return render_template("index.html", news_list = news_list)

@app.route('/cat/<name>/')
def cat(name):
    ''' 新闻类别 '''
    # 查询类别为name的新闻数据
    news_list = News.query.filter_by(type=name).all()
    return render_template('cat.html', news_list = news_list, name = name)

@app.route('/detail/<int:pk>/')
def detail(pk):
    ''' 新闻详情 '''
    new_obj = News.query.get(pk)
    return render_template('detail.html', new_obj = new_obj)

@app.route('/admin/') # 默认显示page=1页的数据
@app.route('/admin/<int:page>/') # 显示第page也的数据
def admin(page=None):
    ''' 新闻管理首页 '''
    if page is None:
        page = 1
    page_data = News.query.filter_by(is_valid=1).paginate(page=page, per_page=6)
    return render_template('admin/index.html', page_data = page_data)

@app.route('/admin/add/', method=('GET','POST'))
def add():
    ''' 后台新闻新增'''
    form = NewsForm()
    if form.validate_on_sumit():
        # 验证数据后获取数据
        # 保存数据
        new_obj = News(
            title=form.title.data,
            content=form.content.data,
            type=form.type.data,
            image=form.image.data,
            created_at=datetime.now()
        )
        db.session.add(new_obj)
        db.session.commit()
        flash("新增成功")
    return render_template('admin/add.html')

@app.route('/admin/delete/<int:pk>/')
def delete(pk):
    ''' 后台新闻删除 '''
    new_obj = News.query.get(pk)
    return render_template('admin/update.html', new_obj = new_obj)

@app.route('/admin/update/<int:pk>/')
def update(pk):
    ''' 后台新闻修改 '''
    new_obj = News.query.get(pk)
    return render_template('admin/update.html', new_obj = new_obj)



if __name__ == "__main__":
    app.run(debug = True)


























