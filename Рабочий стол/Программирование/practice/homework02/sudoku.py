import random
def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values, n):
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    grid = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append(values[i*n + j])
        grid.append(line)
    return grid



def get_row(values, pos):
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return values[pos[0]]


def get_col(values, pos):
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    column = []
    for i in range(len(values)):
        column.append(values[i][pos[1]])
    return column


def get_block(values, pos):
    """ Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    block = []
    for i in range(len(values)):
        block.append(values[(pos[0]//3)*3 + i//3][(pos[1]//3)*3 + i%3])
    return block


def find_empty_positions(grid):
    """ Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                return (i,j)
    return None


def find_possible_values(grid, pos):
    """ Вернуть множество возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    values = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for value in get_col(grid, pos):
        values.discard(value)
    for value in get_row(grid, pos):
        values.discard(value)
    for value in get_block(grid, pos):
        values.discard(value)
    return values


def solve(grid):
    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    pos = find_empty_positions(grid)
    if pos is None:
        return grid
    for value in find_possible_values(grid, pos):
        solution = solve(grid[:pos[0]] + [(grid[pos[0]][:pos[1]] + [value] + grid[pos[0]][pos[1]+1:])] + grid[pos[0]+1:])
        if solution:
            return solution
    return None


def check_solution(solution):
    """ Если решение solution верно, то вернуть True, в противном случае False"""
    """
    >>> solution = read_sudoku('puzzle1.txt')
    check_solution(solution)
    False
    >>> solution = [['5', '3', '3', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    check_solution(solution)
    False
    >>>solution = [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    check_solution(solution)
    True
    """
    
    for i in range(9):
        if {'1', '2', '3', '4', '5', '6', '7', '8', '9'} != set(get_row(solution, (0,i))):
            return False
        if {'1', '2', '3', '4', '5', '6', '7', '8', '9'} != set(get_col(solution, (i,0))):
            return False
        if {'1', '2', '3', '4', '5', '6', '7', '8', '9'} != set(get_block(solution, (i//3*3,i%3*3))):
            return False
    return True


def generate_sudoku(N):
    """ Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    grid = mix(read_sudoku('grid.txt'),random.randint(10,20))
    pos = (random.randint(0,8), random.randint(0,8))
    for i in range(81-N):
        while grid[pos[0]][pos[1]] == '.':
            pos = (random.randint(0,8), random.randint(0,8))
        grid[pos[0]][pos[1]] = '.'
    return grid






def tilt(grid):
    grid_result = []
    #grid_line = []
    #grid_result[i].append([grid_line.append([grid[j][i] for j in range(9)]) for i in range(9)])
    for i in range(9):
        grid_line = []
        for j in range(9):
            grid_line.append(grid[j][i])
        grid_result.append(grid_line)
    return grid_result
def swap_lines(grid):
    grid_result = []
    row = random.randint(0,8)
    row_swap = (row%3+random.randint(1,2))%3 + (row//3)*3
    for i in range(9):
        if i == row:
            grid_result.append(grid[row_swap])
        elif i == row_swap:
            grid_result.append(grid[row])
        else:
            grid_result.append(grid[i])
    return grid_result
def swap_columns(grid):
    return tilt(swap_lines(tilt(grid)))
def swap_lines_x3(grid):
    #здесь один ряд  - это три ряда
    grid_result = []
    row = random.randint(0,2)
    row_swap = (row + random.randint(1,2))%3
    for i in range(9):
        if i//3  == row:
            grid_result.append(grid[3*row_swap+i%3])
        elif i//3 == row_swap:
            grid_result.append(grid[3*row+i%3])
        else:
            grid_result.append(grid[i])
    return grid_result
def swap_columns_x3(grid):
    return tilt(swap_lines_x3(tilt(grid)))
def mix(grid,amt = 10):
    if amt != 0:
        action = random.randint(0,4)
        if action == 0:
            return mix(tilt(grid),amt-1)
        elif action == 1:
            return mix(swap_lines(grid),amt-1)
        elif action == 2:
            return mix(swap_columns(grid),amt-1)
        elif action == 3:
            return mix(swap_lines_x3(grid),amt-1)
        else:
            return mix(swap_columns_x3(grid),amt-1)
    return grid


if __name__ == '__main__':
    for fname in ['puzzle1.txt', 'puzzle2.txt', 'puzzle3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        display(solution)