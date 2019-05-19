#!usr/bin/python
# -*- coding:utf8 -*-
# 列表模仿队列，先进后出
from collections import deque

queue = deque(["Eric", "Clarence", "Linux Torvards"])
# 把一个元素添加到列表的结尾,相当于a[len(a):] = [x]
queue.append("Terry")
queue.append("Graham")
print(queue.popleft()) # The first to arrive now leaves
print(queue.popleft())
print(queue.pop()) # 返回最后一个元素，元素随即从列表中被移除

print(queue)

# 列表推导式提供了从序列创建列表的简单途径.
vec = [2, 4, 6]
print([3 * x for x in vec])
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print(vec1[i] * vec2[i] for i in range(len(vec1)))

# 集合支持集合推导式
a = {x for x in 'afagegete' if x not in 'abc'}
print(a)


matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)


# dek语句可以从一个列表中依索引而不是值来删除一个元素。这与使用pop()返回一个值不同，可以用del语句从
# 列表中删除一个切割或清空整个列表
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)

# 元组由若干逗号分隔的值组成
# 元组在输出时总是有括号的，以便于正确表达嵌套结构.在输入时可能有或没有括号，不过括号通常是必须的
t  = 345, 1212, "hello"
print(t)

# 字典以关键字为索引，看做无序的键值对集合
# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# 此外，字典推导可以用来创建任意键和值的表达式词典：
test = {x : x ** 2 for x in (2, 4, 6)}
# 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
print(list(zip(questions, answers)))
for q, a in zip(questions, answers):
    print("What is your {0}? It is {1}.".format(q, a))



