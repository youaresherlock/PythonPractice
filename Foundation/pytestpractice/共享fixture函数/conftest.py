#!usr/bin/python
# -*- coding:utf8 -*-
"""
conftest.py配置里可以实现数据共享
"""
import pytest
import requests


@pytest.fixture(autouse=True)
def baidu_login():
    print('\n公用的登录方法')
























