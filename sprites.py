import pygame as pg
import random
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30,90))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.pos = vec(WIDTH/2,HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def update(self):
        self.acc = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -0.5
        if keys[pg.K_d]:
            self.acc.x = 0.5
        if keys[pg.K_s]:
            self.acc.y = 0.5
        if keys[pg.K_w]:
            self.acc.y = -0.5
        self.acc += self.vel * -0.07
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
