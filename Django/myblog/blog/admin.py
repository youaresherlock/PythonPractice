from django.contrib import admin

# Register your models here.
'''
配置Admin 
在应用下admin.py中引入自身的Models模块(或里面的模型类) 
编辑admin.py: admin.site.register(models.Article)

显示其他字段 
在配置类中加上一条属性
list_display = ('title', 'content') 
list_display同时支持tuple和list类型

过滤器 
list_filter = ('pub_time')
'''
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time',)

admin.site.register(models.Article, ArticleAdmin)
