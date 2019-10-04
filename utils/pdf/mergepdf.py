#!usr/bin/python
# -*- coding:utf8 -*-

# 合并pdf

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

work_path = 'C:/Users/Clarence/Desktop/PythonPractice/utils/pdf/mergepdf/'

# 合并同一文件夹下的pdf文件
flst = [] # 获得pdf文件路径
for root, dirs, files in os.walk(work_path):
    flst = files
flst = [work_path + f for f in flst]
out_pdf = PdfFileWriter()

for pf in flst:
    in_pdf = PdfFileReader(open(pf, 'rb')) # 二进制打开
    page_count = in_pdf.getNumPages() # 输入pdf的页数
    for pc in range(page_count):
        out_pdf.addPage(in_pdf.getPage(pc)) # Adds a page to this PDF file.

with open(work_path +'合并1-3pdf.pdf', 'wb') as wf:
    out_pdf.write(wf) # writes the collection of pages added to this object out as a PDF file.

for root, dirs, files in os.walk(work_path):
    print(files)












