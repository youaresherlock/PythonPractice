#!/usr/bin/python
# -*- coding:utf-8 -*-


# 方法1logg
def reverseBits(n: int) -> int:
    result = 0

    for i in range(32):
        # 此处+优先符高于&
        result = (result << 1) + (n & 1)
        n >>= 1

    return result


if __name__ == '__main__':
    message = 43261596
    print(reverseBits(message))
























    