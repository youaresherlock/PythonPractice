#!usr/bin/python
# -*- coding:utf8 -*-
from datetime import datetime, timedelta

import jwt
from jwt import PyJWTError
import os, base64

payload = {  # jwt设置有效期的本质: 在内容中设置exp字段, 值要求为格林尼治时间
    "user_id": 22,
    'exp': datetime.utcnow() + timedelta(seconds=30)
}

# 生成随机字符串, 可用于秘钥
# randowm_str = base64.b64encode(os.urandom(40)).decode()

# 秘钥
key = 'N1UzXOFKJRZk5cslhMDcbqHZ0lKvCAyL85fufewVmUF9bGPAlAXw9w=='

# 生成签名
token = jwt.encode(payload, key=key, algorithm='HS256')
# print(token)


# 验签  pyjwt自动校验过期
# token = b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMiwiZXhwIjoxNTcwNjc3NjUzfQ.6scDFsiQwTH4gjyunGvVYW5jX40eLprevvN_I0Yw6GU'
try:
    data = jwt.decode(token, key=key, algorithms='HS256')  # 取出的是数据内容
    print(data)
except PyJWTError as e:
    print('验签失败: %s' % e)