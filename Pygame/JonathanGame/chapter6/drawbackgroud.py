import sys, random, math, pygame
from pygame import locals

# main program begins
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Orbit Demo")

# load bitmaps
space = pygame.image.load("space.png").convert()
planet = pygame.image.load("planet2.png").convert()
ship = pygame.image.load("freelance.png").convert_alpha()
width, height = ship.get_size()
ship = pygame.transform.smoothscale(ship, (width // 2, height // 2))

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
    width, height = ship.get_size()
    screen.blit(ship, (50, 50))


    pygame.display.update()