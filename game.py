import sys 
import pygame
from pygame.locals import *

from objects import *
 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

light=pygame.image.load('spotlight.png')

#print(light.get_rect())
#print(light.get_rect().x)
#sys.exit()
#print(dir(light))

print(pygame.mouse.get_pos())
exit_called = False
 
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
 
FramePerSec = pygame.time.Clock()

 
PT1 = platform(WIDTH/2, HEIGHT-10, WIDTH, 20)
P1 = Player()
T = Torch()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
all_sprites.add(T)

T.surf = pygame.transform.scale(T.surf, (100,100))
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    P1.move()
    T.move()
     
    displaysurface.fill((0,0,0))
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
    
    filter = pygame.surface.Surface((HEIGHT, WIDTH))
    filter.fill(pygame.color.Color('Grey'))
    mouse_pos = pygame.mouse.get_pos()
    filter.blit(light, vec(mouse_pos - vec(light.get_rect().width/2, light.get_rect().height/2)))
    displaysurface.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
 
 

    pygame.display.update()
    FramePerSec.tick(FPS)
