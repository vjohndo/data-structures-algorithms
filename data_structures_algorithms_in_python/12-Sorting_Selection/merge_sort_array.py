def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S"""
    i = j = 0
    while i + j < len(S): # keep looping while the total of i and j are less than the S
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            # If j has not been fully added, or if i has not been added & i is less than j
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1

def merge_sort(S):
    """Array based inmplementation of the merge sort"""
    n = len(S)
    if n < 2: 
        return # i.e. make no changes to S
    
    mid = n//2
    S1 = S[0:mid] # Upto but not including mid
    S2 = S[mid:n] # Upto but not including n

    merge_sort(S1) # recur on S1
    merge_sort(S2) # recur on S2

    merge(S1, S2, S)