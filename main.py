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

    print("Here is your starting grid:")
    grid = init_grid(dim)
    draw_grid(grid)

    starting_lives = prompt_for_starting_lives(grid)


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


def prompt_for_starting_lives(grid):
    """Prompts the user for which cells they wish to start live.

    :param grid: The grid the cells are on.

    :returns: An array with the coords of the starting live cells.
    """
    print("Where would you like to place your starting lives?")

    grid_len = len(grid)  
    print('grid len = ', grid_len)

    lives = []

    while True:
        inp = input("Enter a cell in the form [y, x] or type 'END': ")

        # Here is our break condition to end the input prompt loop
        if inp == "END":
            break

        # checks the coordinates are valid
        coord = inp.split(',')
        if len(coord) != 2:
            print("You must provide 2 coordinates.")
            continue
        else:
            try:
                coord[0] = int(coord[0])
                coord[1] = int(coord[1])
            except Exception as e:
                print("Your coordinates must be integers.")
                continue
            
            if coord[0] < 0 or coord[1] < 0:
                print("Your coordinates cannot be negative.")
                continue
            elif coord[0] > grid_len - 1 or coord[1] > grid_len - 1:
                print("Your coordinates must be within your grid.")
            else:
                lives.append(coord)
                print(f"Coordinate [{coord[0]}, {coord[1]}] will start live.")
    
    print(f"Here are you starting live cells = {lives}.\n")

    return lives




if __name__ == "__main__":
    main()
    