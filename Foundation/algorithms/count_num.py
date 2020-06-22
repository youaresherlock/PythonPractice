#!usr/bin/python
# -*- coding:utf8 -*-
"""
输入字符串, 返回排序后的列表[#!usr/bin/python
# -*- coding:utf8 -*-(字符， 个数)]
"""


str1 = "itesajlajlaf"
"""
方法二: 
    count = [0] * 1000 
    for x in str1:
        count[ord(x)] += 1 
    for i in range(0, len(count)):
        if count[i] > 0:
            print(chr(i) + str(count[i]), end="")
"""
dict1 = {}
for x in str1:
    if x not in dict1:
        dict1[x] = 1
    else:
        dict1[x] += 1

list1 = list(dict1.items())
list1.sort(key=lambda x: x[0])
print(list1)

















