"""
Towers of Hanoi

Lessons learned... 3 hours of thinking to understand 8 lines of code :O
"""

# Helper function that moves disks
def move_disk(from_pole, to_pole):
    print("moving disk from", from_pole, "to", to_pole)


def move_tower(height, from_pole, to_pole, with_pole):
    # BASE CASE / ESCAPE, should the height < 1, do nothing
    """
    DO NOTHING
    """

    # Other wise 
    if height >= 1:
        # call the function to move the tower of n-1 height
        move_tower(height-1, from_pole, with_pole, to_pole)
        
        # move the single disk to the destination
        move_disk(from_pole, to_pole)

        # Stack the rest of the tower on top
        move_tower(height-1, with_pole, to_pole, from_pole)

move_tower(3, "A", "B", "C")