#!usr/bin/python
# -*- coding:utf8 -*-

# 一个工厂方法的例子
class DogToy:
    def speak(self):
        print('wang wang')

class CatToy:
    def speak(self):
        print('miao miao')

def toy_factory(toy_type):
    if toy_type == 'dog':
        return DogToy()
    elif toy_type == 'cat':
        return CatToy()

# 一个构造模式的例子
class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None # in gigabytes
        self.hdd = None  # in gigabytes
        self.gpu = None

    def __str__(self):
        info = ('Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AG23385193')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory),
                           self.builder.configure_hdd(hdd),
                           self.builder.configure_gpu(gpu))]

    @property
    def computer(self):
        return self.builder.computer

# 使用builder, 可以创建多个builder类实现不同的组装方式
engineer = HardwareEngineer()
engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
computer = engineer.computer
print(computer)

# 单例模式
class Singleton:
    def __init__(self):
        self.instance = []

    def __call__(self, cls):
        def wrapper(*args, **kwargs):
            if self.instance:
                result = self.instance[0]
            else:
                result = cls(*args, **kwargs)
                self.instance.append(result)
            return result
        return wrapper

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            _instance = super().__new__(cls, *args, **kwargs)
            cls._instance = _instance
        return cls._instance

class MyClass(Singleton):
    pass

c1 = MyClass()
c2 = MyClass()
assert c1 is c2 # 单例的, c1 c2同一个实例

# x(arg1, arg2) 相当于 x.__call__(arg1, arg2) x是实例
# 使用类装饰器实现单例模式
@Singleton()
class YourClass():
    def __init__(self, test):
        self.test =test

y1 = YourClass('sete')
y2 = YourClass()
print(id(y1), id(y2), y1.test, y2.test)



















