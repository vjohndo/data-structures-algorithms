from base.AdaptablePriorityQueue import AdaptableHeapPriorityQueue

def MST_PrimJarnik(g):
    """Compute a minimum spanning tree of weighted graph g.
    
    Return a list of edges that comprise the MST (in arbitrary order)
    """
    d = {} # d[v] is a bound on the distance to the tree
    tree = [] # list of edges in the spanning tree
    pq = AdaptableHeapPriorityQueue() # d[v] maps to value (v, e=(u,v)) ... notice how the second argument is an edge
    pqlocator = {} # map from vertex to its pq locator

    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if len(d) == 0: 
            d[v] = 0
        else:
            d[v] = float('inf')
        # pqlocator = (v: Locator)
        pqlocator[v] = pq.add(d[v], (v, None)) 
    
    while not pq.is_empty():
        key, value = pq.remove_min() # grab the lowest key item
        u, edge = value # unpack tuple from pq
        del pqlocator # remove it from the pqlocator, we can't ever acces it again

        if edge is not None: # I.e. starting node or leaf node
            tree.append(edge)
        
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqlocator: # if we've already added v to the tree, it skips all the code below.
                # Check the edge (u,v) better connects v to the growing tree
                wgt = link.element()
                if wgt < d[v]:
                    d[v] = wgt
                    pq.update(pqlocator[v], d[v], (v, link))

    return tree