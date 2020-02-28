#!usr/bin/python
# -*- coding:utf8 -*-

# 读取500G大小文件，特殊只有一行数据
"""
f = open()
f.read(4096)
"""
def myreadlines(f, newline):
  buf = ""
  while True:
    while newline in buf:
      pos = buf.index(newline)
      yield buf[:pos]
      buf = buf[pos + len(newline):]
    chunk = f.read(4096)

    if not chunk:
      #说明已经读到了文件结尾
      yield buf
      break
    buf += chunk

with open("input.txt") as f:
    for line in myreadlines(f, "{|}"):
        print (line)






























