#!usr/bin/python
# -*- coding:utf8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired

class NewsForm(FlaskForm):
    """ 新闻表单 """
    title = StringField(label='新闻标题', validators=[DataRequired("请输入标题")],
        description="请输入标题",
        render_kw={"required": "required", "class": "form-control"})
    content = TextAreaField(label='新闻内容', validators=[DataRequired("请输入内容")],
        description="请输入内容",
        render_kw={"required": "required", "class": "form-control"})
    news_type = SelectField('新闻类型',
        choices=[('推荐', '推荐'), ('百家', '百家'), ('本地', '本地'), ('图片', '图片')],
        render_kw={"class": "form-control"})
    img_url = StringField(label='新闻图片',
        description='请输入图片地址',
        render_kw={'required': 'required', 'class': 'form-control'})
    submit = SubmitField('提交')

