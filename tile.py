import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        self.climb = False
        self.sign = [False, "bonjour"]
         
    def update(self, x_shift):
        self.rect.x += x_shift

class Tile_wall(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./alien/boxAlt.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        self.climb = True
        self.sign = [False, "bonjour"]
    def update(self, x_shift):
        self.rect.x += x_shift
        
class Tile_ground(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./alien/sss.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        self.climb = False
        self.sign = [False, "bonjour"]
    def update(self, x_shift):
        self.rect.x += x_shift

class Tile_spike(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./alien/spike.png")
        self.rect = self.image.get_rect(bottomleft = pos)
        self.damage = True
        self.climb = False
        self.sign = [False, "bonjour"]
    def update(self, x_shift):
        self.rect.x += x_shift

class Tile_s(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./alien/yyy.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        self.climb = False
        self.sign = [False, "bonjour"]
    def update(self, x_shift):
        self.rect.x += x_shift

class Tile_earth(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./alien/ground.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        self.climb = True
        
        self.sign = [False, "bonjour"]
    def update(self, x_shift):
        self.rect.x += x_shift

class Tile_checkpoint(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./alien/Sans titre.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        self.climb = False
        
        self.sign = [False, "bonjour"]
 
    def update(self, x_shift):
        self.rect.x += x_shift

class Tile_sign(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./alien/Sans titre.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        self.climb = False
        self.sign = [True, "Use left and right keys to move"]
 
    def update(self, x_shift):
        self.rect.x += x_shift