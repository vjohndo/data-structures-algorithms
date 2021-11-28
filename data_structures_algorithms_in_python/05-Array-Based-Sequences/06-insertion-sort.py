def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""

    for k in range(1, len(A)):
        cur = A[k] # Grab the current item to be looked at
        j = k # Start the while loop from j
        while j > 0 and A[j-1] > cur: # while j>0 and the preceeding value is greater than the current item
            A[j] = A[j-1] # Move the item right 
            j -= 1 # decrement j

        # Will have escaped the while loop one we've reached the start of array !(j > 0)
        # Or found a preceeding value that is less than the current item !(j-1)
        A[j] = cur