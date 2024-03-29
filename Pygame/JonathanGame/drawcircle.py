import sys
import pygame
from pygame import locals

pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Circles")

while True:
    for event in pygame.event.get():
        if event.type in (locals.QUIT, locals.KEYDOWN):
            sys.exit()
    screen.fill((0, 0, 200))

    # draw a circle
    color = 255, 255, 0
    position = 300, 250
    radius = 100
    width = 10
    pygame.draw.circle(screen, color, position, radius, width)

    pygame.display.update()
