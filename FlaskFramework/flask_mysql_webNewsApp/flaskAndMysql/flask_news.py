#!usr/bin/python
# -*- coding:utf8 -*-
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, abort, request
from flask_sqlalchemy import SQLAlchemy

"""
pycharm默认该项目的根目录为source目录，所以import使用绝对路径而不是相对路径的话，就会从
项目的根目录中查找.可以使用相对路径或者将要引入的模块作为sources
"""
from forms import NewsForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:x1430371727@localhost/net_news?charset=utf8"
app.config['SECRET_KEY'] = 'youaresherlock'
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

@app.route('/admin/add/', methods=['GET','POST'])
def add():
    ''' 后台新闻新增'''
    form = NewsForm()
    if form.validate_on_submit():
        # 验证数据后获取数据
        # 保存数据
        new_obj = News(
            title=form.title.data,
            content=form.content.data,
            type=form.type.data,
            image=form.image.data,
            created_at=datetime.now(),
            is_valid=1
        )
        db.session.add(new_obj)
        db.session.commit()
        # 文字提示
        flash("新增成功")
        # Returns a response object(a WSGI application) that, if called, redirects the client to the target location
        return redirect(url_for('admin'))
    else:
        flash("请输入新闻数据")
    return render_template('admin/add.html', form=form)

# 注: 删除只能用POST请求
@app.route('/admin/delete/<int:pk>/', methods=['POST'])
def delete(pk):
    ''' 后台新闻删除 '''
    # 先判断请求的类型，这里实际上route路由已经限制了只能POST请求
    if request.method == 'POST':
        obj = News.query.get(pk)
        if obj is None:
            return 'no'
        obj.is_valid = False
        db.session.add(obj) # 逻辑删除
        # db.session.delete(obj) # 物理删除
        db.session.commit()
        return 'yes'
    return 'no' # 这里route限制了，所以执行不到

@app.route('/admin/update/<int:pk>/', methods=['GET', 'POST'])
def update(pk):
    ''' 后台新闻修改 '''
    obj = News.query.get(pk)
    # 为给定的状态码引发HTTPExeception
    if obj is None:
        abort(404)
    form = NewsForm(obj=obj)
    if form.validate_on_submit():
        obj.title = form.title.data
        obj.content = form.content.data
        obj.type = form.type.data
        # 将修改后的对象提交事务
        db.session.add(obj)
        db.session.commit()
        flash("修改成功")
        # 跳转到首页
        return redirect(url_for('admin'))
    return render_template('admin/update.html', form = form)



if __name__ == "__main__":
    app.run(debug = True)


























