#!usr/bin/python
# -*- coding:utf8 -*-
"""
方法:
1. 使用模块
2. 正则表达式,该方法性能不太好
3. 分治法,效率最高的方法之一
"""


"""
# 1.
from ipaddress import ip_address, IPv6Address


# 该模块认为如果IPv4地址包含前置0,则地址是有效的
def valid_ip_address(ip: str) -> str:
    try:
        return "IPv6" if type(ip_address(ip)) is IPv6Address else "IPv4"
    except ValueError:
        return "Neither"
"""

"""
使用正则表达式匹配ipv4的逻辑如下,注意不允许有前置0出现.
一共五种情况:
1. 块只包含一位数字,范围是0-9
2. 块包含两位数字,第一位的范围是1到9,第二位是0到9
3. 块包含三位数字,且第一位为1.第二、三位可以是0到9
4. 块包含三位数字,且第一位为2,第二位为0-4.那么第三位可以是0到9
5. 块包含三位数字,且第一位为2,第二位为5,那么第三位可以是0到5 
使用相同逻辑可以构造匹配IPv6地址的正则表达式
"""

"""
# 2.
import re


def valid_ip_address(ip: str) -> str:
    chunk_ipv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    pattern_ipv4 = re.compile(r'^(' + chunk_ipv4 + r'\.){3}' + chunk_ipv4 + r'$')

    chunk_ipv6 = r'([0-9a-fA-F]{1,4})'
    pattern_ipv6 = re.compile(r'^(' + chunk_ipv6 + r'\:){7}' + chunk_ipv6 + r'$')

    if '.' in ip:
        return "IPv4" if pattern_ipv4.match(ip) else 'Neither'
    if ':' in ip:
        return "IPv6" if pattern_ipv6.match(ip) else 'Neither'

    return 'Neither'
"""

"""
Ipv4和Ipv6地址均是由特定的分界符隔开的字符串组成,并且每个子字符串具有相同
格式 
1. 对于Ipv4地址,通过界定符,将地址分为四块;对于Ipv6地址,通过界定符,将地址分为八块
2. 对于Ipv4地址的每一块,检查它们是否在0-255内,且没有前置0 
3. 对于ipv6地址的每一块,检查其长度是否为1-4位的十六进制数
"""


def validate_ipv4(ip: str) -> str:
    nums = ip.split('.')
    for x in nums:
        # Validate integer in range(0, 255)
        # 1. length of chunk is between 1 and 3
        if len(x) == 0 or len(x) > 3:
            return 'Neither'

        # 2. no extra leading zeros
        # 3. only digits are allowed
        # 4. less than 255
        if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
            return 'Neither'

    return "IPv4"


def validate_ipv6(ip: str) -> str:
    nums = ip.split(':')
    hexdigits = '0123456789abcdefABCDEF'
    for x in nums:
        if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
            return 'Neither'

    return "IPv6"


def valid_ip_address(ip: str) -> str:
    if ip.count('.') == 3:
        return validate_ipv4(ip)
    elif ip.count(':') == 7:
        return validate_ipv6(ip)
    else:
        return 'Neither'






if __name__ == '__main__':
    illegal_ipv4 = '172.16.254.01'
    legal_ipv4 = '198.127.0.1'
    legal_ipv6 = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
    print(valid_ip_address(illegal_ipv4))
    print(valid_ip_address(legal_ipv4))
    print(valid_ip_address(legal_ipv6))
