#!usr/bin/python
# -*- coding:utf8 -*-
import pytest
import requests


def test_one():
    r = requests.get('http://baidu.com')
    assert r.status_code == 200


def test_two():
    r = requests.get('http://baidu.com')
    assert r.encoding == 'ISO-8859-1'


# pytest.main()





















