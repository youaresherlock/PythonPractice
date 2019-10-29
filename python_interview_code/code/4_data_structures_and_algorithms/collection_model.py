#!usr/bin/python
# -*- coding:utf8 -*-

# namedtuple 让tuple属性可读

import collections

Point = collections.namedtuple('Point', 'x, y')

p = Point(1, 2)

print(p.x, p.y)
print(p[0], p[1])
