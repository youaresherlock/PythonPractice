#!usr/bin/python
# -*- coding:utf8 -*-

f = open("foo.txt", "w")

f.write("Python 是一个非常好的语言.\n是的，的确非常好!!\n")

f.close()


f = open("foo.txt", "r")

str = f.read()
print(str)
f.close()
print(f.closed)

"""
当处理一个文件对象时，使用with关键字是非常好的方式，在结束后，它会帮你正确的关闭文件.写起来也比try-finally语句块
简短
pickle模块实现了基本的数据序列和反序列化
通过pickle模块的序列化操作将程序中运行的对象信息保存到文件中取，永久存储
pickle.dump(obj, file, [,protocol])
x = pickle.load(file)
"""
import pickle

mes = {"name" : "Clarence", "Age" : 90, "bucket" : [1,2,3,4 + 1j]}
output = open('data.pkl', 'wb')

pickle.dump(mes, output)

output.close()

input = open('data.pkl', 'rb')
info = pickle.load(input)
print(info)

input.close()

"""
os.path模块主要用于获取文件的属性
os.chdir()方法用于改变当前工作目录到指定的路径
"""
import os
print(os.getcwd())
print(os.listdir(os.getcwd()))
# 返回文件大小，如果文件不存在就返回错误
print(os.path.getsize(r"C:\Users\Clarence\Desktop\PythonTest\file.py"))
# 把路径分割成dirname和basename,返回一个元组
print(os.path.split(r"C:\Users\Clarence\Desktop\PythonTest\file.py"))
# 将目录和文件合成一个路径
print(os.path.join("root", "test", "runoob.txt"))

print(os.sep)


