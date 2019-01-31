import numpy as np
from tabulate import tabulate
import sys


def main():
    if len(sys.argv) > 2:
        print("Please only provide one command line argument.")
        sys.exit()
    elif len(sys.argv) == 2:
        try:
            dim = int(sys.argv[1])
        except ValueError as e:
            print("Command line argument should be an integer.")
            sys.exit()
    else:
        try:
            dim = int(input("What would you like the dimensions of your grid to be? "))
        except ValueError as e:
            print("Dimension metric should be an integer.")
            sys.exit()


    grid = init_grid(dim)
    draw_grid(grid)


def init_grid(dim):
    """Creates an array with the dimensions [dim]x[dim].

    :param dim: The desired dimension of your grid.

    :returns: An empty dim x dim array.
    """
    grid = []
    for i in range(dim):
        grid.append([])
        for j in range(dim):
            grid[i].append(None)

    return grid


def draw_grid(grid):
    """Draws the desired grid.

    :param grid: The array object you wish to draw.
    """

    def draw_line():
        row_len = len(grid[0])
        print('-' * row_len * 4, end='')
        print('-')

    def draw_row(row):
        print('|', end='')
        for square in row:
            if square == None: print('   ', end='')
            else: print(' o ', end='')
            print('|', end='')
        print('')

    print('') 
    draw_line()
    for row in range(len(grid)):
        draw_row(grid[row]) 
        draw_line()
    print('') 



if __name__ == "__main__":
    main()
    