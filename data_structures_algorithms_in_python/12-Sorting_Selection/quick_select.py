def quick_select(S, k):
    """Return the kth smallest element of list S, for k from 1 to len(S)."""
    if len(S) == 1:
        return S[0]

    pivot = random.choice(S) # Pick random pivot element from S
    L = [x for x in S if x < pivot]
    E = [x for x in S if x == pivot]
    G = [x for x in S if pivot < x]

    if k <= len(L):
        # If we want to the return the kth smallest element where k is less than len(L)
        # We know that it must lie within the L sequence 
        # run quick select on smaller sequence
        return quick_select(L, k)
    
    elif k <= len(L) + len(E):
        # If kth element less than the number of elements that are less than or equal to the pivot
        # kth smallest element must be the pivot
        return pivot
    
    else:
        # Otherwise the kth element must be in the G sequence
        # A kth element in the S sequence must be the jth element in the G sequence (hence k - len(l) 0 len(e)) 
        j = k - len(L) - len(E)
        # run quick select on the smaller sequence
        return quick_select(G, j)
