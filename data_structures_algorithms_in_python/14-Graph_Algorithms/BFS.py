def BFS(g, s, discovered):
    """Perform BFS of the undiscovered portion of Graph g starting at Vertex s.
    
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    """
    level = [s] # first leve includes only s
    while len(level) > 0:
        next_level = [] # prepare to gather new vertices
        for u in level:
            for e in g.incident_edges(u): # for every outgoing edge from u
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v) # v will be further considered in the next pass
        
        # After looking at all adjacent nodes and adding them to next level
        # make level = next_level for the while loop to continue
        level = next_level