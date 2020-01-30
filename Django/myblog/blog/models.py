from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32, default='title')
    content = models.TextField(null=True) # 允许标题为空
    pub_time = models.DateTimeField(null=True) # 创建对象的同时设置为当前时间

    def __str__(self):
        return self.title

'''
生成数据表
python manage.y makemigrations app名(可选) 
再执行python manage.py migrate生成数据表
Django会在app/migrations下自动生成移植文件 
执行python manage.py sqlmigrate 应用名  文件id 查看SQL语句
查看并编辑db.sqlite3 
使用第三方软件 SQLite Expert Personal 轻量级免费的
配置admin
创建用户 python manage.py createsuperuser 创建超级用户
clarence admin123
localhost:8000/admin/ Admin入口

修改settings.py中LANGUAGE_CODE= 'zh_Hans'后台英文转换成中文

模板for循环 
{% for x in xxx %}
HTML语句
{% endfor %}

超链接目标地址 
href后面是目标地址 
template中可以用" {% url 'app_name:url_name' param %}"
其中app_name和url_name都在url中配置

博客撰写页面
编辑响应函数
使用request.POST['参数名']获取表单数据
models.Article.objects.create(title, content)创建对象

Admin 
创建admin配置类
class ArticleAdmin(admin.ModelAdmin) 
注册: admin.site.register(Article, ArticleAdmin)
'''

























