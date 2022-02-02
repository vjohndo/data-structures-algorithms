from base.AdaptablePriorityQueue import AdaptableHeapPriorityQueue

def shortest_path_lengths(g, src):
    """Compute shortest-path distances from src to reachable vertices of g.
    
    Graph g can be undirected or directed, but must be weighted such that 
    e.element() returns a numeric weight for each edge e.

    Return dictionary mapping each reachable vertex to its distance from src
    """

    d = {} # d[v] is the upperbound from s to v
    cloud = {} # map reachable vertex to it's d[vertex value]
    pq = AdaptableHeapPriorityQueue() # vertex v will have key d[v]
    pqlocator = {} # map from vertex to its pq locator

    # for each vertex v of the graph, add an entry to the priority queue, with
    # The source having distance 0 and all others having infinite distance

    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')


        # save the locator for future updates, rememeber pq.add returns a Locator which we can access
        # pqlocator = {v: Locator}
        pqlocator[v] = pq.add(d[v], v)

    while not pq.is_empty():
        key, u = pq.remove_min # remove the min from the prioirty queue 
        cloud[u] = key # shortest path to u, i.e. added to cloud
        del pqlocator[u] # remove the locator, we don't need it anymore 

        for e in g.incident_edges(u):
            if v not in cloud:
                # perform relaxation step on edge (u, v)
                wgt = e.element()
                if d[u] + wgt < d[v]:
                    d[v] = d[u] + wgt
                    pq.update(pqlocator[v], d[v], v) # grabs and existing based on located updates(loc, newkey, newval):
    
    return cloud


def shortest_path_tree(g, s, d):
    """Reconstruct shortest-path tree rooted at vertex s, given distance map d.
    
    Return tree as a map from each reachable vertex v (other than s) to the
    edge e=(u,v) that is used to reach v from its parent u in the tree.
    """

    tree = {}
    for v in d: 
        if v is not s:
            for e in g.incident_edges(v, False): # consider the incoming edges
                
                # Check the vertices from the incoming edges
                # compare the shortest distances, if they match, must be the shortest path tree
                u = e.opposite(v)
                wgt = e.element()

                if d[v] == d[u] + wgt:
                    tree[v] = e # add in to the tree dictionary, the edge that is incoming to the vertex and is part of the shortest path.

    return tree 