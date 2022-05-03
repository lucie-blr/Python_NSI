import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)
        
    def update(self, x_shift):
        self.rect.x += x_shift

class Tile_wall(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./alien/boxAlt.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        
    def update(self, x_shift):
        self.rect.x += x_shift
        
class Tile_ground(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./alien/sss.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        
    def update(self, x_shift):
        self.rect.x += x_shift

class Tile_spike(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = True
        
    def update(self, x_shift):
        self.rect.x += x_shift