#!usr/bin/python
# -*- coding:utf8 -*-
from tasks import add

for i in range(100):
    result = add.delay(i, i)
    print(result.get())

