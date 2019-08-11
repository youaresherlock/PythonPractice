import sys
import random
import pygame
from pygame import locals

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Rectangles")

pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1
init_color = (255, 255, 0)
random_color = [(255, 193, 193), (60, 179, 113), (180, 238, 180), (135, 206, 250)]

clock = pygame.time.Clock()

while True:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type in (locals.QUIT, locals.KEYDOWN):
            sys.exit()

    screen.fill((174, 238, 238))

    # move the rectangle
    pos_x += vel_x
    pos_y += vel_y

    # keep rectangle on the screen
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y

    if pos_x > 500 or pos_x < 0 or pos_y > 400 or pos_y < 0:
        index = random.randint(0, len(random_color) - 1)
        init_color = random_color[index]

    # draw the rectangle
    width = 0 #solid fill
    pos = pos_x, pos_y, 100, 100
    pygame.draw.rect(screen, init_color, pos, width)

    pygame.display.update()


