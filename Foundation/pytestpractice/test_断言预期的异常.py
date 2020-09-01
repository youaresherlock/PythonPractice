#!usr/bin/python
# -*- coding:utf8 -*-
import pytest
import leap_year


class TestAssert(object):
    """对判断是否是闰年的方法进行测试"""

    def test_exception_typeerror(self):
        with pytest.raises(TypeError, match='传入的参数不是整数'):
            leap_year.is_leap_year('ss')

    def test_exception_true(self):
        assert leap_year.is_leap_year(2020), "今年是闰年"
