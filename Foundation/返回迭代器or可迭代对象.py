#!usr/bin/python
# -*- coding:utf8 -*-
import random
from collections.abc import Iterable, Iterator

r = range(10)
m = map(int, [random.uniform(0, 10) for _ in range(5)])
print(isinstance(r, Iterable), isinstance(m, Iterator))