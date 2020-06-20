#!usr/bin/python
# -*- coding:utf8 -*-
"""
小明受邀参加朋友的晚会Part，形式为自助餐，已经目前有N种食物编号1-N依次摆放在一行，小明可以从中挑选食物，但必须符合以下条件

如果选中了某个编号为X的食物，则两边的食物不能选中（即x-1，x+1的食物不能选）
小明可以选择任意个食物

小明有多少个选择?
"""


"""
方法1:
n = int(input())
num = [0] * (n + 1) 
num[1] = 2 
num[2] = 3 
for i in range(3, n+1):
    num[i] = num[i-1] + num[i-2]
print(num[n])
"""


from functools import wraps


def cache(func):  # 装饰器
    store = {} # 外部变量

    @wraps(func)
    # 按照习惯，有时候单个独立下划线是用作一个名字，来表示某个变量是临时的或无关紧要的
    def _(n):  # 闭包函数
        if n in store:
            return store[n]
        else:
            res = func(n)
            store[n] = res
            return res
    return _


@cache
def get_choices(num):
    if num <= 1:
        return num + 1
    return get_choices(num - 1) + get_choices(num - 2)


if __name__ == '__main__':
    food_num = input()
    print(get_choices(int(food_num)))

