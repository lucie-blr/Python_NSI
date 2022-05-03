import pygame
import time

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load("./alien/p1_front.png")
        self.rect = self.image.get_rect(topleft = pos)
        
        #mouvement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16
        self.double_jump = 1
        self.time = time.time()
        print(self.time)
        print(self.double_jump)
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_UP] and self.double_jump == 1:
            if self.direction.y == 0:
                self.jump()
            print(self.double_jump)
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
        self.rect.x += self.direction.x * self.speed