import pygame, numpy

WIDTH = 1200
HEIGHT = 700
BACKGROUND = (0, 0, 0)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startx, starty]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Player(Sprite): #PLAYER
    def __init__(self, startx, starty):
        super().__init__("./alien/p1_front.png", startx, starty)
        self.stand_image = self.image
        self.jump_image = pygame.image.load("./alien/p1_jump.png")
        
        
        #SPEED
        self.speed = 10
        self.jumpspeed = 15
        self.gravity = 2
        self.vsp = 0 # vertical speed
        self.min_jumpspeed = 3
        self.prev_key = pygame.key.get_pressed()
        
        self.walk_cycle = [pygame.image.load(f"./alien/p1_walk{i:0>2}.png") for i in range(1,3)]
        self.animation_index = 0
        self.facing_left = False
        
    def update(self, boxes):
        hsp = 0 # horizontal speed
        onground = self.check_collision(0, 1, boxes)

        # check keys
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.facing_left = True
            self.walk_animation()
            hsp = -self.speed
        elif key[pygame.K_RIGHT]:
            self.facing_left = False
            self.walk_animation()
            hsp = self.speed
        else:
            self.image = self.stand_image

        if key[pygame.K_UP] and onground:
            self.vsp = -self.jumpspeed

        # variable height jumping
        if self.prev_key[pygame.K_UP] and not key[pygame.K_UP]:
            if self.vsp < -self.min_jumpspeed:
                self.vsp = -self.min_jumpspeed

        self.prev_key = key

        # gravity
        if self.vsp < 10 and not onground: # 9.8 rounded up
            self.jump_animation()
            self.vsp += self.gravity

        # stop falling when the ground is reached
        if self.vsp > 0 and onground:
            self.vsp = 0

        # movement
        self.move(hsp, self.vsp, boxes)
        
    def move(self, x, y, boxes):
        dx = x
        dy = y

        while self.check_collision(0, dy, boxes):
            dy -= numpy.sign(dy)
        
        while self.check_collision(dx, dy, boxes):
            dx -= numpy.sign(dx)

        self.rect.move_ip([dx,dy])
        
    def walk_animation(self):
        self.image = self.walk_cycle[self.animation_index]
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

        if self.animation_index < len(self.walk_cycle)-1:
            self.animation_index += 1
        else:
            self.animation_index = 0
    
    def jump_animation(self):
        self.image = self.jump_image
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)
            
    def check_collision(self, x, y, boxes):
        self.rect.move_ip([x,y])
        collide = pygame.sprite.spritecollideany(self, boxes)
        self.rect.move_ip([-x,-y])
        return collide
        
class Box(Sprite):
    def __init__(self, startx, starty):
        super().__init__("./alien/boxAlt.png", startx, starty)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player(100,200)
    
    boxes = pygame.sprite.Group()
    for bx in range(0,400,70):
        boxes.add(Box(bx,300))
    
    boxes.add(Box(600,300))

    while True:
        pygame.event.pump()
        player.update(boxes)
        
        screen.fill(BACKGROUND)
        player.draw(screen)
        boxes.draw(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()