import pygame
from pygame.locals import *

ACC = 0.5
FRIC = -0.12

Vec = pygame.math.Vector2  # 2 for two dimensional

class Torch(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, width=20, height=10):
        super().__init__()
        self.pos = Vec((x, y))
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(center = self.pos)

        self.poly = pygame.draw.polygon(self.surf, 
            (175, 100, 0), 
            ((0, 0), (0, 1), (1, 1), (1,0)),
        )
        self.vel = Vec(0,0)
        self.acc = Vec(0,0)
    
    def move(self):
        self.acc = Vec(0,0)
        
        pressed_keys = pygame.key.get_pressed()
            
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC    
        
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        #if self.pos.x > WIDTH:
        #    self.pos.x = 0
        #if self.pos.x < 0:
        #    self.pos.x = WIDTH
        #     
        self.rect.midbottom = self.pos

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (10, 420))
        
        self.pos = Vec((10, 385))
        self.vel = Vec(0,0)
        self.acc = Vec(0,0)

    def move(self):
        self.acc = Vec(0,0)
        
        pressed_keys = pygame.key.get_pressed()
            
        if pressed_keys[K_w]:
            self.acc.y = -ACC
        if pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_s]:
            self.acc.y = ACC    
        if pressed_keys[K_d]:
            self.acc.x = ACC    
        
        self.acc.x += self.vel.x * FRIC
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

       # if self.pos.x > WIDTH:
       #     self.pos.x = 0
       # if self.pos.x < 0:
       #     self.pos.x = WIDTH
             
        self.rect.midbottom = self.pos

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, pattern):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(center = (x, y))
        #self.surf.blit(pattern, Vec(x, y))
        self.surf.fill((255, 255, 255))
 
