import pygame as pg

pg.init()
screen = pg.display.set_mode((W,H))
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()

running = True
while running:
    clock.tick(FPS)
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()
