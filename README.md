# Tom Archer - Game of Life

This is my BBC job application where I have been asked to make the game of life.
I have impleneted the game of life in the command line where it is visulised in an ascii grid.

## How to use it.

1. Copy the repo onto your machine.

2. Open the repo in the command line.

   - There are 2 ways to run the game of life.

3. Type "python main.py \[required dimensions\]" to create your grid straight from the command line.
   - _[required dimensions]_ should just be an integer (n) of which an nxn grid will made for the Game of Life.

3. Otherwise "python main.py" will ask you for the _required dimensions_ when you start the program.

4. Enter the coords of the cells you wish to start as live, one at a time.
   - Coords must be entered in the form \[row, col\].
     - The top row is where row = 0.
     - The left most col is where col = 0.
   - Press ENTER after entering each coord.
   - Type "end" to finish inputting coords.

5. Press ENTER to iterate the grid into its next state.

6. Type "end" to end the program.
