#!usr/bin/python
# -*- coding:utf8 -*-
"""
@pytest.fixture注册成为一个fixture函数,来为测试用例
提供一个fixture对象
"""
import pytest
import make_warning


class TestWarns():
    def test_make_warn(self):
        with pytest.warns(DeprecationWarning):
            make_warning.make_warn()

    def test_not_warn(self):
        with pytest.warns(SyntaxWarning):
            make_warning.not_warn()

    def test_user_warn(self):
        with pytest.warns(UserWarning):
            make_warning.make_warn()
















