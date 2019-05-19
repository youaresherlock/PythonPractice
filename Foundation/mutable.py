#!usr/bin/python
# -*- coding:utf8 -*-
"""
在Python中,strings, tuples, 和numbers是不可更改的对象，而dict,list等则是可以修改的对象
不可变类型: 变量赋值a=5后再赋值a=10,这里实际是新生成一个int值对象10,再让a指向它，而5被丢弃，不是改变a的值
可变类型: 变量赋值la = [1,2,3,4]后再赋值la[2]=5则是将list la的第三个元素值更改，本身la没有变动
Python函数的参数传递分为不可变类型和可变类型，分别类似于C++的值传递和引用传递，但是Python中一切都是对象，
我们应该说传不可变对象和可变对象
"""

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)

























