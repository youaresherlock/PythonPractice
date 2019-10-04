#!usr/bin/python
# -*- coding:utf8 -*-

# 单张图片转pdf pip3 install pillow安装PIL库
# https://python-pillow.org/

from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter
img = Image.open('C:\\Users\\Clarence\\Desktop\\PythonPractice\\utils\\pdf\\picture\\1.jpg')
img.save('C:\\Users\\Clarence\\Desktop\\PythonPractice\\utils\\pdf\\picture\\1.pdf', 'PDF') # 通过PIL库保存为pdf格式

# 多张图片转pdf
list = ['C:\\Users\\Clarence\\Desktop\\PythonPractice\\utils\\pdf\\picture\\1.jpg',
        'C:\\Users\\Clarence\\Desktop\\PythonPractice\\utils\\pdf\\picture\\2.jpg',
        'C:\\Users\\Clarence\\Desktop\\PythonPractice\\utils\\pdf\\picture\\3.jpg']
out_pdf = PdfFileWriter()
for file in list:
    img = Image.open(file)
    fw = file.replace('.jpg', '.pdf')
    img.save(fw)
    out_pdf.appendPagesFromReader(PdfFileReader(open(fw, 'rb')))
out_pdf.write(open('C:\\Users\\Clarence\\Desktop\\PythonPractice\\utils\\pdf\\picture\\4.pdf', 'wb'))
























