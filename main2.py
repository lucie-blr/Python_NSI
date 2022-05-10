import pygame
from tile import *
from settings import *
from player import Player
import time
import sys

class Level:
    def __init__(self, level_data, surface, spawn):
        self.display_surface = surface
        self.spawn = spawn
        self.setup(level_data, spawn)
        self.world_shift = 0
        
        
        
    def setup(self, layout, spawn):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        messages = ["prout","Press directional keys to move.","prout3"]
        sign_index = 0
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
                if cell == 'E':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_earth((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'W':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_wall((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'L':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_sign((x,y),tile_size)
                    tile.sign[1] = messages[sign_index]

                    self.tiles.add(tile)
                    sign_index = sign_index + 1
                if cell == 'P':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    
                    player_sprite = Player((x,y))
                        
                    self.player.add(player_sprite)
                    print(self.spawn)
                if cell == 'S':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_spike((x,y+48),tile_size)
                    self.tiles.add(tile)
                if cell == 'Y':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_s((x,y),tile_size)
                    self.tiles.add(tile)
        
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx 
        direction_x = player.direction.x
        width, h = pygame.display.get_surface().get_size()
        
        if player_x < width / 3 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        
        elif player_x > width - (width / 2) and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        
        else:
            self.world_shift = 0
            player.speed = 5
        
    def horizontal_mouvement_collision(self,screen):
        player = self.player.sprite
        
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if sprite.sign[0]:
                    
                    text_font = pygame.font.Font(None, 60)  #Text Font
                    white = (255,255,255)
                    text = text_font.render(sprite.sign[1], True, white)
                    textRect = text.get_rect()
                    textRect.center = (sprite.rect.x, sprite.rect.y - 96)
                    screen.blit(text, textRect)
                else:    
                    
                    if sprite.damage == True:
                        
                        #Death animation
                        player.status = 'death'
                        print(player.death)
                        if player.death == 20:
                            
                            main(self.spawn)  
                    
                    else:    

                        if player.direction.x < 0:
                            player.rect.left = sprite.rect.right
                            if sprite.climb:
                                player.direction.y = 1
                                player.double_jump = 1
                        elif player.direction.x > 0:
                            player.rect.right = sprite.rect.left
                            if sprite.climb:
                                player.direction.y = 1
                                player.double_jump = 1
            else: player.gravity = 0.8
                    
                    
        
    def vertical_mouvement_collision(self,screen):
        player = self.player.sprite
        player.apply_gravity()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if sprite.sign[0]:
                    
                    text_font = pygame.font.Font(None, 60)  #Text Font
                    white = (255,255,255)
                    text = text_font.render(sprite.sign[1], True, white)
                    textRect = text.get_rect()
                    textRect.center = (sprite.rect.x, sprite.rect.y - 96)
                    screen.blit(text, textRect)
                else:    
                    
                    if sprite.damage == True:
                    #Death animation
                        player.status = 'death'
                    if player.death == 20:
                        main(self.spawn)  
                        
                    else:
                        if player.direction.y > 0:
                            player.rect.bottom = sprite.rect.top
                            player.direction.y = 0
                            player.double_jump = 1
                            player.time = time.time()
                        elif player.direction.y < 0:
                            player.rect.top = sprite.rect.bottom
                            player.direction.y = 0
                    
    
    def run(self,screen):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        
        self.player.update()
        self.horizontal_mouvement_collision(screen)
        self.vertical_mouvement_collision(screen)
        self.player.draw(self.display_surface)
        

def main(spawn):
    pygame.init()
    '''
    width = input("Width (\"full\" to get fullscreen):")
    if width == "full":
        screen = pygame.display.set_mode()
    else:
        width = int(width)
        height = int(input("Height :"))
        screen = pygame.display.set_mode((width, height))
    '''
    screen = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()
    level = Level(level_map, screen, spawn)
    width, height = screen.get_size()
    bg = pygame.image.load("./alien/background.jpg")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill('black')
        screen.blit(bg,(0,0))
        level.run(screen) 
        
        pygame.display.update()
        clock.tick(60)
        
if __name__ == "__main__":
    spawn = "null"
    main(spawn)
