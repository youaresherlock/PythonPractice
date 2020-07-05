#!usr/bin/python
# -*- coding:utf8 -*-
"""
LFU:
    采用LFU算法的最简单方法是为每个加载到缓存的快分配一个计数器.每次引用该块时,
计数器将增加1.当缓存达到容量并且有一个新块等待插入时,系统将搜索计数器最低的块并
将其从缓存中删除
实现: LFU的每个数据块都有一个引用计数,所有数据块按照引用计数排序,具有相同引用计数
的数据块则按照时间排序
1. 新加入数据插入到队列尾部(因为引用计数为1)
2. 队列中的数据被访问后,引用计数增加,队列重新排序
3. 当需要淘汰数据时,将已经排序的列表最后的数据块删除
"""
import bisect


class LFUCache:
    def __init__(self, capacity: int):
        # 容量capacity和计时time
        self.cap, self.time = capacity, 0
        # 元素形式为: (频率,时间,键)(freq, time, key)
        self.his = []
        # 使用字典保存双关键字-键值对形式为key: [val, freq, time]
        self.dic = {}

    def get(self, key: int) -> int:
        # key不存在,返回-1
        if key not in self.dic:
            return -1
        # 更新该缓存的时间
        self.time += 1
        # 取出值,频率和时间
        val, freq, time = self.dic[key]
        # 更新该缓存的使用频率
        self.dic[key][1] += 1  # 将频率+1
        self.dic[key][2] = self.time
        # 找到history里的记录并移除原来缓存
        self.his.pop(bisect.bisect_left(self.his, (freq, time, key)))
        # 将更新后的记录二分插入
        bisect.insort(self.his, (freq+1, self.time, key))
        return val

    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return
        self.time += 1
        # 查看哈希表中是否有对应键值
        if key in self.dic:
            # 取出频率和时间
            _, freq, time = self.dic[key]
            self.dic[key][:] = value, freq + 1, self.time
            # 找到history里的记录并移除
            self.his.pop(bisect.bisect_left(self.his, (freq, time, key)))
            # 将更新后的记录二分插入
            bisect.insort(self.his, (freq + 1, self.time, key))
        else:
            # 无该记录
            self.dic[key] = [value, 1, self.time]
            # history容量是否已经满了，满了需要缓存淘汰
            if len(self.his) == self.cap:
                # 删除最近最少使用缓存,因为有序,移除history首个元素即对应的键值对
                del self.dic[self.his.pop(0)[2]]
            # 将新纪录插入history
            bisect.insort(self.his, (1, self.time, key))


if __name__ == '__main__':
    capacity = 2
    cache = LFUCache(capacity)
    print(cache.put(2, 2))
    print(cache.get(1))
    print(cache.put(3, 3))
    print(cache.get(2))
    print(cache.get(3))
    print(cache.put(4, 4))
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))


"""
None
-1
None
2
3
None
-1
3
4
"""






















































































