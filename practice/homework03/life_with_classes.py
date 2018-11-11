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
        self.row = row
        self.col = col
        self.state = bool

    def is_alive(self) -> bool:
        return self.state


class CellList:

    def __init__(
            self, nrows: int, ncols: int, randomize: bool=False,
            filename: str='grid.txt') -> None:
        self.nrows = nrows
        self.ncols = ncols
        self.row = 0
        self.col = 0
        if randomize:
            self.clist = [
                [Cell(row, col, random.randint(0,1)) for col in range(self.ncols)]
                for row in range(self.nrows)]
        else:
            self.clist = from_file(filename)


    def get_neighbours(self, cell: Cell) -> List[Cell]:
        neighbours = []
        # PUT YOUR CODE HERE
        return neighbours

    def update(self) -> CellList:
        new_clist = deepcopy(self)
        # PUT YOUR CODE HERE
        return self

    def __iter__(self):
        return self

    def __next__(self):
        if self.row < self.nrows:
            if self.col < self.ncols:
                self.col += 1
                return self.clist[self.row][self.col]
            else:
                self.row += 1
                self.col = 0
                self.__next__()
        else:
            raise StopIteration

    def __str__(self):
        pass

    @classmethod
    def from_file(cls, filename):
        file = open(filename, 'r')
        clist = [[int(char) for char in line[:lem(line)-1]] for line in file]
        return clist

