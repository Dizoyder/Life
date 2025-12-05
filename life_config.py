#Конфигурация интерфейса

#Размер сетки
GRID_WIDTH = 80
GRID_HEIGHT = 80

#Размер ячейки в пикселях
CELL_SIZE = 8

#Размер сетки в пикселях
GRID_PIXEL_WIDTH = GRID_WIDTH * CELL_SIZE
GRID_PIXEL_HEIGHT = GRID_HEIGHT * CELL_SIZE

#Высота информационной панели
INFO_HEIGHT = 110

#Размер окна
WIDTH = GRID_PIXEL_WIDTH
HEIGHT = GRID_PIXEL_HEIGHT + INFO_HEIGHT

#Конфигурация правил (минимум и максимум рождения и выживания, B3/S23)
BIRTH_MIN = 3
BIRTH_MAX = 3
SURVIVE_MIN = 2
SURVIVE_MAX = 3

#Скорость симуляции, FPS
FPS = 10

#Цвета
COLOR_FILL = (10, 10, 10)
COLOR_CELL = (220, 220, 220)
COLOR_GRID = (40, 40, 40)
COLOR_INFO = (20, 20, 20)
COLOR_FONT = (200, 200, 200)


