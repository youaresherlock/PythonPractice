#!usr/bin/python
# -*- coding:utf8 -*-

import time
from math import sqrt

PW = 100000


def is_prime(n):
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


class ProgressBar:
    def __init__(self, total=0, width=20):
        self.total = total
        self.width = width

    def show(self, count, done='#', wait='-'):
        proc = self.width * count // self.total
        ok, undo = done * proc, wait * (self.width - proc)
        # 生成简单的进度条
        print(f'\rRunning... [{ok}{undo}] {count}/{self.total}', end='  ')


def main(total=PW):
    start = time.time()
    n = 1
    bar = ProgressBar(total)
    for p in range(0, total):
        while True:
            n += 2
            if is_prime(n):
                bar.show(p + 1)
                print(f"第{p + 1}个质数: {n}")
                break

    end = time.time()
    print(f'\ncost: {end-start} sec, result: {n}') # # 以f开头表示在字符串内支持大括号内的python 表达式


if __name__ == '__main__':
    main()

# 求第十万个质数cost: 23.41295313835144 sec, result: 1299721
# 计算第5209527个质数需1hour