#!usr/bin/python
# -*- coding: utf8 -*-

# os模块提供了不少与操作系统相关联的函数
import os
print(os.getcwd())
# shutil模块提供了日常的文件和目录管理任务
"""
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
>>> shutil.move('/build/executables', 'installdir')
"""
# 文件通配符 glob模块提供了一个函数用于从目录通配符搜索中生成文件列表
import glob
print(glob.glob('*.py')) # 当前目录下所有的.py文件

# 字符串正则匹配 re模块为高级字符串处理提供了正则表达式工具.
import re

result = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(result)
# math模块为浮点运算提供了对低层c函数库的访问
"""
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
"""

"""
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
"""
# 数据压缩 支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
import zlib

s = b'witch which has which witches wrist watch'
t = zlib.compress(s)
print(len(s), len(t))
print(zlib.decompress(t))

# 处理get请求,不传data
from urllib.request import urlopen
from urllib.parse import urlencode

url = "https://www.imooc.com/"
data = {"username" : "admin", "password" : 123456}
req_data = urlencode(data) # 将字典类型的请求数据转变为url编码username=admin&password=123456
res = urlopen(url + "?" + req_data) #访问url
"""
Python3将系统默认编码设置为utf8,用str表示unicode所有字符,bytes类型表示二进制数据
一般编码和解码格式保持一致,即使用utf-8编码后，也要用utf-8解码，否则可能会报错
内存中使用的编码是unicode，用空间换时间（程序都需要加载到内存才能运行，因而内存应该是尽可能的保证快）
；硬盘中或者网络传输用utf-8，网络I/O延迟或磁盘I/O延迟要远大与utf-8的转换延迟，而且I/O应该是尽可能地节省带
宽，保证数据传输的稳定性。
如果服务端encode的编码格式是utf-8， 客户端内存中收到的也是utf-8编码的二进制

bytes.decode(encoding="utf-8", errors="strict")
Return a string decoded from the given bytes. Default encoding is 'utf-8'
res =res.read().decode()
"""
res = res.read().decode('utf8')
print(res)


#处理post请求,如果传了data，则为post请求

#import urllib
from urllib.request import Request
#from urllib.parse import urlencode

url='http://www.imooc.com/'
data={"username":"admin","password":123456}
data=urlencode(data)#将字典类型的请求数据转变为url编码
data=data.encode('ascii')#将url编码类型的请求数据转变为bytes类型
req_data=Request(url,data)#将url和请求数据处理为一个Request对象，供urlopen调用
with urlopen(req_data) as res:
    res=res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

print(res)



















