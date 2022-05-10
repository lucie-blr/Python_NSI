import pygame
import time
import os
from settings import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        self.status = 'idle'
        self.facing_right = True
        self.death = 0
        
        #mouvement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16
        self.double_jump = 1
        self.time = time.time()            
    
    def import_character_assets(self):
        self.character_path='./alien/'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[], 'death':[]}
        
        
        for animation in self.animations.keys():
            self.full_path = self.character_path + animation
            self.animations[animation] = import_folder(self.full_path)
            
        
    
    def animate(self):
        
        animation = self.animations[self.status]
        if self.status == 'death':
            print(self.death)
            if self.death < 20:
                self.image = animation[int(self.death)]
                time.sleep(0.02)
                
                self.death = self.death + 1
                self.direction.x = 0
                self.direction.y = 0
            return
        elif self.death == 0:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(animation):
                self.frame_index = 0
            
            image = animation[int(self.frame_index)]
        
            if self.facing_right:
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image
            else:
                self.image = image
    
    def get_status(self):
        if self.death == 0:
            if self.direction.y < 0:
                self.status = 'jump'
            elif self.direction.y > 1:
                self.status = 'fall'
            elif self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            self.direction.x=0
        
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
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
        if self.death == 0:
            self.get_input()
        self.animate()
        self.get_status()
        self.rect.x += self.direction.x * self.speed
        