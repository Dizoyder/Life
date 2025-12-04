#Импорты
import pygame as pg
import random
from life_config import *

#Функции

#Создание сетки как списка списков
def create_grid():
    g = []
    for row in range(GRID_WIDTH):
        r = []
        for col in range(GRID_HEIGHT):
            r.append(0)

        g.append(r)

    return g 


#Главный цикл
pg.init()

#Создание окна
screen = pg.display.set_mode( (WIDTH, HEIGHT))
#Заголовок
pg.display.set_caption("Game of Life")
clock = pg.time.Clock()
font = pg.font.SysFont("consolas", 16)

#Создание сетки
grid = create_grid()

#Цикл обновления
while True:

    #Обработка событий
    for event in pg.event.get():
        #Закрытие окна
        if event.type == pg.QUIT:
            pg.quit()

        #Обработка клавиш
        if event.type == pg.KEYDOWN:
            #Закрытие окна по ESC
            if event.key == pg.K_ESCAPE:
                pg.quit()

    #Скорость обновления(fps)
    clock.tick(FPS)



