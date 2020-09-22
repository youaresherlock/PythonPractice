#!usr/bin/python
# -*- coding:utf8 -*-
from flask import Flask

app = Flask(__name__,  # 导入名称, flask会根据该参数查询静态文件的存储路径
            # 官方建议直接使用__name__, 表示从当前目录中查询静态文件存储路径
            static_folder="static1",  # 设置静态文件的存储目录
            static_url_path='/res/img',  # 设置静态文件的URL访问路径 如 127.0.0.1:5000/res/img/123.jpg
            )

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)

