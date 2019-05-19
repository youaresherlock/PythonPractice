#!usr/bin/python
# -*- coding:utf8 -*-
# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行

# 集合,创建一个空集合必须用set()而不是{}, {}是用来创建一个空字典
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('apple' in basket)

a = set('abafakfeka')
b = set('testesa')

# 两个集合之间的运算
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

a = {x for x in 'aafaf' if x not in 'abc'}
print(a)

# 集合的基本操作
# 添加元素,s.add(x) s.update(x)也可以添加元素,且参数可以是列表，元组，字典等,x可以有多个，用逗号分开
thisset = {"Google", "Runoob", "Taobao"}
thisset.add("Facebook")
print(thisset)
thisset.update([1,2], [3, 3])
print(thisset)

# 移除元素 s.remove(x)不存在会发生错误 s.discard(x)不存在不会发生错误 s.pop()随机删除一个元素
thisset.remove('Facebook')
thisset.pop()
print(thisset)

# 清空集合
thisset.clear()
print(thisset)

print(type(range(10)))




