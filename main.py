import pygame as pg
from config import WIDTH, HEIGHT
from being import Being
pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

beings = [Being() for _ in range(10)]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.fill((0, 0, 0))
    for being in beings:
        being.draw(screen)

    pg.display.flip()
    clock.tick(60)
