#!usr/bin/python
# -*- coding:utf8 -*-

def gen_func():
    try:
        yield "http://projectesdu.com"
    except GeneratorExit:
        pass 
    yield 2
    yield 3
    return "bobby"

if __name__ == "__main__":
    gen = gen_func()
    next(gen)
    gen.close()
    next(gen)
