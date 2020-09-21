#!usr/bin/python
# -*- coding:utf8 -*-
# 自定义转换器:
# 1.定义转换器类, 继承BaseConverter
# 2.设置regex属性 (正则匹配规则)
# 3.添加自定义转换器

from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 1.定义转换器类
class MobileConverter(BaseConverter):
    # 2.设置regex属性(匹配规则)
    regex = r'1[3-9]\d{9}$'  # 不要设置开头的^


# 3.添加自定义转换器
app.url_map.converters['mob'] = MobileConverter


@app.route('/user/<mob:mobile>')
def index(mobile):
    print(mobile)
    return "index"


if __name__ == '__main__':
    # 获取所有的转换器 {转换器名: 转换器类}
    # print(app.url_map.converters)
    app.run(debug=True)
