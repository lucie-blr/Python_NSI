import pygame
import time
import os

def import_folder(path):
    surface_list = []
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    
    return surface_list

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.status = 'idle'
        
        #mouvement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16
        self.double_jump = 1
        self.time = time.time()            
    
    def import_character_assets(self):
        character_path='./alien/'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[]}
        
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
    
    def animate(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
    
    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 0:
            self.status = 'fall'
        elif self.direction.x != '0':
            self.status = 'run'
        else:
            self.status = 'idle'
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.image = pygame.image.load("./alien/right.png")
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.image = pygame.image.load("./alien/left.png")
        else:
            self.direction.x = 0
        
        if keys[pygame.K_UP] and self.double_jump == 1:
            if self.direction.y == 0:
                self.jump()
            if self.direction.y != 0:
                if time.time() > (self.time + 0.2):
                    self.double_jump = 0
                    self.jump()
            
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y = self.jump_speed
    
    def update(self):
        self.get_input()
        self.animate()
        self.get_status()
        self.rect.x += self.direction.x * self.speed
        