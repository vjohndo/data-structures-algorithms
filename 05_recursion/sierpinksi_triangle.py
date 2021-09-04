"""
The sierpinksi triange
    > draw triangles helper function
    > find the mid points helper function
    > sierpinksi recursive function
"""

import turtle

def draw_triangle(coords, color, my_turtle):
    # Set the fill color
    my_turtle.fillcolor(color)
    
    # raise the turtles tail
    my_turtle.up()

    # turtle goes to first set of coords
    my_turtle.goto(coords[0][0], coords[0][1])

    # set teh turtles tail down
    my_turtle.down()
    my_turtle.begin_fill()
    
    # go to each of the coords specified
    my_turtle.goto(coords[1][0], coords[1][1])
    my_turtle.goto(coords[2][0], coords[2][1])
    my_turtle.goto(coords[0][0], coords[0][1])
    
    # end fill
    my_turtle.end_fill()


def get_mid(p1,p2):
    # return tuple with midpoint of each corresponding coordinate
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2 )


def sierpinski(coords, degree, my_turtle):
    # this color map to correspond to each degree of the recursion call
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]

    # First thing to do is draw the outer triangle
    draw_triangle(coords, colormap[degree], my_turtle)
    # After this, wand to form the sub triangles inside
    # But to do this, will need the sub-sub triangles which requires sub-sub-sub triangles etc..
    # However we know that at degree 0, no further subtriangles. it will return nothing.

    # BASE CASE ONCE DEGREE IS ZERO
    """
    DO NOTHING
    """

    if degree > 0:
    # Now we need to do three recursion calls to sub divide the triangle... much like how 
    # consider the base case ... no subdivisions
    # the the stack frame below ... requires 3x unsubdivided trianges
        sierpinski(
                # Original bottom left corner, new top, new bottome right
                [coords[0], get_mid(coords[0], coords[1]), get_mid(coords[0], coords[2]) ],
                degree - 1,
                my_turtle
        )

        sierpinski(
                # Original top corner, new bottem left, new bottom right
                [coords[1], get_mid(coords[0], coords[1]), get_mid(coords[1], coords[2]) ],
                degree - 1,
                my_turtle
        )

        sierpinski(
                # Original bottom bottom left, new top, new bottome right
                [coords[2], get_mid(coords[2], coords[1]), get_mid(coords[2], coords[0]) ],
                degree - 1,
                my_turtle
        )

def main():
    my_turtle = turtle.Turtle()
    my_screen = turtle.Screen()
    # specify vertices of triangle
    my_coords = [[-180, -150], [0, 150], [180, -150]]
    # run sierpinski on them
    sierpinski(my_coords, 5, my_turtle)
    my_screen.exitonclick()


main()
