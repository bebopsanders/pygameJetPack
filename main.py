import pygame as pg
from sprites import *
from settings import *
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
    def new_game(self):
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        for plat in PLAT_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.run_game()
    def run_game(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    def update(self):
        self.all_sprites.update()
        # check to see if player is 1/4 from the top of screen
        if self.player.rect.top <= 200:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
        # spawn new platforms to keep same average number
        while len(self.platforms) < 7:
            width = random.randrange(50,200)
            p = Platform(random.randrange(0,WIDTH-width), random.randrange(-75,-30),width,20)
            self.all_sprites.add(p)
            self.platforms.add(p)
        # check for collisions between player and platforms if player.vel.y > 0 (moving down)
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

    def draw(self):
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    def main_menu(self):
        pass
    def game_over(self):
        pass
g = Game()
g.main_menu()
while g.running:
    g.new_game()
    g.game_over()
pg.quit()
