import sys
import math
import pygame
from pygame import locals

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Arcs")

while True:
    for event in pygame.event.get():
        if event.type in (locals.QUIT, locals.KEYDOWN):
            sys.exit()

    screen.fill((0, 0, 200))

    # draw the arc
    color = 255, 0, 255
    position = 200, 150, 200, 200
    start_angle = math.radians(0)
    end_angle = math.radians(270)
    width = 5
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)

    pygame.display.update()