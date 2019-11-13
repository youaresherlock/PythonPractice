#!usr/bin/python
# -*- coding:utf8 -*-

# 行为型设计模式

class Publisher: # 发布者
    def __init__(self):
        self.observers = [] # 观察者

    def add(self, observer): # 加入观察者
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add : {}'.format(observer))

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    def notify(self): # 调用观察者的回调
        [o.notify_by(self) for o in self.observers]

class Formatter(Publisher): # 继承自发布者
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        self._data = int(new_value)
        self.notify() # data在被合法赋值以后会执行notify方法


class BinaryFormatter:
    """ 订阅者 """
    def notify_by(self, publisher):
        print("{}: '{}' has now bin data = {}".format(
            type(self).__name__,
            publisher.name,
            bin(publisher.data)
        ))

def test():
    df = Formatter('formatter') # 发布者
    bf = BinaryFormatter() # 订阅者
    df.add(bf) # 添加订阅者
    df.data = 3 # 设置的时候调用订阅者的notify_by

"""
BinaryFormatter: 'formatter' has now bin data = 0b11
"""

def ten_percent_discount(order):
    return order.price * 0.10

def on_sale_discount(order):
    return order.price * 0.25 + 20

class Order:
    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        return self.price - discount

    def __repr__(self):
        fmt = '<Price: {}, price after discount: {}>'
        return fmt.format(
            self.price, self.price_after_discount()
        )

def main():
    order0 = Order(100)
    order1 = Order(100, discount_strategy=ten_percent_discount)
    order2 = Order(100, discount_strategy=on_sale_discount)
    print(order0)
    print(order1)
    print(order2)


if __name__ == '__main__':
    test()
    main()




















