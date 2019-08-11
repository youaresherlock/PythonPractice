'''
使用多继承中，我们基本不会使用super()来调用
父类中的任何内容.除非每个父类中的变量和方法
都是独特的
'''
class Point(object):
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Point constructor")

    def ToString(self):
        return "{X:" + str(self.x) + ",Y:" + str(self.y) + "}"

class Size(object):
    width = 0.0
    height = 0.0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        print("Size constructor")

    def ToString(self):
        return "{WIDTH=" + str(self.width) + \
            ",HEIGHT=" + str(self.height) + "}"


class Rectangle(Point, Size):
    def __init__(self, x, y, width, height):
        Point.__init__(self, x, y)
        Size.__init__(self, width, height)
        print("Rectangle constructor")
        self.x = 10
        self.y = 20

    def ToString(self):
        return Point.ToString(self) + "," + Size.ToString(self)

r = Rectangle(250, 200, 40, 50)
print(r.ToString())

