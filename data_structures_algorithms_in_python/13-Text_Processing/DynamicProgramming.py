def matrix_chain(d):
    """d is a list of n+1 numbers such that size of kth matrix is d[k]-by-d[k+1]
    
    Return an n-by-n table such that N[i][j] represents he minimum number of 
    multiplications needed to compute the product of Ai through Aj inclusive
    """
    n = len(d) - 1
    N = [[0] * n for i in range(n)] # initialise a n-by-n result to zero
    for b in range(1, n): # number of productsi nthe sub chain (1, 2, 3, ..)
        for i in range(n-b): # start of subchain (n - 1, ...., 3, 2, 1)
            j = i + b # end of the subchain
            N[i][j] = min(N[i][k] + N[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i, j))
    return N

# -- Longest Common Sequence

def LCS(X, Y):
    """Return table such that L[j][k] is length of LCS for X[0:j] and Y[0:k]"""
    n, m = len(X), len(Y) # introduct convenient notations
    L = [[0] * (m+1) for k in range(n+1)]
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:
                L[j+1][k+1] = L[j][k] + 1
            else:
                L[j+1][k+1] = max([j][k+1], L[j+1][k])
    return L

def LCS_solution(X, Y, L):
    """Return the longest common substring of X and Y, given LCS table L."""
    solution = []
    j, k = len(X), len(Y)
    while L[j][k] > 0: # Keep looping until we hit a base condition
        if X[j-1] == Y[k-1]: # If X == Y --> case 1, must be 
            solution.append(X[j-1]) 
            j -= 1
            k -= 1

        # If no match, move to the larger of the the previous one
        elif L[j-1][k] >= L[j][k-1]:
            j -= 1
        else:
            k -= 1

        return ''.join(reversed(solution))