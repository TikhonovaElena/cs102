import pygame
from pygame.locals import *
import random
from copy import deepcopy
from typing import List


class GameOfLife:

    def __init__(
            self, width: int=640, height: int=480, cell_size: int=10,
            speed: int=10) -> None:
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
        # PUT YOUR CODE HERE

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            # PUT YOUR CODE HERE

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


class Cell:

    def __init__(self, row: int, col: int, state: bool=False) -> None:
        pass

    def is_alive(self) -> bool:
        pass


class CellList:

    def __init__(self, nrows: int, ncols: int, randomize: bool=False) -> None:
        pass

    def get_neighbours(self, cell: Cell) -> List[Cell]:
        neighbours = []
        # PUT YOUR CODE HERE
        return neighbours

    def update(self) -> CellList:
        new_clist = deepcopy(self)
        # PUT YOUR CODE HERE
        return self

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __str__(self):
        pass

    @classmethod
    def from_file(cls, filename):
        pass
