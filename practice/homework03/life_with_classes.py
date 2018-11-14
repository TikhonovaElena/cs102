import pygame
from pygame.locals import *
import random
from copy import deepcopy
from typing import List


class Cell:

    def __init__(self, row: int, col: int, state: bool=False) -> None:
        self.row = row
        self.col = col
        self.state = state

    def is_alive(self) -> bool:
        return self.state


class CellList:

    def __init__(
            self, nrows: int, ncols: int, randomize: bool=False,
            fromFile: bool=False, *filename: str) -> None:
        self.nrows = nrows
        self.ncols = ncols
        self.row = 0
        self.col = 0
        self.clist = []
        if randomize:
            self.clist = [
                [Cell(row, col, random.randint(0,1)) for col in range(self.ncols)]
                for row in range(self.nrows)]
        elif fromFile:
            self.clist = from_file(filename)


    def get_neighbours(self, cell: Cell) -> List[List[Cell]]:
        neighbours = []
        for row in range(cell.row-1, cell.row+2):
            for col in range(cell.col-1, cell.col+2):
                if ((0 <= row < self.nrows) and
                (0 <= col < self.ncols) and
                (row != cell.row or col != cell.col) and
                self.clist[row][col].is_alive()):
                    neighbours.append(self.clist[row][col])
        return neighbours

    def will_alive(self, cell: Cell) -> bool:
        neighbours = self.get_neighbours(cell)
        if (len(neighbours) == 3 or
        (len(neighbours) == 2 and cell.is_alive())):
            return True
        return False

    def update(self):
        """
        Возвращает новый CellList с новым списком клеток внутри
        """
        new_clist = CellList(self.nrows, self.ncols)
        new_clist.clist = [
            [Cell(row, col, self.will_alive(self.clist[row][col]))
            for col in range(self.ncols)]
            for row in range(self.nrows)]
        return new_clist

    def __iter__(self):
        self.row = 0
        self.col = 0
        return self

    def __next__(self) -> Cell:
        if self.row < self.nrows:
            if self.col < self.ncols:
                self.col += 1
                cell = self.clist[self.row][self.col-1]
                return cell
            else:
                self.row += 1
                self.col = 0
                return self.__next__()
        else:
            raise StopIteration

    def __str__(self):
        row = []
        grid = []
        str_grid = '['
        for cell in self:
            row.append(1 if cell.is_alive() else 0)
            if len(row) == self.nrows:
                grid.append(row)
                str_grid = str_grid + str(row) + '\n '
                row = []
        return str_grid[:len(str_grid)-2] + ']'


    @classmethod
    def from_file(cls, filename):
        file = open(filename, 'r')
        clist = [[int(char) for char in line[:len(line)-1]] for line in file]
        return clist


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

    def draw_cell_list(self, cellList: CellList) -> None:
        """ Отображение списка клеток """
        for cell in cellList:
                rect = (
                    self.cell_size * cell.col, self.cell_size * cell.row,
                    self.cell_size, self.cell_size)
                color = (
                    pygame.Color('green') if cell.is_alive() else
                    pygame.Color('white'))
                pygame.draw.rect(self.screen, color, rect)

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        cellList = CellList(
            nrows=self.height//self.cell_size,
            ncols=self.width//self.cell_size, randomize=True
        )

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            cellList = cellList.update()
            self.draw_cell_list(cellList)

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()