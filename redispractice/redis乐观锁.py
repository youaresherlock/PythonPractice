#!usr/bin/python
# -*- coding:utf8 -*-
"""
WATCH mykey  # 监视mykey的值
MULTI  # 开启事务
SET mykey 10
EXEC  # 如果mykey的值在执行exec之前发生过改变, 则该事务会取消(客户端可以在发生碰撞后不断重试)
"""
# 需求: 使用redis实现秒杀功能(防止超卖)
from redis import StrictRedis, WatchError


# 1. 创建客户端
redis_client = StrictRedis()

# 2. 创建管道对象
pipe = redis_client.pipeline()

while True:
    try:
        # 3.监听数据  如果开启监听, 则不会开启默认的事务, 后续的pipe操作会立即执行
        pipe.watch('reserve_count')
        # 4. 读取库存数量
        count = pipe.get('reserve_count')

        # 判断库存数量
        if int(count) > 0:
            # 手动开启事务
            pipe.multi()

            # 库存减一
            pipe.decr('reserve_count')

            # 提交事务
            pipe.execute()
            print('下单成功')
        else:
            print('商品已售罄')
            # 将监听移除
            pipe.reset()
        break
    # 捕获到该异常,说明监听的数据被其他客户端修改,此时应该重试/取消操作
    except WatchError as e:
        print('数据被修改,重试')
        continue

























