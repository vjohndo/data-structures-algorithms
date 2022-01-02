def insertion_sort(L):
    """Sort PositionalList of comparable elements into nondecreaseing order"""
    # We only need to sort if the list is greater length than 1
    if len(L) > 1:
        marker = L.first()              # Set up the marker that the first Position
        while marker != L.last():       # 
            pivot = L.after(marker)
            value = pivot.element()

            if value > marker.element():
                # If the value of the pivot is greater than the preceeding marker, move the marker forward
                # This is how the while loop meets the condition marker != L.last()
                marker = pivot

            else:
                # Otherwise start a walk from the marker
                # As we are starting the walk at the marker, it means that we stop walking at the last position that has a value greater than the pivot
                walk = marker
                while walk != L.first() and L.before(walk).element() > value: # If the walk is at the first position, no more walking
                    walk = walk.before

                L.delete(pivot)
                L.add_before(walk, value)



