from pythonds3.graphs import PriorityQueue, Graph, Vertex

def prim(G, start):

    """ TO VISIT ALL LISTENERS, WITHOUT OVERLAP"""

    pq = PriorityQueue()

    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)

    start.setDistance(0)
    pq.buildHeap([ (v.getDistance(),v) for v in G ])

    while not pq.isEmpty():

        # Pop out the min keyed vertex, it would start with the starting vertex
        currentVert = pq.delMin()

        for nextVert in currentVert.getConnection():
            newCost = currentVert.getWeight(nextVert)

            # If it's still in the PQ, it hasn't beed added to the spanning tree yet
            if nextVert in pq and newCost < nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert, newCost)

