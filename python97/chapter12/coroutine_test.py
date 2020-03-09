#!usr/bin/python
# -*- coding:utf8 -*-

def gen_func():
    #!. 可以产出值，2.可以接受值(调用方传递进来的值)
    html = yield "http://projectesdu.com"
    print(html)
    yield 2
    yield 3
    return "bobby"

# 1.throw  close 

#1. 生成器不只可以产生值，也可以接受值

if __name__ == "__main__":
    gen = gen_func()
    # 1.启动生成器的方式有两种，next(),send()
    # 在调用send发送非None值之前，我们必须启动一次生成器，方式有两种.gen.send(None) next(gen)
    url = gen.send(None)
    html = "bobby"
    print(gen.send(html))# send方法可以传递值进入生成器内部，还可以重启生成器执行到下一个yield