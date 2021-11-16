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
        # If an item is no longer in the priority queue that means it's part of the spanning tree
        currentVert = pq.delMin()

        for nextVert in currentVert.getConnection():

            # Prim's algo is a "greedy" algorithm, it always chooses the shortest path (think  back to 66 cents)
            # This may not necessarily be the most efficient
            newCost = currentVert.getWeight(nextVert)

            # Two conditions 
            # If it's still in the PQ, it hasn't beed added to the spanning tree yet !!!
            # That means we can set up predecessor, figure out distances, decrease keys but said item is not yet in spanning tree
            if nextVert in pq and newCost < nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert, newCost)

