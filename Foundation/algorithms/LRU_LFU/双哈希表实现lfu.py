import collections


class Node:
    def __init__(self, key, val, pre=None, nex=None, freq=0):
        self.pre = pre
        self.nex = nex
        self.freq = freq  # 当前节点使用频率
        self.val = val
        self.key = key

    # 插入节点
    # self-> nex-> self.nex
    def insert(self, nex):
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex


# 创建双向链表，包含值为0的head，tail
def create_linked_list():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nex = tail
    tail.pre = head
    return (head, tail)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0  # 键值对总数
        self.minFreq = 0  # 记录最小的频率，每次容量满了，删这个频率的head.nex
        self.freqMap = collections.defaultdict(
            create_linked_list)  # key是频率，值是一条双向链表的head, tail，最近操作的节点插入tail前面，则head.nex是最小使用频率的节点，删除时删head.nex
        self.keyMap = {}  # 存储键值对，值是node 类型

    # 双向链表中删除指定节点
    def delete(self, node):
        if node.pre:  # 不是第一个节点，就需要删除，
            node.pre.nex = node.nex  # 前后前接起来
            node.nex.pre = node.pre
            if node.pre is self.freqMap[node.freq][0] and node.nex is self.freqMap[node.freq][
                -1]:  # 新的频率中已存在这个节点，且只有这个节点，那就直接把这个新频率删掉，方便后面插入最新数据
                self.freqMap.pop(node.freq)
        return node.key

    # 增加
    def increase(self, node):
        node.freq += 1  # 当前节点频率+1
        self.delete(node)  # 旧频率中，删除此节点
        self.freqMap[node.freq][-1].pre.insert(node)  # 新频率中，tail节点前插入当前节点
        if node.freq == 1:  # 出现频率为1的了，记录一下，下次容量满了先从这里删
            self.minFreq = 1
        elif self.minFreq == node.freq - 1:  # 操作最小频率的节点时，从旧频率到新频率时需要检查下旧频率，只有head,tail就不可能从这里删数据了，那就需要把minFreq更新为新频率，下次从这里删
            head, tail = self.freqMap[node.freq - 1]
            if head.nex is tail:  # 这个频率里没有实际节点，只有head,tail
                self.minFreq = node.freq  # 最小频率更新为节点当前频率

    def get(self, key: int) -> int:
        if key in self.keyMap:
            self.increase(self.keyMap[key])
            return self.keyMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.keyMap:  # 有，更新value
                node = self.keyMap[key]
                node.val = value
            else:
                node = Node(key, value)  # 没有，新建一个node
                self.keyMap[key] = node
                self.size += 1
            if self.size > self.capacity:  # 大于容量
                self.size -= 1
                deleted = self.delete(self.freqMap[self.minFreq][0].nex)  # 删除head.nex
                self.keyMap.pop(deleted)
            self.increase(node)
