from pythonds3.graphs import PriorityQueue, Graph, Vertex

def dijkstra(aGraph, start):
    "aGraph: The graph we are running Dijkstra's on, start: the starting vertex"

    # Build the priority queue
    pq = PriorityQueue()

    # Set the starting vertex distance to 0. 
    # This is how the priority queue is sorted, the key is distance
    # hence by setting it to zero we start with this vertex when iterating
    start.setDistance(0)

    # Build a heap of all vertices in the graph
    # Note that initial distances for all nodes are set a sys.maxint
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])

    # Keep iterating through the priority queue until it is empty
    while not pq.isEmpty():

        # Take out the next item in the queue
        currentVert = pq.delMin()

        # Go through all the connections of the current vert
        for nextVert in currentVert.getConnections():

            # Calculate the new distance based on the distance to get to current node + distance from current node to next node
            # Notice how the starting node has distance of 0
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)

            # From this newly calcualted distance, check if it smaller than the new distance
            # (remember that the nodes are initially initialised with sys.max)
            if newDist < nextVert.getDistance(): 

                # If it's smalled, set the new distance
                nextVert.setDistance(newDist)

                # Say the the ideal path to the next node is from the current node
                nextVert.setPred(currentVert)

                # Update the vertex and move it towards the front of the queue.
                pq.decreaseKey(nextVert, newDist)