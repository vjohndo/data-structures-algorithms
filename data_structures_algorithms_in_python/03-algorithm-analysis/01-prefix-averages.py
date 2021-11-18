# Example of a linear time algorithm 

def prefix_average(S):
    """ Return list such that for all j, A[j] equals average of S[0],...,S[j]"""
    # Return a list of averages up to that point

    # Get the number of elements in the list
    n = len(S)
    # Generate a list of [0].. this is O(n)
    A = [0] * n

    # for each jth character, 
    for j in range(n):

        # keep a track of the total
        total = 0

        # for all the values of i up to the j'th caracter
        for i in range(j + 1):

            # add to the toal
            total += S[i]

        # divide the total for this point by (j + 1)... note the plus 1 due to index starting at 0
        A[j] = total / (j + 1)
    
    return A


def prefix_average2(S):
    """Return list such that for all J, A[j] equals average of S[0],...,S[J]"""
    # O(n^2)
    n = len(S)
    A = [0] * n
    for j in range(n):

        # Same performance asymptotically 
        A[j] = sum(S[0:j+1]) / (j+1)
    
    return A


def prefix_average3(S):

    n = len(S)
    A = [0] * n

    # How about we maintain the total dynamically?
    # We can now get this eqn to O(n)
    total = 0

    for j in range(n):

        total += S[j]
        A[j] = total / (j+1)
    
    return A