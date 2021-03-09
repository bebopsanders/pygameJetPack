import pygame as pg
import random
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30,90))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.pos = vec(WIDTH/2,HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jetFule = 100

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self,self.game.platforms,False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def activateJetPack(self):
        if self.jetFule > 0:
            self.acc.y = -0.17
            self.jetFule -= 2

    def update(self):
        self.acc = vec(0,1)
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -0.5
        if keys[pg.K_d]:
            self.acc.x = 0.5
        if keys[pg.K_w]:
            self.activateJetPack()
        if keys[pg.K_SPACE]:
            self.jump()
        self.acc.x += self.vel.x * -PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

class Platform(pg.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
