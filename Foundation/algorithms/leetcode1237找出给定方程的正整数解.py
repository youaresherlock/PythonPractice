#!usr/bin/python
# -*- coding:utf8 -*-
"""
给出一个函数  f(x, y) 和一个目标结果 z，请你计算方程 f(x,y) == z 
所有可能的正整数 数对 x 和 y。
给定函数是严格单调的，也就是说：

f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)
函数接口定义如下：

interface CustomFunction {
public:
  // Returns positive integer f(x, y) for any given positive integer x and y.
  int f(int x, int y);
};
如果你想自定义测试，你可以输入整数 function_id 和一个目标结果 z 作为输入，
其中 function_id 表示一个隐藏函数列表中的一个函数编号，题目只会告诉你列表中的 2 个函数。  

你可以将满足条件的 结果数对 按任意顺序返回。

输入：function_id = 1, z = 5
输出：[[1,4],[2,3],[3,2],[4,1]]
解释：function_id = 1 表示 f(x, y) = x + y

[address](https://leetcode-cn.com/problems/find-positive-integer-solution-for-a-given-equation)
"""
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
from typing import List


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        # 暴力法 没有利用递增条件
        # return [[x, y] for x in range(1, z+1) for y in range(1, z+1) if customfunction.f(x, y) == z]

        # 二分查找法 只利用到了函数f对y变量是递增的,没有利用到对x也是这样
        # 遍历x,对于每个x,可能存在一个对应的y 而f(x,y)的值随着y的增加是增加的
        # 因此可以使用二分查找
        ans = []
        for x in range(1, z + 1):
            left, right = 1, z
            while left <= right:
                mid = (left + right) // 2
                res = customfunction.f(x, mid)
                if res < z:
                    left = mid + 1
                elif res > z:
                    right = mid - 1
                else:
                    ans.append([x, mid])
                    break
        return ans

















