import pygame
from tile import *
from settings import *
from player import Player, Bullet
import time
import sys
import run
import select
import button
import json
import button
from PIL import Image
from datetime import datetime

class Level:
    def __init__(self, level_data, surface, spawn):
        self.display_surface = surface
        self.spawn = spawn
        self.setup(level_data, surface)
        self.world_shift = 0
        
        
    def setup(self, layout_index, screen):
        self.tiles = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        messages = levelsign[layout_index]
        sign_index = 0
        self.layout_index = layout_index
        print(len(levelmap), layout_index)
        layout = levelmap[layout_index]
        self.bullet = pygame.sprite.GroupSingle()
        
        with open("data.json", "r") as f:	#config size screen
            data = json.load(f)
            FULL = data["FULL"]
            WIDTH = data["WIDTH"]
            
        y_patch = 0
        x_patch = 0
        if FULL == "True" or WIDTH==1920:
            y_patch = 0
        elif WIDTH==1280:
            y_patch = - 3
            x_patch = 9
        elif WIDTH==1000:
            y_patch = - 4
            x_patch = 12
        y_patch = y_patch * tile_size
        x_patch = x_patch * tile_size
        
        for row_index,row in enumerate(layout):
            for col_index, cell in enumerate(row): 
                if cell == 'T':
                    x = col_index * tile_size - x_patch 
                    y = row_index * tile_size + y_patch
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'G':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_ground((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'E':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_earth((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'W':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_wall((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'U':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_unc_wall((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'A':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_bg_wall((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'V':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_bg_glass((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'L':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_sign((x,y),tile_size)
                    tile.sign[1] = messages[sign_index]
                    self.tiles.add(tile)
                    print(sign_index)
                    sign_index = sign_index + 1
                if cell == 'P':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    
                    player_sprite = Player((x,y))
                        
                    self.player.add(player_sprite)
                    print(self.spawn)
                if cell == '↑':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_spike((x,y+48),tile_size)
                    self.tiles.add(tile)
                if cell == '↟':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_fake_spike((x,y+48),tile_size)
                    self.tiles.add(tile)
                if cell == '→':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_right_spike((x,y+48),tile_size)
                    self.tiles.add(tile)
                if cell == '←':
                    x = col_index * tile_size - x_patch + 24
                    y = row_index * tile_size + y_patch
                    tile = Tile_left_spike((x,y+48),tile_size)
                    self.tiles.add(tile)
                if cell == '↓':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch - 24
                    tile = Tile_bottom_spike((x,y+48),tile_size)
                    self.tiles.add(tile)
                if cell == 'Y':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_s((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'F':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_end((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'B':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    player_sprite = Bullet((x,y))
                    self.bullet.add(player_sprite)
                if cell == 'D':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_door((x,y), tile_size)
                    self.tiles.add(tile)
                if cell == 'K':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Tile_key((x,y), tile_size)
                    self.tiles.add(tile)
                if cell == 'M':
                    x = col_index * tile_size - x_patch
                    y = row_index * tile_size + y_patch
                    tile = Mob((x,y), tile_size)
                    self.mobs.add(tile)
    def scroll_x(self):
        player = self.player.sprite
        bullet = self.bullet.sprite
        player_x = player.rect.centerx 
        direction_x = player.direction.x
        width, h = pygame.display.get_surface().get_size()
        
        if player_x < width / 3 and direction_x < 0:
            self.world_shift = 5
            bullet.speed = bullet.speed - player.speed
            player.speed = 0
        
        elif player_x > width - (width / 2) and direction_x > 0:
            self.world_shift = -5
            bullet.speed = bullet.speed - player.speed
            player.speed = 0
        
        else:
            self.world_shift = 0
            player.speed = 5
            bullet.speed = 15
        
    def horizontal_mouvement_collision(self,screen, level_map):
        player = self.player.sprite
        bullet = self.bullet.sprite
        
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.mobs.sprites():
            if sprite.rect.colliderect(player.rect):
                if sprite.damage == True:
                    #Death animation
                    player.status = 'death'
                    if player.death == 20:
                        main(self.layout_index)  
            if sprite.rect.colliderect(bullet.rect):
                try:
                    if sprite.mob:
                        sprite.rect.y = 2000
                        player.coin += 1
                        with open("data.json", "r") as f:	#open and read
                            data = json.load(f)
                        data["coin"] += 1
                        with open("data.json", "w") as f:	#add coin
                            json.dump(data,f)
                except AttributeError:
                    pass
        
        for sprite in self.tiles.sprites():
            
            
            
            if sprite.rect.colliderect(player.rect):
                try: #end
                    if sprite.end:
                        with open("data.json", "r") as f:	#config size screen
                            data = json.load(f)
                            WIDTH = data["WIDTH"]
                            HEIGHT = data["HEIGHT"]
                        text_font = pygame.font.Font(None, 60)  #Text Font
                        white = (255,255,255)
                        text = text_font.render("Level finished !", True, white)
                        textRect = text.get_rect()
                        textRect.center = (WIDTH/2, HEIGHT/2)
                        screen.blit(text, textRect)
                        player.speed = 0
                        player.status = "idle"
                        self.world_shift = 0
                        if player.death == 4:
                            level_map = level_map + 1
                            data["unlock"][0][f"map{level_map}"] = "True"
                            with open (f"data.json", "w") as f:
                                json.dump(data,f)
                            select.main()
                        
                except AttributeError: 
                    
                
                    try:
                        if sprite.key:
                            player.key = player.key + 1
                            sprite.rect.y = sprite.rect.y + 2000
                            
                    except AttributeError:
                        pass
                    
                    try:
                        if sprite.door:
                            if player.key > 0:
                                player.key -= 1
                                sprite.door = False
                                sprite.image = sprite.open_image
                                sprite.open = True
                                
                    
                    except AttributeError:
                        pass
                    
                    if sprite.sign[0]:
                        
                        text_font = pygame.font.Font(None, 40)  #Text Font
                        white = (255,255,255)
                        text = text_font.render(sprite.sign[1], True, white)
                        textRect = text.get_rect()
                        textRect.center = (sprite.rect.x, sprite.rect.y - 48)
                        screen.blit(text, textRect)
                        
                    else:    
                        
                        if sprite.damage == True:
                            
                            #Death animation
                            player.status = 'death'
                            if player.death == 20:
                                
                                main(self.layout_index)  
                        
                        else:    
                            
                            try:
                                if sprite.open:
                                    pass
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
                            except AttributeError: 
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
                    
                    
        
    def vertical_mouvement_collision(self,screen, level_map):
        player = self.player.sprite
        player.apply_gravity()
        
        for sprite in self.mobs.sprites():
            if sprite.rect.colliderect(player.rect):
                if sprite.damage == True:
                    #Death animation
                    pygame.mixer.music.pause()
                    player.status = 'death'
                    if player.death == 20:
                        main(self.layout_index)  
                
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                try:
                    if sprite.end:
                        with open("data.json", "r") as f:	#config size screen
                            data = json.load(f)
                            WIDTH = data["WIDTH"]
                            HEIGHT = data["HEIGHT"]
                        text_font = pygame.font.Font(None, 60)  #Text Font
                        white = (255,255,255)
                        text = text_font.render("Level finished !", True, white)
                        textRect = text.get_rect()
                        textRect.center = (WIDTH/2, HEIGHT/2)
                        screen.blit(text, textRect)
                        player.speed = 0
                        player.status = "win"
                        self.world_shift = 0
                        if player.death == 4:
                            pygame.mixer.music.pause()
                            run.main()
                        
                except AttributeError:
                    
          
                    try:
                        if sprite.door:
                            if player.key > 0:
                                player.key -= 1
                                sprite.door = False
                                sprite.image = sprite.open_image
                                sprite.open = True
                                
                    
                    except AttributeError:
                        pass
                     
                    if sprite.sign[0]:
                        
                        text_font = pygame.font.Font(None, 40)  #Text Font
                        white = (255,255,255)
                        dark = (0,0,0)
                        text = text_font.render(sprite.sign[1], True, white, dark)
                        textRect = text.get_rect()
                        
                        textRect.center = (sprite.rect.x, sprite.rect.y - 48)
                        screen.blit(text, textRect)
                    else:    
                        
                        if sprite.damage == True:
                        #Death animation
                            player.status = 'death'
                        if player.death == 20:
                            main(self.layout_index)  
                            
                        else:
                            try:
                                if sprite.open:
                                    pass
                                else:
                                    if player.direction.y > 0:
                                        player.rect.bottom = sprite.rect.top
                                        player.direction.y = 0
                                        player.double_jump = 1
                                        player.time = time.time()
                                    elif player.direction.y < 0:
                                        player.rect.top = sprite.rect.bottom
                                        player.direction.y = 0
                            except AttributeError:
                                if player.direction.y > 0:
                                    player.rect.bottom = sprite.rect.top
                                    player.direction.y = 0
                                    player.double_jump = 1
                                    player.time = time.time()
                                elif player.direction.y < 0:
                                    player.rect.top = sprite.rect.bottom
                                    player.direction.y = 0
                    
    def bullet_update(self):
        player = self.player.sprite
        bullet = self.bullet.sprite 
        if player.bullet and bullet.Ask_bullet:
            bullet.bullet(player)   
    
    def run(self,screen, level_map):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.mobs.update(self.world_shift)
        self.mobs.draw(self.display_surface)
        self.bullet_update()
        self.bullet.update()
        self.bullet.draw(self.display_surface)
        self.scroll_x()
        
        self.player.update()
        self.horizontal_mouvement_collision(screen, level_map)
        self.vertical_mouvement_collision(screen, level_map)
        self.player.draw(self.display_surface)
        
        with open("data.json", "r") as f:	#config size screen
            data = json.load(f)
            WIDTH = data["WIDTH"]
            HEIGHT = data["HEIGHT"]
        
        
        # Text
        text_font = pygame.font.Font(None, 40)	#Text Font
        white = (255,255,255)
        text = text_font.render(f'Level {level_map} | Keys : {self.player.sprite.key} | Coins : {self.player.sprite.coin}', True, white)
        # create a rectangular object for the text
        textRect = text.get_rect()
        textRect.center = (WIDTH - (WIDTH-200) , HEIGHT - (HEIGHT-20))
        screen.blit(text, textRect)

def main(level_map):
    def buttons_draw(screen):
        for b in buttons:
            b.draw(screen)

    pygame.init()
    pygame.display.set_caption('NekoDarkLand')	#window title

    buttons = []
    
    with open("data.json", "r") as f:	#config size screen
        data = json.load(f)
        WIDTH = data["WIDTH"]
        HEIGHT = data["HEIGHT"]
        FULL = data["FULL"]

    if FULL == "None":	
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
    else:
        screen = pygame.display.set_mode()
        WIDTH, HEIGHT = screen.get_size()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    
    if level_map == 1:
        bg = pygame.image.load("./alien/background1.jpg")
    elif level_map == 2:
        bg = pygame.image.load("./alien/background2.jpg")
    elif level_map == 3:
        bg = pygame.image.load("./alien/background3.jpg")
    elif level_map == 4:
        bg = pygame.image.load("./alien/background4.jpg")
    elif level_map == 5:
        bg = pygame.image.load("./alien/background4.jpg")
    elif level_map == 6:
        bg = pygame.image.load("./alien/background4.jpg")

    spawn = "null"
    
    pygame.mixer.music.load('./mp3/Florian_Stracker_-_01_The_Sword_and_the_Heart.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    
    level = Level(level_map, screen, spawn)

    pause = pygame.image.load("./game-image/pause.png")

	#button position
    w1= WIDTH/2-100				#column button
    h1 = HEIGHT/2			#First lign (resume)

    #buttons
    button1 = button.Button('Resume', 200, 40, (w1, h1), 5)      #resume

    button2 = button.Button('Menu', 200, 40, (w1, h1+60), 5)	#menu redirection
    button3 = button.Button('Exit', 200, 40, (w1, h1+120), 5)	#exit game
    buttons.append(button1)
    buttons.append(button2)
    buttons.append(button3)

    RUNNING, PAUSE = 0, 1
    state = RUNNING

    pause_text = pygame.font.SysFont('Consolas', 50).render('Pause', True, pygame.color.Color('White'))

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #detect the QUIT request
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if state == RUNNING:
                    if event.key == pygame.K_ESCAPE:    # start pause with escape touch
                        pygame.image.save(screen,"./cache/pause-screen-cache.png")  #take a screenshot for the bg of pause screen
                        cache = Image.open("./cache/pause-screen-cache.png")    #open image
                        cache = cache.convert("L")  #convert in black and white
                        cache = cache.save("./cache/pause-screen-cache.png")    #save modification
                        cache = pygame.image.load("./cache/pause-screen-cache.png") #load image in a variable
                        #set status : pause
                        state = PAUSE
                else:
                    if event.key == pygame.K_ESCAPE:    # stop pause with escape touch
                        #set status : play
                        state = RUNNING

                if event.key == pygame.K_s: #detect "s"touch pressed for screenshot
                    date = datetime.now()   #configure date and hour for the name of the screen
                    day = date.day
                    month = date.month
                    year = date.year
                    hour = date.hour
                    minute = date.minute
                    pygame.image.save(screen, f"./screenshot/{year}_{month}_{day}-{hour}_{minute}.png") #save the screen
        else:
            screen.fill((0, 0, 0))

            if state == RUNNING:    #satus : play
                screen.fill('black')
                screen.blit(bg,(0,0))
                level.run(screen, level_map)
                screen.blit(pause,(WIDTH-70, HEIGHT-(HEIGHT-20)))
                
                #check button pause pressed 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:	#Check click button and react
                        if WIDTH-70 <= mouse[0] <= WIDTH-70+53 and HEIGHT-(HEIGHT-20) <= mouse[1] <= HEIGHT-(HEIGHT-20)+55: #pause buton
                            pygame.image.save(screen,"./cache/pause-screen-cache.png")  #take a screenshot for the bg of pause screen
                            cache = Image.open("./cache/pause-screen-cache.png")    #open image
                            cache = cache.convert("L")  #convert in black and white
                            cache = cache.save("./cache/pause-screen-cache.png")    #save modification
                            cache = pygame.image.load("./cache/pause-screen-cache.png") #load image in a variable
                            #set status : pause
                            state = PAUSE
                            time.sleep(0.3)

            elif state == PAUSE:    #satus : pause
                screen.blit(cache, (0,0))
                screen.blit(pause_text, (WIDTH/2-65, 100))     #text "pause"
                screen.blit(pause,(WIDTH-70, HEIGHT-(HEIGHT-20)))   #pause button
                buttons_draw(screen)	#show button

                #check button pause pressed 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:	#Check click button and react
                        if WIDTH-70 <= mouse[0] <= WIDTH-70+53 and HEIGHT-(HEIGHT-20) <= mouse[1] <= HEIGHT-(HEIGHT-20)+55 or w1 <= mouse[0] <= w1+200 and h1 <= mouse[1] <= h1+40: #pause buton and resum
                            #set status : play
                            state = RUNNING
                            time.sleep(0.3)
                        if w1 <= mouse[0] <= w1+200 and h1+60 <= mouse[1] <= h1+60+40: #menu
                            run.main()  #
                        if w1 <= mouse[0] <= w1+200 and h1+120 <= mouse[1] <= h1+120+40: #exit
                            pygame.quit()
                            sys.exit()

            pygame.display.update()
            clock.tick(60)  #FPS

if __name__ == "__main__":
    spawn= "null"
    main(spawn)
