import pygame
from pygame.locals import *
import random
from typing import List, Tuple


class GameOfLife:

    def __init__(
            self, width: int=640, height: int=480,
            cell_size: int=10, speed: int=10) -> None:
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

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color('black'), (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        self.clist = self.cell_list(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.draw_cell_list(self.update_cell_list(self.clist))
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize: bool=True) -> List[List[int]]:
        """ Создание списка клеток.

        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        self.clist = []
        if randomize:
            self.clist = [
                [random.randint(0, 1) for col in range(self.cell_width)]
                for row in range(self.cell_height)
            ]
        return self.clist

    def draw_cell_list(self, clist: List[List[int]]) -> None:
        """ Отображение списка клеток

        :param rects:
            Список клеток для отрисовки, представленный в виде матрицы
        """
        for row in range(len(clist)):
            for col in range(len(clist[row])):
                Rect = (
                    self.cell_size * col, self.cell_size * row,
                    self.cell_size, self.cell_size)
                color = (
                    pygame.Color('green') if clist[row][col] == 1 else
                    pygame.Color('white'))
                pygame.draw.rect(self.screen, color, Rect)

    def get_neighbours(self, cell: Tuple[int, int]) -> int:
        """ Вернуть список соседей для указанной ячейки

        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        counter = 0
        neighbours = [
            [0 for col in range(len(self.clist[0]))]
            for row in range(len(self.clist))
        ]
        for row in range(cell[0] - 1, cell[0] + 2):
            for col in range(cell[1] - 1, cell[1] + 2):
                if (0 <= row < len(self.clist)) and
                (0 <= col < len(self.clist[0])) and
                (row != cell[0] or col != cell[1]) and
                (self.clist[row][col] == 1):
                    counter += 1
        return counter

    def update_cell_list(self, cell_list: List[List[int]]) -> List[List[int]]:
        """ Выполнить один шаг игры.

        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.

        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = [
            [0 for col in range(len(cell_list[0]))]
            for row in range(len(cell_list))
        ]

        for row in range(len(cell_list)):
            for col in range(len(cell_list[0])):
                if (self.get_neighbours((row, col)) == 3) or
                (self.get_neighbours((row, col)) == 2) and
                (self.clist[row][col] == 1):
                    new_clist[row][col] = 1
        self.clist = new_clist
        return self.clist
