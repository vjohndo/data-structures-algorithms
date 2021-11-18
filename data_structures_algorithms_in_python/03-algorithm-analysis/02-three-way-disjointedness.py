

def disjointJohn(A,B,C):
    """ Return true if there is no element common to all three lists"""
    

def disjoint1(A,B,C):
    """ Following implementation is O(n^3) """
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True

def disjoint2(A,B,C):
    """ Let's only check C if a=b have matching values """
    for a in A: # O(n)
        for b in B: # O(n^2)
            if a == b: # O(n^2)
                for c in C: # O(n^2) --> There can be at most O(n) instances where a == b i.e. all "a" are elements of A and B and for c in C runs O(n)
                    if c == a:  # In the worst case will run O(n^2)
                        return False
    return True

def unique1(S):
    """ Return True if there are no duplicate elements in sequence """
    for j in range(len(S)): # O(n) Loop through the list
        for k in range(j + 1, len(S)): # O(n^2) Then look through the rest to see if anything is there ... remember 1 + 2 + 3 + ... + (n-2) + (n-1) + n = n(n+1)/2
            if S[j] == S[k]: # O(n^2)
                return False 

def unique2(S):
    """ Return True if there are no duplicate elements in sequence S. """
    temp = sorted(S) # Sorting the list will be O(n*log(n))
    for j in range(1, len(temp)): # Runing through the sorted list will be O(n)
        if S[j-1] == S[j]:
            return False
    return True

    # Hence algorithm will run in O(n*log(n))


