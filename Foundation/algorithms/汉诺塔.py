#!usr/bin/python
# -*- coding:utf8 -*-
"""
有三个立柱A、B、C。A柱上穿有大小不等的圆盘N个，较大的圆盘在下，较小的圆盘在上。
要求把A柱上的圆盘全部移到C柱上，保持大盘在下、小盘在上的规律（可借助B柱）。
每次移动只能把一个柱子最上面的圆盘移到另一个柱子的最上面。请输出移动过程。

对于"将moveSum个圆盘从from柱移动到to柱（借助by柱）"这个问题，我们可以通过以下三步实现：
将from柱最上面的moveSum-1个圆盘移动到by柱（借助to柱）
将from柱上剩下的那1个圆盘直接移动到to柱
将by柱上的moveSum-1个圆盘移动到to柱（借助from柱）
"""


def move(n, a, b, c):
    if n == 1:
        print(a, "--->", c)
        return
    move(n-1, a, c, b)
    print(a, "--->", c)
    move(n-1, b, a, c)


move(3, 'from', 'by', 'to')































