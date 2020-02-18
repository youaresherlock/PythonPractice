#!usr/bin/python
# -*- coding:utf8 -*-

from collections.abc import Mapping, MutableMapping
# dict属于Mapping类型
a = {}
print(isinstance(a, MutableMapping))