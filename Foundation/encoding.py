#!usr/bin/python
# -*- coding:utf8 -*-

#To define a source code encoding, a magic comment must be placed into the source files either as first or second line in the file
# python默认源文件编码是ASCII,python3默认源文件编码是utf8
# 以utf-8 或者 gbk等编码的代码，加载到内存，会自动转为unicode正常显示
# Python3中有两种字符串类型str和bytes
# 其实utf-8编码之所以能在windows gbk的终端下显示正常，是因为到了内存里python解释器把utf-8转成了unicode

s = "邻" # 以unicode形式保存新的内存空间中
# s可以直接encode成任意编码格式 utf-8可编程编码，对英文字符只用1Bytes表示，对中文字符用3Bytes
print(s.encode('utf8'))
test = b'\xe9\x82\xbb'
print(test.decode('utf8'))
s1 = s.encode('utf8')
s2 = s.encode('gbk')
print(s1, s2) # b'\xe9\x82\xbb' b'\xc1\xda'