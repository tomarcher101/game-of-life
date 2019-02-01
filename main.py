import sys
from pprint import pprint


def main():
    # This code block gets input and builds the grid
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

    # gets the starting live cells from the user
    starting_lives = prompt_for_starting_lives(grid)
    grid = fill_grid_with_lives(grid, starting_lives)
    draw_grid(grid)

    rows = len(grid)
    cols = len(grid)

    inp = input("Press ENTER to continue...")

    while True:
        for row in range(rows):
            for col in range(cols):
                # print(f'grid[{row}][{col}] = {grid[row][col]}')
                cell = grid[row][col]
                cell.get_next_state(grid)
        
        grid = move_grid_to_next_state(grid)
        draw_grid(grid)
        
        inp = input("Press ENTER to continue, or type 'end' to exit... ")
        if inp == 'end' or inp == 'END':
            break


class Cell:
    def __init__(self, y, x, grid):
        self.x = x
        self.y = y
        self.state = None
        self.next_state = None

    def get_surrounding_cells(self, grid):
        """Creates an attribute for every cell surrounding your cell.

        :param grid: The current grid.

        :returns: None
        """
    
        self.max = len(grid)

        xl = self.x - 1
        x = self.x
        xr = self.x + 1
        ya = self.y - 1
        y = self.y
        yb = self.y + 1

        try:
            self.above_left = grid[ya][xl].state
        except Exception as e:
            self.above_left = None

        try:
            self.above = grid[ya][x].state
        except Exception as e:
            self.above = None
        
        try:
            self.above_right = grid[ya][xr].state
        except Exception as e:
            self.above_right = None

        try:
            self.left = grid[y][xl].state
        except Exception as e:
            self.left = None

        try:
            self.right = grid[y][xr].state
        except Exception as e:
            self.right = None

        try:
            self.below_left = grid[yb][xl].state
        except Exception as e:
            self.below_left = None

        try:
            self.below = grid[yb][x].state
        except Exception as e:
            self.below = None
        
        try:
            self.below_right = grid[yb][xr].state
        except Exception as e:
            self.below_right = None
        
    def get_live_neighbour_count(self, grid):
        """Returns the number of live neighbours a cell has.

        :param grid: The current grid.

        :returns: (int) Count of live neighbours.
        """

        self.get_surrounding_cells(grid)
        lve_cnt = 0


        # these try except blocks are required just incase the cell being inspected
        # is on the perimiter of our grid and therefore raises an exception because it is
        # surrounded by "None"s rather than cells.
        try:
            if self.above_left == "live":
                lve_cnt += 1
        except AttributeError as e:
            pass

        try:
            if self.above == "live":
                lve_cnt += 1
        except AttributeError as e:
            pass

        try:
            if self.above_right == "live":
                lve_cnt += 1
        except AttributeError as e:
            pass

        try:
            if self.left == "live":
                lve_cnt += 1
        except AttributeError as e:
            pass

        try:
            if self.right == "live":
                lve_cnt += 1
        except AttributeError as e:
            pass

        try:
            if self.below_left == "live":
                lve_cnt += 1
        except AttributeError as e:
            pass

        try:
            if self.below == "live":
                lve_cnt += 1
        except AttributeError as e:
            pass

        try:
            if self.below_right == "live":
                lve_cnt += 1
        except AttributeError as e:
            pass

        
        # print("aboveleft = ", self.above_left)
        # print("above = ", self.above)
        # print("aboveright = ", self.above_right)
        # print("left = ", self.left)
        # print("right = ", self.right)
        # print("belowleft = ", self.below_left)
        # print("below = ", self.below)
        # print("below_right = ", self.below_right)

        # print("livecount ", lve_cnt)

        return lve_cnt
    
    def get_next_state(self, grid):
        """Gets the next_state attribute from the surrounding cells.

        :param grid: Teh current grid.
        """

        lve_cnt = self.get_live_neighbour_count(grid)

        # scenario 1 - underpopulation
        if self.state == 'live' and lve_cnt < 2:
            self.next_state = None
        # scenario 2 - overcrowding
        elif self.state == "live" and lve_cnt > 3:
            self.next_state = None
        # scenario 3 - survival
        elif self.state == 'live' and (lve_cnt == 2 or lve_cnt == 3):
            self.next_state = "live"
        # scenario 4 - creation of life
        elif self.state == None and lve_cnt == 3:
            self.next_state = "live"
        elif self.state == None and lve_cnt == 0:
            self.next_state = None
        
        # print(f"row={self.y}, col={self.x}, nextstate={self.next_state}")
  

def init_grid(dim):
    """Creates an array with the dimensions [dim]x[dim].

    :param dim: The desired dimension of your grid.

    :returns: An empty dim x dim array.
    """
    grid = []
    for y in range(dim):
        # print('y = ', y)
        grid.append([])
        for x in range(dim):
            # print('x = ', x)
            grid[y].append(Cell(y, x, grid))

    return grid


def draw_grid(grid):
    """Draws the desired grid.

    :param grid: The array object you wish to draw.
    """

    def draw_line():
        """Draws a horizontal line of the required size for your grid"""
        row_len = len(grid[0])
        print('-' * row_len * 4, end='')
        print('-')

    def draw_row(row):
        """Draws a row of the grid"""
        print('|', end='')
        for square in row:
            try:
                if square.state == None: print('   ', end='')
                else: print(' o ', end='')
            except AttributeError as e:
                print('   ', end='')
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

    grid_len = len(grid)  
    lives = []

    print("Where would you like to place your starting lives?")

    while True:
        inp = input("Enter a cell in the form [y, x] or type 'END': ")

        # Here is our break condition to end the input prompt loop
        if inp == "end" or inp == "END":
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
    
    print(f"Here are you starting live cells = {lives}.")

    return lives


def fill_grid_with_lives(grid, lives):
    """Takes a grid and fills the coords provided with 'o'.

    :param grid: The matrix you wish to fill.
    :param lives: Array of the coords you wish to fill on the grid.
    """
    for coord in lives:
        grid[coord[0]][coord[1]].state = 'live'
    
    return grid


def move_grid_to_next_state(grid):
    """Takes a grid and outputs the next state.

    :param grid: The current state of the grid.

    :returns: The next state of the grid
    """
    for row in grid:
        for cell in row:
            cell.state = cell.next_state
            cell.next_state = None
    
    return grid


if __name__ == "__main__":
    main()
    