import copy
from random import choice
from time import sleep

empty = ' '
sand = ['0', '1', '2', '3', '4']
barrier_black = '#'
barrier_blue = '-'
barrier_white = '='
barrier_change = '!'


class SandScape:

    def __init__(self, grid: list):
        self.grid = copy.deepcopy(grid)
        self.can_move = True
        self.paused = False

    def update(self):
        self.can_move = False
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell in sand:
                    self.fall(x, y)

    def fall(self, x, y):
        if self.paused:
            return

        if self.grid[y - 1][x] == empty:
            self.grid[y - 1][x] = self.grid[y][x]
            self.grid[y][x] = empty
            self.can_move = True

        elif self.grid[y - 1][x - 1] == empty and self.grid[y - 1][x + 1] == empty:
            offset = choice([1, -1])
            self.grid[y - 1][x + offset] = self.grid[y][x]
            self.grid[y][x] = empty
            self.can_move = True

        elif self.grid[y - 1][x - 1] == empty:
            self.grid[y - 1][x - 1] = self.grid[y][x]
            self.grid[y][x] = empty
            self.can_move = True

        elif self.grid[y - 1][x + 1] == empty:
            self.grid[y - 1][x + 1] = self.grid[y][x]
            self.grid[y][x] = empty
            self.can_move = True

    def draw_grid(self):
        print('\n')
        for row in reversed(self.grid):
            for cell in row:
                print(cell, end='')
            print(end='\n')

    def count(self):
        count = 0
        for row in self.grid:
            for cell in row:
                if cell in sand:
                    count += 1
        return count

    def toggle_paused(self):
        self.paused = not self.paused

    def set(self, grid: list):
        self.grid = copy.deepcopy(grid)


def is_valid_grid(grid):
    for row in grid:
        for cell in row:
            if cell != '#' and cell not in sand and cell != ' ':
                return False
    return True


def outline_grid(grid):
    newgrid = []
    for row in range(len(grid) + 2):
        newgrid.append([])
        for cell in range(len(grid[0]) + 2):
            if cell == 0 or cell == len(grid[0]) + 1 or row == 0 or row == len(grid) + 1:
                newgrid[row].append('#')
            else:
                newgrid[row].append(grid[len(grid) - row][cell - 1])
    return newgrid


hourglass = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '#'],
    ['#', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '='],
    ['=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '='],
    ['=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '='],
    ['=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '='],
    ['=', '=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '=', '='],
    ['=', '=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '=', '='],
    ['=', '=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '=', '='],
    ['=', '=', '=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '=', '=', '='],
    ['=', '=', '=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '=', '=', '='],
    ['=', '=', '=', '=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '=', '=', '=', '='],
    ['=', '=', '=', '=', '=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '=', '=', '=', '=', '='],
    ['=', '=', '=', '=', '=', '=', '#', '-', ' ', ' ', ' ', ' ', ' ', '-', '#', '=', '=', '=', '=', '=', '='],
    ['=', '=', '=', '=', '=', '=', '=', '#', '-', ' ', ' ', ' ', '-', '#', '=', '=', '=', '=', '=', '=', '='],
    ['=', '=', '=', '=', '=', '=', '=', '=', '#', '-', ' ', '-', '#', '=', '=', '=', '=', '=', '=', '=', '='],
    ['=', '=', '=', '=', '=', '=', '=', '#', '-', ' ', ' ', ' ', '-', '#', '=', '=', '=', '=', '=', '=', '='],
    ['=', '=', '=', '=', '=', '=', '#', '-', ' ', ' ', ' ', ' ', ' ', '-', '#', '=', '=', '=', '=', '=', '='],
    ['=', '=', '=', '=', '=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '=', '=', '=', '=', '='],
    ['=', '=', '=', '=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '=', '=', '=', '='],
    ['=', '=', '=', '#', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '#', '=', '=', '='],
    ['=', '=', '=', '#', '-', '0', '1', '2', ' ', ' ', ' ', ' ', ' ', '4', '3', '1', '-', '#', '=', '=', '='],
    ['=', '=', '#', '-', '4', '2', '4', '4', '2', '1', '0', '0', '4', '0', '4', '0', '1', '-', '#', '=', '='],
    ['=', '=', '#', '-', '4', '3', '3', '1', '0', '3', '2', '0', '1', '4', '1', '1', '3', '-', '#', '=', '='],
    ['=', '=', '#', '-', '1', '2', '3', '4', '1', '4', '3', '3', '0', '3', '4', '2', '0', '-', '#', '=', '='],
    ['=', '#', '-', '2', '2', '1', '4', '3', '0', '1', '3', '2', '2', '4', '0', '4', '3', '4', '-', '#', '='],
    ['=', '#', '-', '1', '0', '4', '1', '2', '4', '0', '4', '1', '4', '3', '2', '3', '3', '3', '-', '#', '='],
    ['=', '#', '-', '0', '4', '1', '3', '1', '2', '2', '3', '1', '3', '2', '4', '1', '2', '0', '-', '#', '='],
    ['=', '#', '-', '1', '4', '2', '1', '3', '3', '2', '1', '3', '1', '1', '0', '3', '2', '1', '-', '#', '='],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '#'],
    ['#', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '!', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

if __name__ == "__main__":

    scape = SandScape(hourglass)

    print(f'\nGrain Count: {scape.count()}')

    for i in range(25):
        scape.draw_grid()
        sleep(0.25)
        scape.update()

    print(f'\nGrain Count: {scape.count()}')
