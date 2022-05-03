import pygame
from tile import Tile

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup(level_data)
        
    def setup(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index, cell in enumerate(row): 
                print(f'{row_index}/{col_index}:{cell}')
        
    def run(self):
        self.tiles.draw(self.display_surface)