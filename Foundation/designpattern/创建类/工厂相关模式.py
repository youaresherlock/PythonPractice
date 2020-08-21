#!usr/bin/python
# -*- coding:utf8 -*-
"""
factory pattern工厂模式, 我们在创建对象时不会对客户端暴露创建逻辑,并且是通过使用一个
共同的接口来指向新创建的对象
意图：定义一个创建对象的接口，让其子类自己决定实例化哪一个工厂类，工厂模式使其创建过程延迟到子类进行。

主要解决：主要解决接口选择的问题。

何时使用：我们明确地计划不同条件下创建不同实例时。

如何解决：让其子类实现工厂接口，返回的也是一个抽象的产品。

关键代码：创建过程在其子类执行。

复杂对象适合使用工厂模式,而简单对象只需要通过new就可以完成创建
"""


class Burger():
    """
    汉堡
    """
    name=""
    price=0.0
    type='BURGER'

    def getPrice(self):
        return self.price

    def setPrice(self,price):
        self.price=price

    def getName(self):
        return self.name


class cheeseBurger(Burger):
    def __init__(self):
        self.name="cheese burger"
        self.price=10.0


class spicyChickenBurger(Burger):
    def __init__(self):
        self.name="spicy chicken burger"
        self.price=15.0


class Snack():
    """
    小食类
    """
    name = ""
    price = 0.0
    type = "SNACK"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0


class Beverage():
    """
    饮料
    """
    name = ""
    price = 0.0
    type = "BEVERAGE"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0


class foodFactory():
    """
    抽象工厂foodFactory为抽象的工厂类，而burgerFactory，snackFactory，beverageFactory为具体的工厂类。
    """
    type=""

    def createFood(self,foodClass):
        print(self.type," factory produce a instance.")
        foodIns=foodClass()
        return foodIns


class burgerFactory(foodFactory):
    def __init__(self):
        self.type="BURGER"


class snackFactory(foodFactory):
    def __init__(self):
        self.type="SNACK"


class beverageFactory(foodFactory):
    def __init__(self):
        self.type="BEVERAGE"


if  __name__=="__main__":
    burger_factory=burgerFactory()
    snack_factory=snackFactory()
    beverage_factory=beverageFactory()
    cheese_burger=burger_factory.createFood(cheeseBurger)
    print(cheese_burger.getName(),cheese_burger.getPrice())
    chicken_wings=snack_factory.createFood(chickenWings)
    print(chicken_wings.getName(),chicken_wings.getPrice())
    coke_drink=beverage_factory.createFood(coke)
    print(coke_drink.getName(),coke_drink.getPrice())








































