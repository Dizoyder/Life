#Импорты
import pygame as pg
import random
from life_config import *

#Функции

#Создание сетки как списка списков
def create_grid():
    g = []
    for row in range(GRID_HEIGHT):
        r = []
        for col in range(GRID_WIDTH):
            r.append(0)

        g.append(r)

    return g 

#Случайное заполнение сетки
def randomize_grid(grid):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if random.random() < DENSITY:
                grid[row][col] = 1
            else:
                grid[row][col] = 0
    
#Подсчёт соседей ячейки
def count_neighbors(grid, x, y):
    count = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            #Пропустить саму клетку
            if dx == 0 and dy == 0:
                continue
            nx = x + dx
            ny = y + dy
            #Если клетка в поле
            if 0 <= nx < GRID_WIDTH:
               if 0 <= ny < GRID_HEIGHT:
                   #Если есть сосед
                   if grid[ny][nx] == 1:
                       count = count + 1
    return count
        
#Один шаг генерации игры
def step(grid):
    #Создание пустой копии сетки
    new_grid = create_grid()
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            #Подсчёт соседней клетки
            neighbors = count_neighbors(grid, x, y)
            #Проверка правила выживания клетки
            if grid[y][x] == 1:
                if SURVIVE_MIN <= neighbors <= SURVIVE_MAX:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
            #Проверка правила рождения клетки
            if grid[y][x] == 0:
                if BIRTH_MIN <= neighbors <= BIRTH_MAX:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
    return new_grid
    
            
#Рисование сетки
def draw_grid(screen, grid):
    #Затирание окна
    screen.fill(COLOR_FILL)
    #Рисование живых ячеек
    for y in range(GRID_HEIGHT):
       for x in range(GRID_WIDTH):
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

#Рисование информационной панели
def draw_info(screen, font, isRun, gen, top_y):
    #Строка правил
    rule_text = f"Правила: рождение - {BIRTH_MIN}-{BIRTH_MAX}, выживание - {SURVIVE_MIN}-{SURVIVE_MAX}"
    #Строка состояния
    if isRun == True:
        state_text = "Процесс"
    else:
        state_text = "Пауза"
    #Строка Генерации
    gen_text = f"Генераций: {gen}"
    #Список строк
    info_lines = [
        f"{rule_text} | {state_text} | {gen_text}",
        "SPACE: запуск/пауза, N: следующий шаг",
        "R: заполнить сетку случайно, C: очистить сетку",
        "Мышь (ЛКМ/ПКМ): заполнить/стереть ячейку, ESC: выход из программы"
        ]
    
    #Отрисовка
    y = top_y
    for line in info_lines:
        surf = font.render(line, True, COLOR_FONT)
        #Вклеивание строки в окно
        screen.blit(surf, (5, y))
        y = y + surf.get_height() + 2
        

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

#Состояние игры(выключено)
isRun = False

#Счётчик поколений
gen = 0

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
            #Включить/выключить игру
            if event.key == pg.K_SPACE:
                isRun = not isRun     
            #Очистка сетки
            if event.key == pg.K_c:
                #Создание сетки заново
                grid = create_grid()
                gen = 0
            #Случайное заполнение сетки
            if event.key == pg.K_r:
                randomize_grid(grid)
                gen = 0
            #Пошаговый запуск
            if event.key == pg.K_n and not isRun:
                grid = step(grid)
                gen = gen + 1

        #Нарисовать/стереть в ручную
        if not isRun:
            if event.type == pg.MOUSEBUTTONDOWN:
                #Точка события
                x, y = event.pos
                if 0 <= x <= GRID_PIXEL_WIDTH:
                    if 0 <= y <= GRID_PIXEL_HEIGHT:
                        #Вычисление строки и столбца клетки
                        ix = x // CELL_SIZE
                        iy = y // CELL_SIZE
                        if event.button == 1: #Клик ЛКМ
                            grid[iy][ix] = 1
                        elif event.button == 3: #Клик ПКМ
                            grid[iy][ix] = 0
            elif event.type == pg.MOUSEMOTION:
                #Точка события
                x, y = event.pos
                if 0 <= x <= GRID_PIXEL_WIDTH:
                    if 0 <= y <= GRID_PIXEL_HEIGHT:
                        #Вычисление строки и столбца клетки
                        ix = x // CELL_SIZE
                        iy = y // CELL_SIZE
                        buttons = event.buttons 
                        if buttons[0]: #ЛКМ зажата 
                            grid[iy][ix] = 1
                        elif buttons[2]: #ПКМ зажата
                            grid[iy][ix] = 0

    #Обновление симуляциии
    if isRun == True:
        grid = step(grid)
        gen = gen + 1

    #Отрисовка сетки
    draw_grid(screen, grid)

    #Отрисовка инфо панели
    draw_info(screen, font, isRun, gen, GRID_PIXEL_HEIGHT + 5)

    #Переворот графических буферов
    pg.display.flip()
    
    #Скорость обновления(fps)
    clock.tick(FPS)



