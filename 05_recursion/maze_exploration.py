"""
EXPLORING A MAZE 
    > The maze area is divided up into squares
    > Each square is either open or occupied by a section of wall
    > Turtle can not pass through wall

    Path logic
    1) Go north and call the path recursion logic
    2) If wall go south and call the path recursion logic
    3) If wall go west and call the path recusion logic
    4) If wall go east and call the path recursion logic

    Notice how that causes a potentially infinite loop going north and south
    > Need to track where we've been

    Base case:
    > Run into a wall
    > Run into a path we've already explored
    > Found the outside
    > All squares explored
"""
# We WILL create a maze class to represent the maze
# It will have
"""
__init__ --> reads that data file that represents maze
draw_maze --> will draw the maze on the window of the scren
update_position --> updates the maze representation, changes turtle position
is_exit --> checks to see if the current position is an exist from the maze
"""

import turtle

# define some constant variables.
PART_OF_PATH = "O"
TRIED = "."
OBSTACLE = "+"
DEAD_END = "-"

class Maze:
    # The maze class works by taking a maze file and contructing a 2d list
    def __init__(self, maze_filename):
        """
        CONSTRUCTION OF MAZE_LIST FROM TXT FILE
        """
        # Define helper variables for the row and column size of the list 
        rows_in_maze = 0
        columns_in_maze = 0

        # create a maze_list
        self.maze_list = []

        # Open maze file as an object in read only mode
        maze_file = open(maze_filename, "r")

        # go through each line in the file (row)
        for line in maze_file:
            
            # For each iteration through lines create a row list
            row_list = []
            
            #create a row list a col counter (used to determine the start square)
            col = 0
            
            # for each char in the line append the char to the row list
            for char in line:
                row_list.append(char)

                # Should there be an "S", this is start and keep note of it
                if char == "S":
                    # Take the current iteration of the row/col , this is the start
                    self.start_row = rows_in_maze
                    self.start_col = col

                # increase the col accumulator to keep track of the coloumn
                col = col + 1
            
            # for each iteration through the lines, increase the row counter
            rows_in_maze = rows_in_maze + 1

            # Add the row list that was created through iterating through chars
            self.maze_list.append(row_list)

            # set the column size in maze now that we can check the length of the constructed row_list
            columns_in_maze = len(row_list)

        """
        CONSTRUCTION OF THE GAMESPACE / TURTLE
        """
        # row and columns sizes will define draw_maze
        self.rows_in_maze = rows_in_maze
        self.columns_in_maze = columns_in_maze

        # amount of translation to be used in the draw maze method
        # These specifiy the ORIGIN of the coordinate system and points to the top left (-x, + y)
        self.x_translate = -columns_in_maze/2
        self.y_translate = rows_in_maze/2

        # generate turtle 
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.screen = turtle.Screen()

        # set up the user defined coordinate systems. provides lower left coods and upper right coords of the canvas
        # e.g. for a 20x20 grid, the first coordinate should (centred on the square means we need at account for 0.5) should be -10.5
        self.screen.setworldcoordinates(
            -(columns_in_maze -1 ) / 2 - 0.5,
            -(rows_in_maze -1 ) / 2 - 0.5,
            (columns_in_maze -1 ) / 2 + 0.5,
            (rows_in_maze -1 ) / 2 + 0.5
        )

    # Draw_centred_box
    def draw_centred_box(self,x,y,color):
        # go to the start point (offset) with tail up
        self.turtle.up()
        # offset to a corner using -0.5 for each side.
        self.turtle.goto(x - 0.5, y - 0.5)

        # set the colour and orient the head of the turtle to 90 degrees (i.e. straight up), tail down and fill on
        self.turtle.color(color)
        self.turtle.fillcolor(color)
        self.turtle.setheading(90)
        self.turtle.down()
        self.turtle.begin_fill()
        
        # for four times... i.e. on each side of the square
        for i in range(4):

            # move forward and rotate right 90 degs
            self.turtle.forward(1)
            self.turtle.right(90)
        
        # complete the fill
        self.turtle.end_fill()

    # define a draw maze method which uses a draw a centred box helper function
    def draw_maze(self):
        self.turtle.speed(2000)
        # Turns off automatic screen updates... let's set to 1 to see how it is contructed
        self.screen.tracer(0)

        # for each square in the 2d map
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                
                # if the square is an obstacle, draw it
                if self.maze_list[y][x] == OBSTACLE:
                    
                    # draw a centered box at the given coordinates. The draw-centres-box handles the offset
                    self.draw_centred_box(
                        x + self.x_translate, 
                        -y + self.y_translate, 
                        "orange"
                    )
        
        # reset the turtles colors and fill as we're done drawing the obstacles
        self.turtle.color("black")
        self.turtle.fillcolor("blue")
        self.screen.update()
        self.screen.tracer(1)

    # Helper function for updating position
    def move_turtle(self, x, y):
        # turn the pen off
        self.turtle.up()

        # Torwards returns the angle between aline from the tutle and x,y position and the current orienation of the turtle
        self.turtle.setheading(self.turtle.towards(x + self.x_translate, -y + self.y_translate))
        self.turtle.goto(x + self.x_translate, -y + self.y_translate)
    
    # Helper function for dropping bread crumb
    def drop_bread_crumb(self, color):
        # draws a dot with size ten given color
        self.turtle.dot(10,color)

    # helper function for the maze search algorithm
    # takes in a row, col, or a val which is what the square will be updated to
    def update_position(self, row, col, val = None):
        # mark the square if needed
        if val: 
            self.maze_list[row][col] = val
        
        # move the turtle to that square
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None

        # if we're marking it drop a bread crumb
        if color:
            self.drop_bread_crumb(color)

    # helper function for the maze search algorithm
    def is_exit(self, row, col):

        # defines the conditions if you're at edge of the maze
        return (
            row == 0
            or row == self.rows_in_maze - 1
            or col == 0
            or col == self.columns_in_maze - 1
        )

    # NOT SURE.
    def __getitem__(self, idx):
        return self.maze_list[idx]


# Let's write up our search function, it takes a maze object which we will write later and starting coordinates
def search_from(maze, start_row, start_column):
    
    # For our maze object, update the position to our desired start coords
    maze.update_position(start_row, start_column)
    
    # From the start point search four directions until we find a way out but check if we've hit any of the base cases
    # Base case 1: If we've hit a wall
    if maze[start_row][start_column] == OBSTACLE:
        return False

    # Base case 2: If we've hit a path we've already tried or what we've determined to be a dead end (completely surrounded path we've tried / wall)
    if maze[start_row][start_column] == TRIED or maze[start_row][start_column] == DEAD_END:
        return False

    # Base case 3: We've found an outside edge no occupoed by an obstacle
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True

    maze.update_position(start_row, start_column, TRIED)

    # Now we can search four directions
    # We will use logical short circuiting to try each direction 

    found = (
        # Call search from recursively in the north, then the south, then the west, then the east
        search_from(maze, start_row, start_column - 1) or
        search_from(maze, start_row - 1, start_column) or
        search_from(maze, start_row + 1, start_column) or
        search_from(maze, start_row, start_column + 1)
    )

    # If any of those recursive calls are true:
    if found: 
        # Move the turtle and mark this sqaure as part of the path
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        # Move the turtle and mark this square as a dead end
        maze.update_position(start_row, start_column, DEAD_END)
    return found


# We will then use the turtle module to draw and explore the maze
my_maze = Maze("maze.txt")
my_maze.draw_maze()
my_maze.update_position(my_maze.start_row, my_maze.start_col)

search_from(my_maze, my_maze.start_row, my_maze.start_col)