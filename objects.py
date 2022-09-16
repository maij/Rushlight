import pygame
from pygame.locals import *

ACC = 0.5
FRIC = -0.12

tile_color = (150,110,30)

Vec = pygame.math.Vector2  # 2 for two dimensional

class Torch(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, width=20, height=10):
        super().__init__()
        self.pos = Vec((x, y))
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(midbottom = self.pos)

        self.poly = pygame.draw.polygon(self.surf, 
            (175, 100, 0), 
            ((0, 0), (0, 100), (100, 100), (100,0)),
        )
        self.vel = Vec(0,0)
        self.acc = Vec(0,0)
    
    def move(self):
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

class Player(pygame.sprite.Sprite):
    def __init__(self, x=10, y=385):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (10, 420))
        
        self.pos = Vec((x, y))
        self.vel = Vec(0,0)
        self.acc = Vec(0,0)

    def move(self):
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
    def __init__(self, x, y, pattern):
        super().__init__()
        self.pos = Vec((x, y))

        self.rect = pattern.get_rect(center=(x,y))
        self.surf = pygame.Surface((self.rect.width, self.rect.height))
        self.surf.fill(tile_color)
        self.surf.blit(pattern, pattern.get_rect())
