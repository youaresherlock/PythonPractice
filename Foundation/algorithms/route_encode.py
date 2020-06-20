#!usr/bin/python
# -*- coding:utf8 -*-
"""
游程编码又称“运行长度编码”或“行程编码”，是一种统计编码，该编码属于无损压缩编码。对于二值图有效。

行程编码的基本原理是：用一个符号值或串长代替具有相同值的连续符号（连续符号构成了一段连续的“行程”。行程编码因此而得名），使符号长度少于原始数据的长度。

例如：5555557777733322221111111

行程编码为：(6,5),(5,7),(3,3),(4,2),(7,1)。可见，行程编码的位数远远少于原始字符串的位数。

现有一段原始编码，请完成它的行程编码
"""


message = input()
message_list = []
count = 1
for i in range(0, len(message)):
    if i + 1 < len(message) and message[i] == message[i+1]:
        count += 1
    else:
        message_list.append(message[i])
        message_list.append(count)
        count = 1
print(message_list)

buf = ""
for index, value in enumerate(message_list):
    if index % 2 == 0:
        buf += "(" + str(value) + ","
    else:
        buf += str(value) + "),"

print(buf.rstrip(','))


"""
方法二: 
line = input()
count = 1
for i in range(1, len(line)):
    if line[i] == line[i - 1]:
        count += 1
    else:
        print("(" + str(count) + "," + line[i - 1] + "),",end="")
        count = 1
print("(" + str(count) + "," + line[-1] + ")")
"""
