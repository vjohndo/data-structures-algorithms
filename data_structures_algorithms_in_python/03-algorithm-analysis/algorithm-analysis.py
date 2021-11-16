# Example of a linear time algorithm 

def prefix_average(S):
    """ Return list such that for allj, A[j] equals average of S[0],...,S[j]"""
    n = len(S)
    A = [0] * n

    for j in range(n):
        total = 0
        for i in range(j + 1):
            total += S[i]

        A[j] = total / (j + 1)
    
    return A


    