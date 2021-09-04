# [0] import the turtle module.. don't call this module turtle otherwise you'll import it self
import turtle

# [2] We need to define a function for the turtle to draw
def draw_spiral(my_turtle, line_len):
    # Base case -> if the line length <= 0
    """
    Do nothing
    """

    # Progression towards base case by reducing the line length
    # move turtle forward, turn it 90 degrees
    # then call the function again with a reduced line len
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)

# [1] we create an instance of the turtle. When the turtle is created a window is also created for it self to draw in
my_turtle = turtle.Turtle()
# [3a] we'll point to the screen and call it my_win
my_win = turtle.Screen()
draw_spiral(my_turtle, 100)

# [3] This method allows you to put the turtle into a wait mode until you click in the window
my_win.exitonclick()
