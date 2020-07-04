#!usr/bin/python
# -*- coding:utf8 -*-
import logging

# 定义文件
file1 = logging.FileHandler(filename="multifile.txt", mode="a", encoding="utf8")
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
file1.setFormatter(fmt)

file2 = logging.FileHandler(filename="multifile2.txt", mode="a", encoding="utf8")
fmt = logging.Formatter()
file2.setFormatter(fmt)

# 定义日志
logger1 = logging.Logger(name="这里是name", level=logging.ERROR)
logger1.addHandler(file1)
logger1.addHandler(file2)

# 写日志
logger1.error(msg="这里是msg111")
logger1.log(msg="这里是msg222", level=50)

# 定义文件
file3 = logging.FileHandler(filename="multifile3.txt", mode="a", encoding="utf8")
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
file3.setFormatter(fmt)

# 定义日志
logger2 = logging.Logger(name='这里是name222222', level=logging.INFO)
logger2.addHandler(file3)

# 写日志
logger2.info('这里是msg333333')

