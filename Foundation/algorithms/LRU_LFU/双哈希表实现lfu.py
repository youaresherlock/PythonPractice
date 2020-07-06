import collections


class Node:
    def __init__(self, key, val, pre=None, nex=None, freq=0):
        self.pre = pre
        self.nex = nex
        self.freq = freq  # ��ǰ�ڵ�ʹ��Ƶ��
        self.val = val
        self.key = key

    # ����ڵ�
    # self-> nex-> self.nex
    def insert(self, nex):
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex


# ����˫����������ֵΪ0��head��tail
def create_linked_list():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nex = tail
    tail.pre = head
    return (head, tail)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0  # ��ֵ������
        self.minFreq = 0  # ��¼��С��Ƶ�ʣ�ÿ���������ˣ�ɾ���Ƶ�ʵ�head.nex
        self.freqMap = collections.defaultdict(
            create_linked_list)  # key��Ƶ�ʣ�ֵ��һ��˫�������head, tail����������Ľڵ����tailǰ�棬��head.nex����Сʹ��Ƶ�ʵĽڵ㣬ɾ��ʱɾhead.nex
        self.keyMap = {}  # �洢��ֵ�ԣ�ֵ��node ����

    # ˫��������ɾ��ָ���ڵ�
    def delete(self, node):
        if node.pre:  # ���ǵ�һ���ڵ㣬����Ҫɾ����
            node.pre.nex = node.nex  # ǰ��ǰ������
            node.nex.pre = node.pre
            if node.pre is self.freqMap[node.freq][0] and node.nex is self.freqMap[node.freq][
                -1]:  # �µ�Ƶ�����Ѵ�������ڵ㣬��ֻ������ڵ㣬�Ǿ�ֱ�Ӱ������Ƶ��ɾ����������������������
                self.freqMap.pop(node.freq)
        return node.key

    # ����
    def increase(self, node):
        node.freq += 1  # ��ǰ�ڵ�Ƶ��+1
        self.delete(node)  # ��Ƶ���У�ɾ���˽ڵ�
        self.freqMap[node.freq][-1].pre.insert(node)  # ��Ƶ���У�tail�ڵ�ǰ���뵱ǰ�ڵ�
        if node.freq == 1:  # ����Ƶ��Ϊ1���ˣ���¼һ�£��´����������ȴ�����ɾ
            self.minFreq = 1
        elif self.minFreq == node.freq - 1:  # ������СƵ�ʵĽڵ�ʱ���Ӿ�Ƶ�ʵ���Ƶ��ʱ��Ҫ����¾�Ƶ�ʣ�ֻ��head,tail�Ͳ����ܴ�����ɾ�����ˣ��Ǿ���Ҫ��minFreq����Ϊ��Ƶ�ʣ��´δ�����ɾ
            head, tail = self.freqMap[node.freq - 1]
            if head.nex is tail:  # ���Ƶ����û��ʵ�ʽڵ㣬ֻ��head,tail
                self.minFreq = node.freq  # ��СƵ�ʸ���Ϊ�ڵ㵱ǰƵ��

    def get(self, key: int) -> int:
        if key in self.keyMap:
            self.increase(self.keyMap[key])
            return self.keyMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.keyMap:  # �У�����value
                node = self.keyMap[key]
                node.val = value
            else:
                node = Node(key, value)  # û�У��½�һ��node
                self.keyMap[key] = node
                self.size += 1
            if self.size > self.capacity:  # ��������
                self.size -= 1
                deleted = self.delete(self.freqMap[self.minFreq][0].nex)  # ɾ��head.nex
                self.keyMap.pop(deleted)
            self.increase(node)
