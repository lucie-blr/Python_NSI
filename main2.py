from turtle import width
import pygame
from tile import *
from settings import *
from player import Player
import time
import sys

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup(level_data)
        self.world_shift = 0
        
    def setup(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index, cell in enumerate(row): 
                if cell == 'T':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'G':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_ground((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'W':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_wall((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if cell == 'S':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_spike((x,y),tile_size)
                    self.tiles.add(tile)
        
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx 
        direction_x = player.direction.x
        
        if player_x < width / 5 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        
        elif player_x > width - (width / 5) and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        
        else:
            self.world_shift = 0
            player.speed = 5
        
    def horizontal_mouvement_collision(self):
        player = self.player.sprite
        
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if sprite.damage == True:
                    pygame.quit()
                    sys.exit()
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        
    def vertical_mouvement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if sprite.damage == True:
                    start()
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.double_jump = 1
                    player.time = time.time()
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    
    
    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        
        self.player.update()
        self.horizontal_mouvement_collision()
        self.vertical_mouvement_collision()
        self.player.draw(self.display_surface)

def start():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    level = Level(level_map_2, screen)
    bg = pygame.image.load("./alien/background.jpg")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill('black')
        screen.blit(bg,(0,0))
        level.run() 
        
        pygame.display.update()
        clock.tick(60)

start()