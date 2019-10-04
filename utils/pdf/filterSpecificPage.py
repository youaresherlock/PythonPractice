#!usr/bin/python
# -*- coding:utf8 -*-

#过滤pdf的特定页面，只保留特定页面；

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

with open('zz-pdf.pdf', 'rb') as rf: #需去除特定页面的pdf
    in_pdf=PdfFileReader(rf)  
    out_pdf=PdfFileWriter()
    add_pages=[1] #从0开始计数 
    for i in range(in_pdf.getNumPages()):
        if i in add_pages:
            with open('pdf-marker.pdf','rb') as mf:
                out_pdf.addPage(PdfFileReader(mf).getPage(0)) #取特定的一页
        out_pdf.addPage(in_pdf.getPage(i))
    out_pdf.write(open('zz-pdf-marker.pdf','wb'))


#将特定页面添加到pdf文件里

m_pdf = PdfFileMerger()
m_pdf.merge(0,'zz-pdf.pdf',pages=(0,2)) #提前确定初始化的时候有多少页
m_pdf.merge(1,'ipynb2pdf.pdf',pages=(0,1)) #可以省略用open打开的操作
m_pdf.write(open('zz-pdf-marker-7.pdf','wb'))

with open('zz-pdf.pdf', 'rb') as rf: #另一种写法
    #in_pdf=PdfFileReader(rf)
    m_pdf=PdfFileMerger() 
    m_pdf.merge(0,rf,pages=(0,2))
    with open('ipynb2pdf.pdf','rb') as f:
        m_pdf.merge(1,f,pages=(0,1))
        m_pdf.write(open('zz-pdf-marker-6.pdf','wb'))