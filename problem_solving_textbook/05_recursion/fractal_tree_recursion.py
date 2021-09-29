"""
Fractal tree recursion
    > Each call of the recursive function is another branch
"""
import turtle
import random

def tree(branch_len, turtle_instance):
    # BASE CASE should the length be less then 5, DO NOTHING
    """
    DO NOTHING
    """

    # PROGRESS TOWARDS BASE CASE by reducing branch length
    if branch_len > 5:
        my_turtle.width(branch_len**((1/2)))
        
        if branch_len < 18:
            my_turtle.color('green')
            my_turtle.width(branch_len**((1/1.5)))
        else:
            my_turtle.color('brown')
        
        # move the turtle forward 
        turtle_instance.forward(branch_len)

        branch_angle = random.randint(15,45)

        # and turn right 20 degs i.e. face the right hand side
        turtle_instance.right(branch_angle)

        # Recursive call. Get the result of the above stack frame noting eventually there will be a stack frame with no branch.
        tree(branch_len - random.randint(12,16), turtle_instance)

        # Turn enought to face the otherside
        turtle_instance.left(branch_angle*2)

        # Recursive call. Get the result of the above stack frame noting eventually there will be a stack frame with no branch.
        tree(branch_len - random.randint(12,16), turtle_instance)

        if branch_len <= 16:
            my_turtle.color('green')
            my_turtle.width(branch_len**((1/1.5)))
        else:
            my_turtle.color('brown')

        my_turtle.width(branch_len**((1/2)))
        # Turn back to face dead on striaght when this stack frame was called
        turtle_instance.right(branch_angle)

        # Move back to where we started on this stack frame
        turtle_instance.backward(branch_len)
        


my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

# get the turtle into a starting position. the turtle starts facing 0 deg in bearing
my_turtle.left(90) # turn left 90 deg
my_turtle.up() # lift up tail
my_turtle.backward(150) # move backwards 100 units
my_turtle.down() # put tail down
my_turtle.color("brown")
tree(100, my_turtle)

my_screen.exitonclick()