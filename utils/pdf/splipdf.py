#!usr/bin/python
# -*- coding:utf8 -*-

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

# 切分pdf

work_path = 'C:/Users/Clarence/Desktop/PythonPractice/utils/pdf/splitpdf/test.pdf'

source_pdf = PdfFileReader(open(work_path, 'rb')) # 需要切分的pdf
count_src = source_pdf.getNumPages()

# 每20页切分为1个PDF文件
out_pdf = PdfFileWriter()
for count in range(count_src):
    if count % 20 == 0 and count > 0:
        with open(work_path + '切分_{0}.pdf'.format(count), 'wb') as wf:
            out_pdf.write(wf)
        out_pdf = PdfFileWriter() # 每20页重新常见Writer对象
    else:
        # 首次需要加入页
        out_pdf.addPage(source_pdf.getPage(count))

















