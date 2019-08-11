import sys
import pygame
from pygame import locals

pygame.init()

screen = pygame.display.set_mode((600, 500))

myFont = pygame.font.Font(None, 60)
white = 255, 255, 255
blue = 0, 0, 255
textImage = myFont.render("Hello Pygame", True, white)

while True:
    for event in pygame.event.get():
        if event.type in (locals.QUIT, locals.KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    pygame.display.update()
