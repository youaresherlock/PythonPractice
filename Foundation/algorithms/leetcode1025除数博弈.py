#!usr/bin/python
# -*- coding:utf8 -*-
"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 False。
假设两个玩家都以最佳状态参与游戏。


输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。

[address](https://leetcode-cn.com/problems/divisor-game)
"""


def divisor_game(N: int) -> bool:
    """
    找规律
    N = 1 Alice败
    N = 2 Alice胜
    N = 3 Alice败
    N = 4 Alice胜
    N = 5 Alice败
    我们会猜想当N为偶数的时候,先手(Alice)会胜

    证明: 我们用数学归纳法
    (1) N = 1 and N = 2 时结论成立
    (2) N > 2 时,假设N <= k时该结论成立,则N = k + 1 时
        k为偶数, 则k+1为奇数, x是k+1的因数,只可能是奇数,而奇数减去奇数等于
    偶数,且K+1-x<=k,则轮到Bob的时候都是偶数, 而之前已经假设N<=k的时候偶数先手
    必胜,则Alice必败
        k为奇数,则K+1为偶数,x可以是奇数也可以是偶数, 若 Alice 减去一个
    奇数，那么 k + 1 - xk+1−x 是一个小于等于 k 的奇数，此时 Bob 占有它
    ，处于必败态，则 Alice 处于必胜态。
    综上所以成立
    """
    return N % 2 == 0






