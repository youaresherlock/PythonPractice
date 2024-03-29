#!usr/bin/python
# -*- coding:utf8 -*-
"""给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。
已知此链表是一个整数数字的二进制表示形式。请你返回该链表所表示数字的 十进制值 。

输入：head = [1,0,1]
输出：5
解释：二进制数 (101) 转化为十进制数 (5)
 
[address](https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer)

"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_decimal_value(head: ListNode) -> int:
    cur = head
    ans = 0
    while cur:
        # 二进制转十进制规律
        ans = ans * 2 + cur.val
        cur = cur.next

    return ans


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = ListNode(1)
    print(get_decimal_value(head))

















