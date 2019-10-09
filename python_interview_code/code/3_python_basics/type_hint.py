#!usr/bin/python
# -*- coding:utf8 -*-

"""
PEP 484 Type Hints
对函数的参数进行类型注解
对函数的返回值进行类型注解
只对函数参数做一个辅助的说明, 并不对函数参数进行类型检查
提供给第三方工具,做代码分析,发现隐藏bug
函数注解的信息,保存在__annotations__属性中,__annotations__属性是一个字典
"""

def greeting(name: str) -> str:
    return 'hello ' + name

print(greeting('clarence'))
print(greeting.__annotations__)