#!usr/bin/python
# -*- coding:utf8 -*-
from PIL import Image
import pytesseract
image = Image.open("phone.jpg")
code = pytesseract.image_to_string(image, lang="eng", config="--psm 6")
print(f"解析出图片上的数字为:{code}")
# 假设这是货到到的偏移量的大小
# price_list = ['192.6', '107', '21.4', '64.2']
# num = 21.4
# real_price = ""
# # 遍历
# for price in price_list:
#     res = int(float(price)/num)
#     print(f"获取到数据对应的下标：{res}")
#     real_price += code[res]
# print(real_price)