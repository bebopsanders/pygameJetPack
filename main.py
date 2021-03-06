import pygame as pg
from settings import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
    def new_game(self):
        self.all_sprites = pg.sprite.Group()
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
