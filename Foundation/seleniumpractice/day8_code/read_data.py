#!usr/bin/python
# -*- coding:utf8 -*-
import yaml


with open('data.yaml', 'r', encoding='utf8') as f:
    # results = f.read()
    # print('results={}'.format(results))
    # 直接使用load方法，会有方法弃用警告信息，不影响读取数据操作
    # 如果要关闭，可以使用Loader=yaml.FullLoader关闭警告
    # results = yaml.load(f)
    results = yaml.load(f, Loader=yaml.FullLoader)
    print('results={}'.format(results))
    name = results['data']['name']
    age = results['data']['age']
    mobile = results['data']['mobile']
    print('姓名: {}\n年龄: {}\n手机号: {}'.format(name, age, mobile))


# 打开yaml文件，写入数据到文件中
data = {'data3': {'name': '李四', 'age': 30, 'mobile':'18812345678'}}
with open('data.yaml', 'a+', encoding='utf8') as f:
    # 中文默认情况下,会乱码
    # yaml.dump(data, f)
    yaml.dump(data, f, allow_unicode=True)






















