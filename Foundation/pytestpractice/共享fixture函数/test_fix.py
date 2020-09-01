#!usr/bin/python
# -*- coding:utf8 -*-
import pytest


# @pytest.mark.usefixtures('baidu_login')
def test_get_carts(baidu_login):
    """购物车不需要登陆"""
    print("测试查询购物车")


@pytest.mark.usefixtures('baidu_login')
class Test_fixtures:
    """需要登陆的信息"""

    def test_get_user_info(self):
        print("获取用户信息")

    def test_order_info(self):
        print("查询订单信息")




















