
import pytest
import requests


@pytest.fixture()
def baidu_connection():
    resp = requests.get('http://www.baidu.com')
    return resp


def test_baidu(baidu_connection):
    assert baidu_connection.status_code == 200






















