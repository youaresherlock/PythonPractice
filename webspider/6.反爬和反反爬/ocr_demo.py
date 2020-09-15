#!usr/bin/python
# -*- coding:utf8 -*-
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '22636118'
API_KEY = 'BtWq8b4QFdbOX5le6O3DbKue'
SECRET_KEY = '1nmmRREYSYAgHiYE0462Gba0yVIW9YTG'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('phone.jpg')

res = client.basicGeneral(image)

print(res)
