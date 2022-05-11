import pygame, math, itertools

def magnitude(v): 
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))

def sub(u, v):
    return [u[i]-v[i] for i in range(len(u))]

def normalize(v): 
    return [v[i]/magnitude(v)  for i in range(len(v))]

pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()    

path = itertools.cycle([(26, 43), (105, 110), (45, 225), (145, 295), (266, 211), (178, 134), (250, 56), (147, 12)])
target = next(path)
ball, speed = pygame.rect.Rect(target[0], target[1], 10, 10), 3.6
pause_text = pygame.font.SysFont('Consolas', 32).render('Pause', True, pygame.color.Color('White'))

RUNNING, PAUSE = 0, 1
state = RUNNING

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: break
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_p: state = PAUSE
            if e.key == pygame.K_s: state = RUNNING
    else:
        screen.fill((0, 0, 0))

        if state == RUNNING:
            target_vector = sub(target, ball.center) 

            if magnitude(target_vector) < 2: 
                target = next(path)
            else:
                ball.move_ip([c * speed for c in normalize(target_vector)])

            pygame.draw.rect(screen, pygame.color.Color('Yellow'), ball)

        elif state == PAUSE:
            screen.blit(pause_text, (100, 100))

        pygame.display.flip()
        clock.tick(60)
        continue
    break