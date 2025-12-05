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

#Рисование сетки
def draw_grid(screen, grid):
    #Затирание окна
    screen.fill(COLOR_FILL)
    #Рисование живых ячеек
    for y in range(GRID_WIDTH):
       for x in range(GRID_HEIGHT):
           if grid[y][x] == 1:
               r = pg.Rect(
                    x * CELL_SIZE,
                    y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE,
                   )
               pg.draw.rect(screen, COLOR_CELL, r)

    #Рисование линий
    for x in range(0, GRID_PIXEL_WIDTH, CELL_SIZE):
        pg.draw.line(
            screen,
            COLOR_GRID,
            (x, 0),
            (x, GRID_PIXEL_HEIGHT)

            )    
    for y in range(0, GRID_PIXEL_HEIGHT, CELL_SIZE):
        pg.draw.line(
            screen,
            COLOR_GRID,
            (0, y),
            (GRID_PIXEL_WIDTH, y)

            )

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

    #Отрисовка
    draw_grid(screen, grid)

    #Переворот графических буферов
    pg.display.flip()
    
    #Скорость обновления(fps)
    clock.tick(FPS)



