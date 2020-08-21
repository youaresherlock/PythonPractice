#!usr/bin/python
# -*- coding:utf8 -*-
"""
有效括号字符串为空 ("")、"(" + A + ")" 或 A + B，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。

如果有效字符串 S 非空，且不存在将其拆分为 S = A+B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。

给出一个非空有效字符串 S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。

对 S 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S 。

输入："(()())(())"
输出："()()()"
解释：
输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。

[address](https://leetcode-cn.com/problems/remove-outermost-parentheses)
"""


def remove_outer_parentheses(S: str) -> str:
    # 思路 关键在于如何判断哪些括号是最外层括号.
    # 1. 双指针计数
    # 使用双指针的意义在于,用两个指针找到所有最外层左右括号的下标
    # 一开始为0,碰到左括号, 计数+1,碰到有括号,计数-1.当计数为0时,就找到了最外层的右括号.
    # (()())()
    # 12121010 得到(0, 5)和(6, 7)
    # primitive_indices = []
    # left, count = 0, 0
    # for i in range(len(S)):
    #     if S[i] == '(':
    #         count += 1
    #     elif S[i] == ')':
    #         count -= 1
    #     if count == 0:  # 找到最外层右括号
    #         primitive_indices.append((left, i))  # 添加答案
    #         left = i + 1  # 更新最外层左括号指针
    #
    # return ''.join(S[m+1:n] for m, n in primitive_indices)

    # 2. 单指针计数
    # 一次遍历过程中,直接把非最外层的括号放进答案里
    # res, count = [], 0
    # for c in S:
    #     # 当count=0且c=='('时,表示刚开始不需要加入
    #     if c == '(' and count > 0:
    #         res.append(c)
    #     # 当count=1且c==')'时,表示到达末尾,count这时候为0也不许要加入
    #     if c == ')' and count > 1:
    #         res.append(c)
    #     if c == '(':
    #         count += 1
    #     else:
    #         count -= 1
    #
    # return ''.join(res)

    # 3. 单调栈(栈里面只存在左括号,右括号仅仅是用来消灭左括号的)
    # 碰到'('入栈,碰到')'就把栈顶的一个'('消掉
    # 如果栈为空,那么刚刚碰到的')'就是最外层右括号,如果入栈前栈为空,则即将
    # 入栈的'('就是最外层左括号
    res, stack = '', []
    for c in S:
        if c == '(':
            if stack:
                res += c
            stack.append('(')
        if c == ')':
            stack.pop()
            if stack:
                res += c

    return res































