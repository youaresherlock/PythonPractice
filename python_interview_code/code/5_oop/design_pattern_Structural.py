#!usr/bin/python
# -*- coding:utf8 -*-

# 适配器模式的例子
class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Adapter:
    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        print('enter init')
        self.obj = obj
        print('first', self.__dict__,self.obj.__dict__)
        self.__dict__.update(adapted_methods)
        print('second', self.__dict__)
        print('leave init')

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)
        # print('attr: {}'.format(attr))
        # return self.obj.name

objects = []
dog = Dog()
print(dog.bark, dog.__dict__, getattr(dog, 'bark'))
objects.append(Adapter(dog, make_noise=dog.bark))
cat = Cat()
objects.append(Adapter(cat, make_noise=cat.meow))
for obj in objects:
    print("A {0} goes {1}".format(obj.name, obj.make_noise()))

"""
<bound method Dog.bark of <__main__.Dog object at 0x0000025EBDDD1B00>> {'name': 'Dog'} <bound method Dog.bark of <__main__.Dog object at 0x0000025EBDDD1B00>>
enter init
first {'obj': <__main__.Dog object at 0x0000025EBDDD1B00>} {'name': 'Dog'}
second {'obj': <__main__.Dog object at 0x0000025EBDDD1B00>, 'make_noise': <bound method Dog.bark of <__main__.Dog object at 0x0000025EBDDD1B00>>}
leave init
enter init
first {'obj': <__main__.Cat object at 0x0000025EBDDD1BA8>} {'name': 'Cat'}
second {'obj': <__main__.Cat object at 0x0000025EBDDD1BA8>, 'make_noise': <bound method Cat.meow of <__main__.Cat object at 0x0000025EBDDD1BA8>>}
leave init
A Dog goes woof!
A Cat goes meow!
"""