#!usr/bin/python
# -*- coding:utf8 -*-
import json
from jsonpath import jsonpath
import requests


# 获取拉勾网城市json字符串
url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}

response = requests.get(url, headers=headers)

# html_str = response.content.decode()
# json_str = json.loads(html_str)
json_str = response.json()

city_list = jsonpath(json_str, '$..name')

with open('city_name.json', 'w') as f:
    """
    这是因为json.dumps 序列化时对中文默认使用的ascii编码.
    想输出真正的中文需要指定ensure_ascii=False
    """
    content = json.dumps(city_list, ensure_ascii=False)
    f.write(content)
















