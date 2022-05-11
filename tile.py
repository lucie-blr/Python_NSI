import pygame

#Création des différents type de block avec des class

class Tile(pygame.sprite.Sprite): #Création de la class
    def __init__(self, pos, size): #Fonction qui se lance au lancement de la classe
        super().__init__() 
        self.image = pygame.image.load("./alien/tile.png") #Définition de l'image
        self.rect = self.image.get_rect(topleft = pos) #Récupération de la position du coin en bas à gauche de l'image 
        self.damage = False #Définition de si l'objet peut faire des dégats au joueur
        self.climb = False #Définition de si l'objet peut être grimpé par le joueur
        self.sign = [False, "bonjour"] #Définition de si l'objet est un panneau et du message de l'objet
         
    def update(self, x_shift): #Fonction qui change les variables de l'objet
        self.rect.x += x_shift #Déplacer les tiles

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
        self.image = pygame.image.load("./alien/sign.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        self.climb = False
        self.sign = [True, "Use left and right keys to move"]
 
    def update(self, x_shift):
        self.rect.x += x_shift
        
class Tile_end(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./alien/flag.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        self.climb = False
        self.sign = [False, "Use left and right keys to move"]
        self.end = True
 
    def update(self, x_shift):
        self.rect.x += x_shift
        
class Tile_key(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./alien/sign.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        self.climb = False
        self.sign = [False, "Use left and right keys to move"]
        self.key = True
 
    def update(self, x_shift):
        self.rect.x += x_shift

class Tile_door(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("./alien/sign.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = False
        self.climb = False
        self.sign = [False, "Use left and right keys to move"]
        self.door = True
 
    def update(self, x_shift):
        self.rect.x += x_shift