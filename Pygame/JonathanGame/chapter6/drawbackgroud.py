import sys, random, math, pygame
from pygame import locals

class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # x property
    def getx(self):
        return self.__x
    def setx(self, x):
        self.__x = x
    x = property(getx, setx)

    # y property
    def gety(self):
        return self.__y
    def sety(self, y):
        self.__y = y
    y = property(gety, sety)

    def __str__(self):
        """ 输出对象的描述信息 """
       # str.format()格式化输出 不带小数输出
        return "{X:" + "{:.0f}".format(self.__x) + \
    ",Y:" + "{:.0f}".format(self.__y) + "}"

# print_text function
def print_text(font, x, y, text, color=(255,255,255)):
    """
    python引用变量的顺序: 当前作用域局部变量->外层作用域变量->
    当前模块中的全局变量
    global 关键字用来在函数或其他局部作用域中使用全局变量
    但是如果不修改全局变量也可以不适用global关键字
    """
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

# wrap_angle function
def wrap_angle(angle):
    return angle % 360

# main program begins
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Orbit Demo")
font = pygame.font.Font(None, 18)

# load bitmaps
space = pygame.image.load("space.png").convert()
planet = pygame.image.load("planet2.png").convert()
ship = pygame.image.load("freelance.png").convert_alpha()
width, height = ship.get_size()
ship = pygame.transform.smoothscale(ship, (width // 2, height // 2))

radius = 250
angle = 0.0
pos = Point(0, 0)
old_pos = Point(0, 0)

# repeating loop
while True:
    for event in pygame.event.get():
        if event.type == locals.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[locals.K_ESCAPE]:
        sys.exit()

    # draw background
    screen.blit(space, (0, 0))
    width, height = planet.get_size()
    screen.blit(planet, (400 - width / 2, 300 - height / 2))

    # move the ship
    angle = wrap_angle(angle - 0.1)
    pos.x = math.sin(math.radians(angle)) * radius
    pos.y = math.cos(math.radians(angle)) * radius
    # rotate the ship
    delta_x = pos.x - old_pos.x
    delta_y = pos.y - old_pos.y
    rangle = math.atan2(delta_y, delta_x)
    rangled = wrap_angle(-math.degrees(rangle))
    scratch_ship = pygame.transform.rotate(ship, rangled)

    # draw the ship
    width, height = scratch_ship.get_size()
    x = 400 + pos.x - width // 2
    y = 300 + pos.y - height // 2
    screen.blit(scratch_ship, (x, y))

    print_text(font, 0, 0, "Orbit: " + "{:.0f}".format(angle))
    print_text(font, 0, 20, "Rotation: " + "{:.2f}".format(rangle))
    print_text(font, 0, 40, "Position: " + str(pos))
    print_text(font, 0, 60, "Old Pos: " + str(old_pos))

    pygame.display.update()

    # remember position
    old_pos.x, old_pos.y = pos.x, pos.y