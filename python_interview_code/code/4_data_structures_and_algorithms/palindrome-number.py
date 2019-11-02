#!usr/bin/python
# -*- coding:utf8 -*-

"""
https://leetcode.com/problems/palindrome-number/
判断一个数字是否是回文数
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return list(str(x)) == list(reversed(str(x)))
        # return str(x) == str(x)[::-1]
        if x < 0:
            return False
        beg = 0
        s = str(x)
        beg, end = 0, len(s) - 1
        while beg < end:
            if s[beg] == s[end]:
                beg += 1
                end -= 1
            else:
                return False
        return True

def test():
    s = Solution()
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(-1) == False
    assert s.isPalindrome(1) is True










