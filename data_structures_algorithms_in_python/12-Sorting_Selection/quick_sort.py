from base.queue import LinkedQueue

def quick_sort(S):
    """Sort the elements of queue S using the quick-sort algorithm"""
    n = len(S)
    if n < 2:
        return # list is already sorted
    
    p = S.first() # use first as arbitrary pivot
    L = LinkedQueue() # Set up queues for the three sequences; Less than
    E = LinkedQueue() # Equal to 
    G = LinkedQueue() # Greater than

    while not S.is_empty():
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())

    quick_sort(L)
    quick_sort(G)

    # Concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(E.dequeue())


def inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm
    
    a  will be leftmost index
    b  will be right most index
    """
    if a >= b:
        # Range is trivially sorted i.e. the leftmost and right most index are the same and is already sorted
        return

    pivot = S[b] # choose the last index as the pivot
    left = a
    right = b-1 # the right most index will be b - 1, b is the pivot
    while left <= right:
        # scan until reaching value equal to or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        
        # scan until reaching value equal to or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1

        if left <= right:
            S[left], S[right] = S[right], S[left] # will end up reassigning itself to itself if left = right
            left, right = left + 1, right - 1 # continue the process for the remining inside part of the sequence

    # eventually the above while loop will result in itemfromright < itemfromless
    # itemfromright will sit on the sequence L
    # itemfromleft will sit on sequence G
    # therefore to keep the order, swap itemfromleft with the pivot
    # we allow equal elements to pivot to be swapped
    S[left], S[b] = S[b], S[left]
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)