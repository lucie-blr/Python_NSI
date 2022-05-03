import pygame, sys
from settings import *
from tile import Tile
from level import Level

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill('black')
    level.run()
    
    pygame.display.update()
    clock.tick(60)