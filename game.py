import sys 
import pygame
from pygame.locals import *

from helpers import *
from objects import *
 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

filter_on = False

torch_colors = {
    'r' : (255, 0, 0),
    'g' : (0, 255, 0),
    'b' : (0, 0, 255),
}

bg_color = pygame.Color('lightskyblue4')

light = pygame.image.load('spotlight.png')

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

 
P1 = Player()
#P2 = Player(120, 120)
torch = Torch(50, 50)
tile = Tile(WIDTH/12, WIDTH/12, light)
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rushlight")

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
#all_sprites.add(P2)
all_sprites.add(torch)
all_sprites.add(tile)

#torch.surf = pygame.transform.scale(torch.surf, (100,10))
tile.surf = pygame.transform.scale(tile.surf, (100,100))

light_toggle = False 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    torch.move()
    
    # Enable or disable the spotlight 
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_l] and not light_toggle:
        filter_on = not filter_on
    light_toggle = pressed_keys[K_l]

    displaysurface.fill(bg_color)
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

            
    # Move player
    P1.acc = Vec(0, 0)
    if pressed_keys[K_w]:
        P1.acc.y = -ACC
    if pressed_keys[K_a]:
        P1.acc.x = -ACC
    if pressed_keys[K_s]:
        P1.acc.y = ACC    
    if pressed_keys[K_d]:
        P1.acc.x = ACC    
    P1.move()
    snap_to_bounding_box(P1, displaysurface.get_rect())
    
    # Move torch
    torch.acc = Vec(0,0)
    if pressed_keys[K_LEFT]:
        torch.acc.x = -ACC
    if pressed_keys[K_RIGHT]:
        torch.acc.x = ACC    
    if pressed_keys[K_UP]:
        torch.acc.y = -ACC
    if pressed_keys[K_DOWN]:
        torch.acc.y = ACC    
    torch.move()
    snap_to_bounding_box(torch, displaysurface.get_rect())

    if filter_on:    
        filter = pygame.surface.Surface((HEIGHT, WIDTH))
        filter.fill(pygame.color.Color('Grey'))
        mouse_pos = pygame.mouse.get_pos()
        filter.blit(light, vec(mouse_pos - vec(light.get_rect().width/2, light.get_rect().height/2)))
        displaysurface.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
 
 

    pygame.display.update()
    FramePerSec.tick(FPS)
