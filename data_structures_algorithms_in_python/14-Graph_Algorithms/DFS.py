from Graph import Graph

g = Graph()
u = g.insert_vertex('u')

def DFS(g, u, discovered):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
    
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dicitonary as a result
    """

    for e in g.incident_edges(u): # For every outgoing edge from u (rememeber incident_edge(vertex, outgoing=True))
        v = e.opposite(u)
        if v not in discovered: # v is an unvisited index
            discovered[v] = e # e is the tree edge that discovered v, we will be able to use this to trace a path
            DFS(g, v, discovered) # recursively explore from v


# We assume the source vertex u occurs a key of the dictionary. 
# Below is a sample of how a user may call upon the DFS
result = {u : None}
DFS(g, u, result)


# We can reconstruct a path by starting from end node and trace back using the edge it was discovered by
def construct_path(u, v, discovered):
    """Provides a path from vertices u to v"""
    path = []
    if v in discovered:
        # build a list from v to u and then reverse it at the end
        path.append(v) 
        walk = v
        while walk is not u:
            e = discovered[walk] # get the edge that discovered the current "walk" vertex
            parent = e.opposite(walk)
            path.append(parent) # add the parent to the list
            walk = parent
        path.reverse() # reorient path from u to v
    return path

def DFS_complete(g):
    """Perform DFS for entire graph and reutrn forest as a dictionary
    
    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None.)
    """
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None # set u as the start of a new DFS tree
            DFS(g, u, forest)
    return forest


