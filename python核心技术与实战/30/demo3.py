#!usr/bin/python
# -*- coding:utf8 -*-
from unittest.mock import MagicMock


def side_effect(arg):
    if arg < 0:
        return 1
    else:
        return 2


mock = MagicMock()
mock.side_effect = side_effect

mock(-1)
1

mock(1)
2