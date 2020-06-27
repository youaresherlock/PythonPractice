#!usr/bin/python
# -*- coding:utf8 -*-
"""
首先输入数字n，表示要输入多少个字符串。连续输入字符串
(输出次数为N,字符串长度小于100)。
按长度为8拆分每个字符串后输出到新的字符串数组，
长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
Input:
2
abc
123456789
Output:
abc00000
12345678
90000000
"""

n = int(input())

buf = ""
for i in range(0, n):
    x = input()
    if i == 0 and i != n-1:
        buf += x
        if len(buf) <= 8:
            buf += '0' * (8 - len(buf))
    elif i == n-1:
        buf += x
        c = len(buf) % 8
        buf += '0' * (8 - c)
    else:
        c = len(buf) % 8
        if c + len(x) <= 8:
            buf += x + '0' * (8 - c - len(x))
        else:
            if i == (n - 1):
                buf += x + '0' * (16 - len(x) - c)
            else:
                buf += x
while len(buf) >= 8:
    print(buf[:8])
    buf = buf[8:]
print(buf)










