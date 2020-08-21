#!usr/bin/python
# -*- coding:utf8 -*-
"""
singleton pattern
这种模式涉及到一个单一的类,该类负责创建自己的对象,同时确保只有单个对象
被创建.
意图：保证一个类仅有一个实例，并提供一个访问它的全局访问点。

主要解决：一个全局使用的类频繁地创建与销毁。

何时使用：当您想控制实例数目，节省系统资源的时候。

如何解决：判断系统是否已经有这个单例，如果有则返回，如果没有则创建。

关键代码：构造函数是私有的。
"""
import threading
import time


#这里使用方法__new__来实现单例模式
class Singleton(object):#抽象单例
    def __new__(cls, *args, **kwarg):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwarg)
        return cls._instance


#总线
class Bus(Singleton):
    lock = threading.RLock()

    def sendData(self,data):
        self.lock.acquire()
        time.sleep(3)
        print("Sending Signal Data...",data)
        self.lock.release()


#线程对象，为更加说明单例的含义，这里将Bus对象实例化写在了run里
class VisitEntity(threading.Thread):
    my_bus=""
    name=""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name=name

    def run(self):
        self.my_bus=Bus()
        self.my_bus.sendData(self.name)


if  __name__=="__main__":
    for i in range(3):
        print("Entity %d begin to run..."%i)
        my_entity=VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()