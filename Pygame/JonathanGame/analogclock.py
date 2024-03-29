import sys, random, math, pygame
from pygame import locals

# main program begins
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Circle Demo")
screen.fill((0, 0, 100))


pos_x = 300
pos_y = 250
radius = 200
angle = 360
color = 240, 240, 240

# repeating loop
while True:
    for event in pygame.event.get():
        if event.type == locals.QUIT:
            sys.exit()
        keys = pygame.key.get_pressed()
        if keys[locals.K_ESCAPE]:
            sys.exit()

    # increment angle
    angle += 1
    if angle >= 360:
        angle = 0
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = r, g, b
    # calculate coordinates
    x = math.cos(math.radians(angle)) * radius
    y = math.sin(math.radians(angle)) * radius

    # draw one step around the circle
    pos = int(pos_x + x), int(pos_y + y)
    print(pos)
    pygame.draw.circle(screen, color, pos, 10, 0)

    pygame.display.update()