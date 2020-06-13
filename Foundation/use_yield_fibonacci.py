#!usr/bin/python
# -*- coding:utf8 -*-
print(type((i * 2 for i in range(5))))  # 生成器推导式


def fibonacci(num):
    a, b = 0, 1
    current_index = 0
    while current_index < num:
        result = a
        a, b = b, a + b
        current_index += 1
        yield result


fib = fibonacci(10)
for value in fib:
    print(value)