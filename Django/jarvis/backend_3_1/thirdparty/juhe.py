#!/usr/bin/python
# -*-encoding=utf8 -*-
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/21
# @Filename       : juhe.py
# @Desc           :


import json
import requests


def weather(cityname):
    """
    :param cityname: 城市名字
    :return: 返回实况天气
    """
    key = '9a3e1fa6cb79d69f1594af5cb219a469'
    api = 'http://v.juhe.cn/weather/index'
    params = 'cityname=%s&key=%s' % (cityname, key)
    url = api + '?' + params
    print(url)
    response = requests.get(url=url)
    json_data = json.loads(response.text)
    print(json_data)
    result = json_data.get('result')
    sk = result.get('sk')
    response = dict()
    response['temperature'] = sk.get('temp')
    response['wind_direction'] = sk.get('wind_direction')
    response['wind_strength'] = sk.get('wind_strength')
    response['humidity'] = sk.get('humidity')  # 湿度
    response['time'] = sk.get('time')
    return response


if __name__ == '__main__':
    data = weather('深圳')
