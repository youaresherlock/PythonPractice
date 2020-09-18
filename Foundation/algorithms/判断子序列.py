"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

链接：https://leetcode-cn.com/problems/is-subsequence
"""

"""
方法1: 贪心算法
我们维护两个指针指向两个列表的最开始，然后对第二个序列一路扫过去，
如果某个数字和第一个指针指的一样，那么就把第一个指针前进一步。
第一个指针移出第一个序列最后一个元素的时候，返回 True，
否则返回 False
"""
# def isSubsequence(s, t):
#     s_index = 0
#     for t_index in range(0, len(t)):
#         if s[s_index] == t[t_index]:
#             s_index += 1
#
#         if s_index == len(s):
#             return True
#     return False
#
# print(isSubsequence("abc", "alfebeeeeeeeeccccc"))

"""
b = (i for i in range(5))
print(2 in b)
print(4 in b)
print(3 in b)
########## 输出 
##########True True False
"""

def isSubsequence(s, t):
    # 这步很关键, 生成器会一直走到尽头, 所以可以判断是否按照顺序出现在t序列中
    t = iter(t)
    # 利用生成器 all函数中全为True则为True
    return all(i in t for i in s)


print(isSubsequence("abc", "alfebeeeeeeeeccccc"))