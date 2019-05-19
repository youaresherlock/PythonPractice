#!usr/bin/python
# -*- coding:utf8 -*-

import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return False
        if number %2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1

"""
找出比某个数的等比级数大的最小素数,比如10,我们要生成
比10,100,1000,10000...大的最小素数
"""
def print_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)
    """
    when send() is called to start the generator, it must be called with None as the argument,
    because there is no yield expression that counld receive the value
    """
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))

print_successive_primes(1000000000000, 10)
















