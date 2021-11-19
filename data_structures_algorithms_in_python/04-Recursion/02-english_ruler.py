def draw_line(tick_length, tick_label = ' '):
    """Draw one line with given tick length (followed by optional label)"""
    line = '-' * tick_length

    if tick_label:
        line += ' ' + tick_label
    
    print(line)

def draw_interval(center_length):
    """ Draw tick interval based upon a central tick length """
    if center_length > 0: # Base case would be a centre length <= 0 | O(1)
        draw_interval(center_length - 1) # Go to a smaller interval and draw it (progression to base case) | This would result in n-1 calls, so O(n)
        draw_line(center_length) # Draw the centre
        draw_interval(center_length - 1) # Go to a smaller interval and draw it (progression to base case) | This would result in n-1 calls, so O(n)

    # else the base case is do nothing, reached the smallest interval

def draw_ruler(num_inches, major_length):
    """ Draw English rule with give number of inches, major tick length. """

    # O(n^2)

    # Managed the construction of the entire ruler
    draw_line(major_length, '0') # Deaw the starting line | O(1)
    for j in range(1, 1 + num_inches): # Go through each of intervals | O(n)
        draw_interval(major_length - 1) # Draw the small interval | O(n) times, each activation is O(n)
        draw_line(major_length, str(j)) # Draw the end of the that "inch" | O(1)

draw_ruler(10, 2)


# draw_interval(3)
#   draw_interval(2)
#       draw_interval(1)
#           draw_interval(0)
#           draw_line(1)
#           draw_interval(0)
#       draw_line(2)
#       draw_interval(1)
#           draw_interval(0)
#           draw_line(1)
#           draw_interval(0)