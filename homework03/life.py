import pygame
from pygame.locals import *
import random
from copy import deepcopy

class GameOfLife:

    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.clist = self.cell_list()
        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        self.clist = game.cell_list()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:  # type: ignore
                    running = False

            self.draw_grid()

            self.draw_cell_list(self.clist)

            self.clist = self.update_cell_list(self.clist)

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=True) -> list:
        """ Создание списка клеток.
        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
<<<<<<< HEAD
        self.clist = [[0 for i in range(self.cell_width)] for j in range(self.cell_height)]
=======
        clist = [[0 for i in range(self.cell_width)] for j in range(self.cell_height)]
>>>>>>> 9f1d38a60cf32a9f8c9aecf4e80682e00d17a1f4
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if randomize:
                    self.clist[i][j] = random.randint(0, 1)
        return self.clist

    def draw_cell_list(self, clist: list) -> None:
        """ Отображение списка клеток
        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                x = j * self.cell_size + 1
                y = i * self.cell_size + 1
                a = self.cell_size - 1
                b = self.cell_size - 1
                if clist[i][j]:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (x, y, a, b))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (x, y, a, b))

<<<<<<< HEAD
    def get_neighbours(self, cell):
=======
    def get_neighbours(self, cell: tuple) -> list:
>>>>>>> 9f1d38a60cf32a9f8c9aecf4e80682e00d17a1f4
        """ Вернуть список соседей для указанной ячейки
        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        neighbours = []
        r, w = cell
        a = self.cell_height - 1
        b = self.cell_width - 1
        for i in range(r - 1, r + 2):
            for j in range(w - 1, w + 2):
                if not (0 <= i <= a and 0 <= j <= b) or (i == r and j == w):
                    continue
                neighbours.append(self.clist[i][j])
        return neighbours

    def update_cell_list(self, cell_list: list) -> list:
        """ Выполнить один шаг игры.

        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.

        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = deepcopy(self.clist)
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                k = sum(self.get_neighbours((i, j)))
                if self.clist[i][j]:
                    if k < 2 or k > 3:
                        new_clist[i][j] = 0
                else:
                    if k == 3:
                        new_clist[i][j] = 1
        self.clist = new_clist
        return self.clist


if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()