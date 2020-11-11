#!usr/bin/python
# -*- coding:utf8 -*-
"""
消除字符串中相同的字符(大小写敏感),输出最终字符串的长度
字符串只包含大小写字母,如果有别的字符直接输出0
"""


def disappear(message):
    if not message.isalpha():
        return 0
    p = []
    for si in message:
        if p and si == p[-1]:
            p.pop()
        else:
            p.append(si)
    result = "".join(p)

    return len(result)


if __name__ == '__main__':
    message = input()
    print(disappear(message))
















