from base.queue import LinkedQueue

def merge(S1, S2, S):
    """Merge two sorted queue instances S1 and S2 into empty queue S."""
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    
    # Eventually one of the queues will become empty
    while not S1.is_empty():
        S.enqueue(S1.dequeue())
    while not S2.is_empty():
        S.enqueue(S2.dequeue())

def merge_sort(S):
    """Sort the elements of queue S using the merge-sort algorithm"""
    n = len(S)
    if n < 2:
        return 

    #divide
    S1 = LinkedQueue()
    S2 = LinkedQueue()

    while len(S1) < n // 2: # Move the first n//2 elements into S1
        S1.enqueue(S.dequeue())
    while not S.is_empty(): # Move the rest to S2
        S2.enqueue(S.dequeue())
    
    merge_sort(S1) # Sort first queue
    merge_sort(S2) # Sort second queue

    merge(S1, S2, S) # merge the sorted halves back into S