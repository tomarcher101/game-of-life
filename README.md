# Tom Archer - Game of Life

This is my BBC job application where I have been asked to make the game of life.
I have impleneted the game of life in the command line where it is visulised in an ascii grid.

## Assumptions

- You guys mention in the brief that it takes place on an infinite grid. I have assumed that you guys are okay with me working on a finite grid.
- I have assumed you might like to choose the dimensions of the grid.
- I have assumed that you would like me to visualise the process, which I have done in the command line.

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
   - The grid will print after each time you press ENTER (iterating the state).

6. Type "end" to end the program.
