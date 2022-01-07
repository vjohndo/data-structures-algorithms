from HeapPriorityQueue import HeapPriorityQueue

def pq_sort(C):
    """Sort a collection of elements in a positional list"""
     
    n = len(C)
    P = HeapPriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)

    for j in range(n):
        (k,v) = P.remove_min()
        C.add_last(v)

