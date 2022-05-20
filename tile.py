from re import S
import pygame
from settings import import_folder

#Création des différents type de block avec des class

class Tile(pygame.sprite.Sprite): #Création de la class
    def __init__(self, pos): #Fonction qui se lance au lancement de la classe
        super().__init__() 
        self.image = pygame.image.load("./alien/tile3.png") #Définition de l'image
        self.rect = self.image.get_rect(topleft = pos) #Récupération de la position du coin en bas à gauche de l'image 
        self.damage = False #Définition de si l'objet peut faire des dégats au joueur
        self.climb = False #Définition de si l'objet peut être grimpé par le joueur
        self.sign = [False, ""] #Définition de si l'objet est un panneau et du message de l'objet
        self.open = False
        self.end = False
        self.key = False
        self.door = False
        self.mob = False
         
    def update(self, x_shift): #Fonction qui change les variables de l'objet
        self.rect.x += x_shift #Déplacer les Tiles
        
class Tile_wall(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/wall.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.climb = True
        
class Tile_unc_wall(Tile_wall):
    def __init__(self,pos):
        super().__init__(pos)
        self.climb = False

class Tile_bg_wall(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/wall-ar.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.open = True

class Tile_bg_glass(Tile_bg_wall):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/glass.png")
        self.rect = self.image.get_rect(topleft = pos)

class Tile_ground(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/sss3.png")
        self.rect = self.image.get_rect(topleft = pos)

class Tile_s(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/yyy.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class Tile_earth(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/ground3.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.climb = True

class Tile_checkpoint(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/Sans titre.png")
        self.rect = self.image.get_rect(topleft = pos)
        
class Tile_sign(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/sign.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.sign[0] = True
        self.open = True

class Tile_end(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/flag.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.end = True
        
class Tile_key(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/key.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.key = True
        self.open = True
        
class Tile_door(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.open_image = pygame.image.load("./alien/door.png")
        self.image = pygame.image.load("./alien/close_door.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.door = True
       
class Tile_box(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/boxAlt.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.mob = True

#### SPIKES #### 
class Tile_spike(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/spike.png")
        self.rect = self.image.get_rect(bottomleft = pos)
        self.damage = True

class Tile_fake_spike(Tile_spike):
    def __init__(self, pos):
        super().__init__(pos)
        self.damage = False
        self.open = True

class Tile_left_spike(Tile_spike):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/left_spike.png")
        self.rect = self.image.get_rect(bottomleft = pos)

class Tile_right_spike(Tile_spike):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/right_spike.png")
        self.rect = self.image.get_rect(bottomleft = pos)

class Tile_bottom_spike(Tile_spike):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/down_spike.png")
        self.rect = self.image.get_rect(bottomleft = pos)



#MOBS        
class Mob(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load("./alien/slime/slime3.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.damage = True
        self.mob = True
        self.speed = 5
        self.move = 0
        self.animation = 0
        self.right = True
        
        self.full_path = './alien/slime'
        self.animations = import_folder(self.full_path)
        
    def update(self, x_shift):
        self.rect.x += self.speed + x_shift
        if self.move < 30:
            self.move += 1
        else:
            self.speed = self.speed * -1
            self.move = 0
            if self.right:
                self.right = False
            else:
                self.right = True
            
        if self.animation < len(self.animations):
            image = self.animations[int(self.animation)]
            self.animation += 0.15
            if self.right: #si le joueur est tourné vers la droite, retourner l'image
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image
            else:
                self.image = image
                
        else:
            self.animation = 0