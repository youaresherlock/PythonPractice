#!usr/bin/python
# -*- coding:utf8 -*-
from datetime import datetime
from flask import Flask, render_template, flash, url_for, abort, request, redirect
from flask_mongoengine import MongoEngine, ValidationError
from forms import NewsForm


app = Flask(__name__)
# mongodb 数据库配置
app.config['MONGODB_SETTINGS'] = {
    'db': 'flask_news',
    # 'username': 'admin',
    # 'password': '123456',
    'host': '127.0.0.1',
    'port': 27017
}
app.config["SECRET_KEY"] = "a random key"
db = MongoEngine(app)
"""
An iterable (e.g. list, tuple or set) of choices to which the value of this field should be limited.
Can either be nested tuples of value (stored in mongo) and a human readable key
"""
NEWS_TYPES = (
    ('推荐', '推荐'),
    ('百家', '百家'),
    ('本地', '本地'),
    ('图片', '图片')
)

class News(db.Document):
    ''' 新闻模型 '''
    title = db.StringField(required=True, max_length=200)
    content = db.StringField(required=True)
    news_type = db.StringField(required=True, choices=NEWS_TYPES)
    img_url = db.StringField()
    is_valid = db.BooleanField(default=True)
    created_at = db.DateTimeField(default=datetime.now())
    updated_at = db.DateTimeField(default=datetime.now())

    # 对有黄字标题的新增新闻过滤验证
    def clean(self):
        if '黄' in self.title:
            raise ValidationError("不能有黄字")

    meta = {
        'collection': 'mongo_news',
        'ordering': ['-created_at']
    }

    def __repr__(self):
        return '<News %r>' % self.title

@app.route('/')
def index():
    ''' 新闻首页 '''
    news_list = News.objects.filter(is_valid=True).all()
    return render_template('index.html', news_list=news_list)

@app.route('/cat/<name>/')
def cat(name):
    ''' 新闻类别页 '''
    news_list = News.objects.filter(is_valid=True, news_type=name).all()
    return render_template('cat.html', news_list=news_list)

@app.route('/detail/<pk>/')
def detail(pk):
    ''' 新闻详情页 '''
    new_obj = News.objects.filter(pk=pk, is_valid=True).first_or_404()
    # new_obj = News.objects.filter(is_valid=True, pk=pk).first()
    # if not new_obj:
    #     abort(404)
    return render_template('detail.html', new_obj=new_obj)

@app.route('/admin/')
@app.route("/admin/<int:page>/")
def admin(page=None):
    ''' 后台首页 '''
    if page is None:
        page = 1
    page_data = News.objects.filter(is_valid=True).paginate(page=page, per_page=5)
    return render_template('admin/index.html', page_data=page_data)

@app.route('/admin/add/', methods=['GET', 'POST'])
def add():
    ''' 后台增加新闻 '''
    form = NewsForm()
    """
    validate_on_submit() call validate() only if the form is submitted. This is 
    a shortcut for form.is_submitted() and form.validate().
    """
    if form.validate_on_submit():
        print(form.title.data)
        new_obj = News(title=form.title.data, content=form.content.data,
                       img_url=form.img_url.data, news_type=form.news_type.data)
        new_obj.save()
        flash('新增成功')
        return redirect(url_for('admin'))
    return render_template('admin/add.html', form=form)

@app.route('/admin/update/<pk>/', methods=['GET', 'POST'])
def update(pk):
    ''' 后台更新新闻 '''
    obj = News.objects.filter(pk=pk, is_valid=True).first_or_404()
    # obj = News.objects.get_or_404(pk=pk, is_valid=True)
    form = NewsForm(obj=obj)
    if form.validate_on_submit():
        obj.title = form.title.data
        obj.content = form.content.data
        obj.news_type = form.news_type.data
        obj.updated_at = datetime.now()
        obj.save()
        flash("修改成功")
        return redirect(url_for('admin'))
    return render_template('admin/update.html', form=form)

@app.route('/admin/delete/<pk>/', methods=['POST'])
def delete(pk):
    ''' 后台删除新闻 '''
    new_obj = News.objects.filter(pk=pk).first()
    if not new_obj:
        return 'no'
    # 逻辑删除
    new_obj.is_valid = False
    new_obj.save()
    # 物理删除
    # delete the document from the database. This will only take effect if the document has been previously saved
    # new_obj.delete()
    return 'yes'


if __name__ == '__main__':
    app.run(debug=True)


















