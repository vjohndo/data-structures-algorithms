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
    