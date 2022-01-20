def topological_sort(g):
    """Return a list of vertices of directed acyclic graph g in topological order.
    
    If graph g has a cycle, the result will be incomplete
    """
    topo = [] # a list of vertices placed in topological order
    ready = [] # list of vertices that have no remainin constraints and can be visited
    incount = {} # used to keep track of in-degree for each vertex
    for u in g.vertices(): # go through all the vertices
        incount[u] = g.degree(u, False) # Get the incoming degree... remember degree(node, outgoing=True)
        if incount[u] == 0: # if u has no incoming edges
            ready.append(u) # it is free of constraints and is ready to be looked at

    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)
        for e in g.incident_edgess(u): # at this stage there will ONLY be outgoing edges
            v = e.opposite(u)
            incount[v] -= 1 # reduce the incount of v by one, we've just added it's opposite u inthe the order
            if incount[v] == 0: # should it reach 0, it is now free of incoming restraints and can be added
                ready.append(v)

